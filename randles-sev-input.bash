#!/bin/bash
declare -a list=("0.00000597 1 0.395 0.000003 0.1" "0.00000428  1 0.395 0.000003 0.07" "0.00000280 1 0.395 0.000003 0.05" "0.00000230 1 0.395 0.000003 0.04" "0.00000136 1 0.395 0.000003 0.02" "0.00000092 1 0.395 0.000003 0.01" "0.00000065 1 0.395 0.000003 0.005")

for i in "${list[@]}"
do
  python randles-sevcik-equation.py $i
#  echo "$i"
  done

