
# ======================== 8 kyu Welcome! =============================



# # The Database

# languages = { 
# 'english': 'Welcome',
# 'czech': 'Vitejte',
# 'danish': 'Velkomst',
# 'dutch': 'Welkom',
# 'estonian': 'Tere tulemast',
# 'finnish': 'Tervetuloa',
# 'flemish': 'Welgekomen',
# 'french': 'Bienvenue',
# 'german': 'Willkommen',
# 'irish': 'Failte',
# 'italian': 'Benvenuto',
# 'latvian': 'Gaidits',
# 'lithuanian': 'Laukiamas',
# 'polish': 'Witamy',
# 'spanish': 'Bienvenido',
# 'swedish': 'Valkommen',
# 'welsh': 'Croeso'
# }

# def greet(language):
#     if language in languages.keys():
#         print(languages[language])
#     else:
#         print('ip address not in the database')
# greet('welsh')




languages = {
    'english': 'Welcome',
    'czech': 'Vitejte',
    'danish': 'Velkomst',
    'dutch': 'Welkom',
    'estonian': 'Tere tulemast',
    'finnish': 'Tervetuloa',
    'flemish': 'Welgekomen',
    'french': 'Bienvenue',
    'german': 'Willkommen',
    'irish': 'Failte',
    'italian': 'Benvenuto',
    'latvian': 'Gaidits',
    'lithuanian': 'Laukiamas',
    'polish': 'Witamy',
    'spanish': 'Bienvenido',
    'swedish': 'Valkommen',
    'welsh': 'Croeso'
}


def greet(language):
    return languages.get(language, 'Welcome')  # Default to English if not found or invalid input




  # Default to English if not found or invalid input


# def welcome(language):
#     greeting = greet(language)
#     return greeting



# Example usage
print(greet('english'))  # Output: Welcome
print(greet('french'))  # Output: Bienvenue
print(greet('german'))  # Output: Willkommen
print(greet('japanese'))  # Output: Welcome (Not in the database, defaults to English)
print(greet(''))  # Output: Welcome (Invalid input, defaults to English)



# Possible invalid inputs include:

# IP_ADDRESS_INVALID - not a valid ipv4 or ipv6 ip address
# IP_ADDRESS_NOT_FOUND - ip address not in the database
# IP_ADDRESS_REQUIRED - no ip address was supplied