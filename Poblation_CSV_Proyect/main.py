import read_csv as rscv
import grafic as grc
import utiles as u

menu = rscv.keys
path = 'C:/Proyectos/PycharmProjects/Curso de Python (Comprehensions, Funciones y Manejo de Errores)/Poblation_Proyect/data.csv'

def pintar_menu():
   for i in menu.items():
        if i[0] not in (2,3,4,5):
                print(f'{i[0]} - {i[1]}')

def Grafic_population():
    name = str(input('Ingresa la CCA3 del pais solicitado: '))
    data = rscv.read_csv(path)
    if rscv.existencia_CCA3(data,name):
        labels,values, nombre = rscv.pais(data,name)
        grc.generate_bar_chart(labels,values,'Poblacion de '+nombre)
    else:
        print('CCA3 erroneo, ingrese uno correcto')

def grafic_column():
    pintar_menu()
    try:    
        columna = int(input('Ingresa el numero de la columna que deseas: '))
        if rscv.existencia_Column(columna):
                if columna not in (2,3,4,5):
                        data = rscv.read_csv(path)
                        labels, values,nombre = rscv.column(data,columna)
                        grc.generate_bar_chart(labels,values,nombre)
                else:
                        print('el numero de la columna no puede ser 2,3,4 y 5')
        else:
                print('El Numero de la columna no existe')
    except ValueError:
        print('El valor ingresado no es un numero entero')


if __name__ == '__main__':
        grafic_column()