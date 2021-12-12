#!/bin/bash
#usage: validate.sh path/to/data

ga() {
    gawk 'BEGIN {
            FS=",";
            OFS=",";
            FPAT = "([^,]+)|(\"[^\"]+\")"
        }         
        #Yeetus
        {   
            if(NR==1) {
                print "Station name,Station ID"
            } else {
                if (substr($3, 1, 1) == "\"") {
                    len = length($3)
                    $3 = substr($3, 2, len - 2)    # Get text within the two quotes
                    sub(/,/, ";", $3)

                }
                print $2,$3;
            }
        }
        
        END {print FILENAME, e > "/dev/stderr"}' "$1" 
}

mkdir -p Data
ga $1 | cat > "Data/stations.csv"




