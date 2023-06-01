A=$1
B=$2

# test si un ou les deux arguments sont vides
if [[ -z "$A" || -z "$B" ]]; then
	echo "Merci de remplir un ou les deux arguments!!!"
	exit 1

	# test sur l'extension '.txt' sur le premier argument 
	elif [[ "${A: -4}" ! = ".txt" ]]; then
		echo "Votre premier argument doit être un fichier .txt!!!" 
		exit 1

	# les conditions sont alors remplies alors la suvegarde peut s'effectuer
	else 
		cp "$A" "copyfile.txt"
		echo "Sauvegarde effectuée avec succès."
fi

