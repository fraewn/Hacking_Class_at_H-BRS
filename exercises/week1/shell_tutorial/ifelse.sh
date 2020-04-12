#!/bin/sh
Y=h
X=h
Z=b

if [ $X = $Y ]
then 
	echo "same"
else 
	echo "not same"
fi 

if [ $X = $Y ]; then 
	echo "same with then in line"
fi 

if [ $Z = $Y ]; then 
	echo "same third"
elif [ $X = $Y ]; then 
	echo "elif jojo"
else
	echo "last else"
fi 

