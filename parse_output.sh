#!/usr/bin/env bash

OUTPUT_FILE="$1"

number_of_wins=`grep WIN $OUTPUT_FILE | wc | awk '{print $1}'`
number_of_losses=`grep LOSS $OUTPUT_FILE | wc | awk '{print $1}'`
echo "File: $OUTPUT_FILE Wins: $number_of_wins Losses: $number_of_losses"
