import secrets 
import string 

def generate_user_id(length=11): 
    # Caracteres posibles para el ID aleatorio
    characters = string.ascii_letters + string.digits 

    # Genera un ID aleatorio de la longitud deseada
    random_id = ''.join(secrets.choice(characters) for _ in range(length))
    return random_id

def generate_user_id_int(length=6): 
    characters = string.digits 

    random_id = ''.join(secrets.choice(characters) for _ in range(length))
    return random_id