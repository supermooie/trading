#!/usr/bin/env bash

# 
# Downloads year data for the ASX share code. Saves file as <ASX CODE>.csv
#
# Requies: curl
#
# Input: ASX share code
#
# Author: Jonathan Khoo
# Date:   4.08.12
#

# Usage: ./get_stock_data.sh <ASX CODE>

function usage()
{
	echo "`basename $0` <ASX CODE>"
}

ARGC=$#
if [ $ARGC -ne 1 ]; then
	usage
	exit 0
fi

CODE=$1

echo "Retrieving data from tradingroom.com.au for $CODE."

curl "http://www.tradingroom.com.au/apps/qt/csv/pricehistory.ac?section=yearly_price_download&code=$CODE" --O $CODE.csv
