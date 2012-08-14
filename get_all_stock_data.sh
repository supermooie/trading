#!/usr/bin/env bash

while read line; do
  echo $line
  ./get_stock_data.sh $line
done < stock_list
