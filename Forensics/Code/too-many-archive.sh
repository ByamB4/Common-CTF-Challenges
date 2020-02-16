#!/bin/bash

filename=$1

rm -r tmp
mkdir tmp
cp $filename tmp

cd tmp
file $filename

file $filename | grep "gzip"

while [ 1 ]
do
  file $filename | grep 'gzip'
  if [ "$?" -eq "0" ]
  then
    echo '[+] gzip'
    mv $filename $filename.gz
    ls
    gzip -d $filename.gz
    filename=$(ls *)
  fi
  file $filename | grep 'Zip'
  if [ "$?" -eq "0" ]
  then
    echo '[+] zip'
    mv $filename $filename.zip
    ls
    unzip $filename.zip
    rm $filename.zip
    filename=$(ls *)
  fi

  file $filename | grep 'bzip2'
  if [ "$?" -eq "0" ]
  then
    echo '[+] bzip2'
    mv $filename $filename.bz2
    bunzip2 $filename.bz2
    filename=$(ls *)
  fi
  
  file $filename | grep 'POSIX'
  if [ "$?" -eq "0" ]
  then
    echo '[+] POSIX'
    tar -xf $filename
    filename=$(ls *)
  fi

  file $filename | grep 'XZ'
  if [ "$?" -eq "0" ]
  then
    echo '[+] XZ'
    mv $filename $filename.xz
    xz -d $filename.xz
    filename=$(ls *)
  fi
done
