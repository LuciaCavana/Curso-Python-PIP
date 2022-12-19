import read_csv as rscv
import charts 
menu = rscv.keys
path = 'C:/Users/lcavana/Documents/py-project/Poblation_CSV_Proyectdata.csv/data.csv'
Continent = ['South America', 'North America', 'Asia', 'Europe', 'Africa', 'Oceania']

def pintar_menu():
   for i in menu.items():
        if i[0] not in (2,3,4,5):
                print(f'{i[0]} - {i[1]}')

def Grafic_population():
    name = str(input('Ingresa la CCA3 del pais solicitado: '))
    data = rscv.read_csv(path)
    if rscv.existencia_CCA3(data,name):
        labels,values, nombre = rscv.pais(data,name)
        charts.generate_bar_chart(labels,values,'Poblacion de '+nombre)
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
                        charts.generate_bar_chart(labels,values,nombre)
                else:
                        print('el numero de la columna no puede ser 2,3,4 y 5')
        else:
                print('El Numero de la columna no existe')
    except ValueError:
        print('El valor ingresado no es un numero entero')

def print_Continent():
        print('*'*5+'Menu'+'*'*5)
        for item in Continent:
                print(item) 
        print('*'*11)
        user_continent = input('Elegi que continente desea visualizar => ')
        if not user_continent.lower().title() in Continent:
                print('Error, la opcion no se encuentra en la lista')
                return None
        return user_continent
        

def Grafic_Continent():
        pintar_menu()
        try: 
                cont = print_Continent()
                if not cont == None:
                        data = rscv.read_csv(path)
                        data = list(filter(lambda item:item['Continent']==cont,data))
                        countries= list(map(lambda x:x[rscv.keys[3]],data))
                        percentages= list(map(lambda x:x[rscv.keys[17]],data))
                        charts.generate_pie_chart(countries, percentages)
        except ValueError:
                print('Error')


if __name__ == '__main__':
        Grafic_Continent()