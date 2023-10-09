#!/bin/bash

var=$1

if [[ $var -gt 5 ]]
then
  echo "one" 
elif [[ $var -lt 3 ]]
then
  echo "two"
elif [[ $var -eq 4 ]]
then
  echo "three"
else
  echo "four"
fi