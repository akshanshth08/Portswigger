#!/bin/bash
>input.lst
while read x
do
echo "peter">>input.lst
echo $x >>input.lst
done<password.lst
