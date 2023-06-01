A=$1
B=$2
C=$3

echo "vous avez entré $A $B $C"

if [[ -z "$A" || -z "$B" || -z "$C" ]]; then
	echo "Vous n'avez pas entré les bons arguments"
	exit 1

elif [[ "$B" == "+" ]]; then
	Res=$(($A+$B))
	echo "le résultat est: $A + $C = $Res"

elif [[ "$B" == "-" ]]; then
	Res=$(($A-$B))
	echo "le résultat est: $A - $C = $Res"

elif [[ "$B" == "*" ]]; then
	Res=$(($A*$B))
	echo "le résultat est: $A * $B = $Res"

elif [[ "$B" == "/" ]]; then
	Res=$(($A/$B))
	echo "le résultat est: $A / $B = $Res"

else
	echo "Vous n'avez pas entré les bons arguments"
	exit1
fi

