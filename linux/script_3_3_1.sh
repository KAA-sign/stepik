#!/bin/bash

if [[ -n $0 ]]
  then 
  echo "True1"
fi

if [[ -z "" ]]
  then
  echo "True2"
fi

if [[ ! (4 -le 3) ]]
  then
  echo "True3"
fi

if [[ -e $0 ]]
  then
  echo "True4"
fi

if [[ $var1 == $var2 || $var1 != $var2 ]]
  then
  echo "True5"
fi

if [[ 5 -ge 5 ]]
  echo "True6"
fi
