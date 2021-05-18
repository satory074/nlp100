#!/bin/zsh
sed "s/\t/ /g" in/hightemp.txt > out/11_sed_out.txt
cat in/hightemp.txt | tr '\t' ' ' > out/11_tr_out.txt
expand -t 1 in/hightemp.txt > out/11_expand_out.txt