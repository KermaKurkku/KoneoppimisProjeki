#!/bin/sh
#usage: convert_data.sh /path/to/files

validate() {
    gawk 'BEGIN {
			FS=",";
			OFS=",";
			FPAT = "([^,]+)|(\"[^\"]+\")"
		} 
        
        #tarkistetaan idt, matka 0-25km, aika 0-5h
        {
			if (NR!=1 && $3 > 0 && $5 > 0 && $7 > 0 && $7 < 25000 && $8 > 0 && $8 < 18000) {
				print $1,$2, $3, $5;
			} else {
				e++
			}
		}
        
        END {print FILENAME, e > "/dev/stderr"}' "$1" 
}

combine() {
    gawk 'BEGIN {FS=","; OFS=",";}
        {   
			gsub(/"/, "")
			if ((NR!=1 && NF!=4) || $1<0 || $2<0 || $3<0 || $4<0 || $0 ~/[a-zA-Z]/) {
				e++
				print $0 > "/dev/stderr"
			} else {
				print $0
			}
        } END {print "Incorrect rows ",  e > "/dev/stderr"}
    ' "$1" 
}

cwd=$PWD

cd "$1"
mkdir -p /tmp/convertDataPy
for i in *.csv
do
	validate "$i" > /tmp/convertDataPy/temp-$i
	python3 $cwd/convert_data.py /tmp/convertDataPy/temp-$i
done



cd /tmp/convertDataPy
mkdir -p $cwd/Data
echo "Departure,Return,Departure station id,Return station id" > $cwd/Data/station_data.csv

for i in temp-*.csv
do
	echo "Combining files"
	combine $i >> $cwd/Data/station_data.csv
done

rm -rf /tmp/convertDataPy