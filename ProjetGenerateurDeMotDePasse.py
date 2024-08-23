#Importation des modules
import random
import string
#Définition de la fonction pour générer un mot de passe avec des paramètres pour la longueur minimale, l'inclusion de chiffres et de caractères spéciaux
def generate_password(min_length, numbers=True, special_characters= True) :
    letters = string.ascii_letters #les lettres en maj et min
    digits = string.digits #les chiffres de 0 a 9
    special = string.punctuation #les caracteres speciaux
    
    characters = letters # Commence avec uniquement les lettres comme base
    if numbers:
        characters += digits  # Ajoute les chiffres si demandé
    if special_characters:
        characters += special  # Ajoute les caractères spéciaux si demandé
    pwd=""  # Initialisation de la chaîne de caractères 
    meets_criteria = False  # Indicateur pour vérifier si le mot de passe répond aux critères
    has_number= False # Indicateur pour vérifier si le mot de passe contient un chiffre
    has_special= False # Indicateur pour vérifier si le mot de passe contient un caractère spécial
# Boucle pour générer des caractères jusqu'à ce que le mot de passe soit conforme aux critères de nos specifications
    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters) # Sélectionne un caractère aléatoire parmi les caractères possibles
        pwd+= new_char # Ajoute ce caractère au mot de passe

        if new_char in digits:
            has_number = True # Vérifie si le caractère ajouté est un chiffre
        elif new_char in special:
            has_special= True # Vérifie si le caractère ajouté est un caractère spécial

        meets_criteria=True # dans le cas ou le mot de passe répond aux critères
        if numbers:
            meets_criteria=has_number 
        if special_characters:
            meets_criteria= meets_criteria and has_special

    return pwd # Retourne le mot de passe généré

min_length = int(input("Enter the minimum length"))
has_number= input("Do you want have numbers (y/n)").lower()=="y"
has_special= input("Do you want have special characters (y/n)").lower()=="y"
pwd= generate_password(min_length, has_number, has_special) # Génère un mot de passe selon les critères de l'utilisateur specifiees
print("The generated password is:", pwd) # Affiche le mot de passe généré


generate_password(10) # Génère un mot de passe avec une longueur minimale de 10 caractères (ligne de test)