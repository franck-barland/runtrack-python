#!/bin/bash

A=$1
B=$2
C=$3

echo "Vous avez entré $A $B $C"

if [[ -z "$A" || -z "$B" || -z "$C" ]]; then
	echo "Vous n'avez pas entré les bons arguments"
	exit 1

elif [[ "$B" == "+" ]]; then
	Res=$(($A + $C))
	echo "Le résultat est : $A + $C = $Res"

elif [[ "$B" == "-" ]]; then
	Res=$(($A - $C))
	echo "Le résultat est : $A - $C = $Res"

elif [[ "$B" == "*" ]]; then
	Res=$(($A * $C))
	echo "Le résultat est : $A * $C = $Res"

elif [[ "$B" == "/" ]]; then
	if [[ $C -eq 0 ]]; then
		echo "Erreur : Division par zéro impossible"
		exit 1
	else
		Res=$(($A / $C))
		echo "Le résultat est : $A / $C = $Res"
	fi

else
	echo "Vous n'avez pas entré les bons arguments"
	exit 1
fi