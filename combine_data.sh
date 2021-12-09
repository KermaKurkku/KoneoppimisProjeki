#!/bin/bash
#usage: validate.sh path/to/data

ga() {
    gawk 'BEGIN {FS=","; OFS=",";}         
        #Yeetus
        {   
            if(NR==1) {
                e++
            } else {
                print $0;
            }
        }
        
        END {print FILENAME, e > "/dev/stderr"}' "$1" 
}

cd "$1"
for i in 2020-*.csv
do 
    echo "Departure,Return,Departure station id,Return station id" > "2020.csv"
    ga "$i" >> "2020.csv"
done

