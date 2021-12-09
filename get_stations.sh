#!/bin/bash
#usage: validate.sh path/to/data

ga() {
    gawk 'BEGIN {FS=","; OFS=",";}         
        #Yeetus
        {   
            if(NR==1) {
                print "Station name,Station ID"
            } else {
                print $2,$3;
            }
        }
        
        END {print FILENAME, e > "/dev/stderr"}' "$1" 
}

ga "Data/Helsingin_ja_Espoon_kaupunkipyöräasemat_avoin.csv" | cat >> "Data/stations.csv"




