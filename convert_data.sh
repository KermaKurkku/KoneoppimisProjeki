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
			print $0
        }
    ' "$1" 
}

convert() {
	gawk 'BEGIN {FS=",";}
		NR==1 {print "Departure day,Departure hour,Return day,return hour,Departure station id,Return station id"}
		{
			gsub(/\./, ",")
			gsub(/\"/, "")
			if (NR!=1 && NF<6) {
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
echo "" > station_data-temp.csv
for i in temp-*.csv
do
	echo "Combining files"
	combine $i >> station_data-temp.csv
done

mkdir -p $cwd/Data

convert station_data-temp.csv > $cwd/Data/station_data.csv

rm -rf /tmp/convertDataPy