A=$1

echo "Vous venez(1) ou vous partez(2)?"
# test présence d'argument
if [[ -z "$A" ]]; then
	echo "Veillez à savoir venez ou vous partez!"
	exit 1

elif [[ "$A" -eq "Hello" ]]; then
	echo "Bonjour, je suis un script!"
	exit 1

elif [[ "$A" -eq "Bye" ]]; then
	echo "au revoir et bonne journée"
	exit 1

else 
	echo "merci de passer les bons paramètres!"

fi
