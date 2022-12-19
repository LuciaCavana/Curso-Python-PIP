import random

def choose_option():
    options = ('piedra', 'papel','tijera')
    user_option=input('piedra, paptel o tijera =>')
    user_option= user_option.lower()

    #verificar si la opcion elegida por el usuario esta dentro de las opciones
    if not user_option in options:
        print('esa opcion no es valida')
        return None, None

    computer_opcion = random.choice(options)

    print('User Option =>',user_option)
    print('Computer Option =>',computer_opcion)
    return user_option, computer_opcion

def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print('Empate!')
    elif user_option=='piedra':
        if computer_option == 'tijera':
            print('Piedra gana a tijera \n user gano!')
            user_wins +=1
        else:
            print('Papel gana a piedra \n computer gano!')
            computer_wins +=1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('papel gana a piedra \n user gano!')
            user_wins +=1
        else:
            print('tijera gana a papel \n computer gano!')
            computer_wins +=1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('tijera gana a papel \n user gano!')
            user_wins +=1
        else:
            print('piedra gana a tijera \n computer gano!')
            computer_wins +=1
    return user_wins, computer_wins


#INICIO DEL JUEGO
def run_game():
    computer_wins = 0
    user_wins = 0
    rounds = 1
    while True:
        print('*' * 10)
        print('ROUND',rounds)
        print('*' * 10)

        user_option, computer_option = choose_option()
        user_wins, computer_wins = check_rules(user_option,computer_option, user_wins, computer_wins)

        if computer_wins == 2:
            print('El ganador es la computadora')
            break
        elif user_wins == 2:
            print('El ganador es el usuario!')
            break

run_game()
