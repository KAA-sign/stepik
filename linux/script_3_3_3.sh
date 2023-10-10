#!/bin/bash

var=$1

if [[ $var -eq 0 ]]
then
  echo "No students"
elif [[ $var -eq 1 ]]
then
  echo "$var student"
elif [[ $var -le 4 ]]
then
  echo "$var students"
else
  echo "A lot of students"
fi