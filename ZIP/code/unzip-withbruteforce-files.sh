for i in {0..139}; do
    file="all_the_zips/zip$i.zip";
    echo "$file";
    fcrackzip -D -u -p /usr/share/dict/words "$file" | grep "PASSWORD FOUND";
done