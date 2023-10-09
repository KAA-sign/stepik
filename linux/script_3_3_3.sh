#!/bin/bash

var=$1

if [[ $var -eq 0 ]]
  then
  echo "No students"
elif [[ $var -le 4 ]]
then
  echo "students"