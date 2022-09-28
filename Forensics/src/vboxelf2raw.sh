#!/usr/bin/env bash

FILE=$1
OUTFILE=$2

set -e

failed() {
    echo "$1"
    exit 1
}

if [ -z $1 ]; then
   failed "usage: $0 <infile> <outfile>"
fi

if [ -z $2 ]; then
   failed "usage: $0 <infile> <outfile>"
fi

[ -f "$FILE" ] || failed "no such file or directory"
[ -f "$OUTFILE" ] && failed "outfile exists"

touch $OUTFILE

ELF_BASE_ADDRESS=0
while IFS= read -r SECTION; do
    CURRENT_SECTION_SIZE=$((16#$(echo $SECTION | cut -f1 -d' ')))
    CURRENT_SECTION_OFFSET=$((16#$(echo $SECTION | cut -f2 -d' ')))
    CURRENT_FILE_OFFSET=$((16#$(echo $SECTION | cut -f3 -d' ')))
    if [ $CURRENT_SECTION_SIZE -eq 0 ]; then
        continue
    fi

    FILE_SIZE=$(ls -l $OUTFILE | cut -d' ' -f5)
    PAD_SIZE=$(($CURRENT_SECTION_OFFSET - $FILE_SIZE))
    dd if=/dev/zero of=$OUTFILE bs=4096 seek=$(($FILE_SIZE / 4096)) count=$(($PAD_SIZE / 4096)) 2>/dev/null
    dd if=$FILE bs=16 skip=$(($CURRENT_FILE_OFFSET / 16)) count=$(($CURRENT_SECTION_SIZE / 16)) 2>/dev/null | dd of=$OUTFILE bs=4096 seek=$(($CURRENT_SECTION_OFFSET / 4096))
done < <(objdump -h $FILE  | egrep load | awk '{print $3, $5, $6}')
