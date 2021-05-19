#!/bin/zsh
cat out/11_expand_out.txt | cut -d " " -f 1 > out/col1.txt
cat out/11_expand_out.txt | cut -d " " -f 2 > out/col2.txt