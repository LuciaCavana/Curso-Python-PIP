import msvcrt
def pres_key():
    print("\nPresione 'Esc' para continuar...")
    key = None
    while key != '\x1b':
        key = msvcrt.getwch()
    return True

def compare(cadena, comparar):
    if cadena.upper().strip() == comparar.upper().strip():
        return True
    else:
        return False 

def dict_a_list(dict):
    labels = ['0']
    values = [0]
    for keys in dict.keys():
        values.append(int(dict[keys]))
        labels.append(keys)
    return labels, values
