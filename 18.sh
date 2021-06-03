#!/bin/zsh
sort -t$'\t' -k 3,3 -r -n './in/hightemp.txt' | > 'out/18.txt'