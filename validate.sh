#!/bin/bash
#usage: validate.sh path/to/data

ga() {
    gawk 'BEGIN {FS=","; OFS=",";} 
        NR==1 {print $1,$2, $3, $5}
        
        #tarkistetaan idt, matka 0-20km, aika 0-3h
        {if ($3 > 0 && $5 > 0 && $7 > 0 && $7 < 20000 && $8 > 0 && $8 < 10800) 
        print $1,$2, $3, $5;
        else e++}
        
        END {print FILENAME, e > "/dev/stderr"}' "$1" 
}

cd "$1"
for i in *.csv
do 
    ga "$i" > "new-$i"
done

