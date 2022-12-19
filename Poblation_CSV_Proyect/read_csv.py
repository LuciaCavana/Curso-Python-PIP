import utiles as u
import csv
keys = {
        1:'Rank', #int
        2:'CCA3',
        3:'Country/Territory',
        4:'Capital',
        5:'Continent',
        6:'2022 Population',#int
        7:'2020 Population',#int
        8:'2015 Population',#int
        9:'2010 Population',#int
        10:'2000 Population',#int
        11:'1990 Population',#int
        12:'1980 Population',#int
        13:'1970 Population',#int
        14:'Area (kmÂ²)',#float
        15:'Density (per kmÂ²)',#float
        16:'Growth Rate',#float
        17:'World Population Percentage',#float
}

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data

def Todo(data):
  for i in data:
    for string in keys.items():
      print(f'{string[1]}: {i[string[1]]}')

def existencia_CCA3(data,name):
  boolean = False
  for i in data:
    if u.compare(i['CCA3'],name): 
        boolean = True
  return boolean

def existencia_Column(column):
  boolean = False
  for i in keys.keys():
    if i == column: 
        boolean = True
  return boolean

def pais(data, name):
  labels = ['0']
  values = [0]
  for i in data:
    if u.compare(i['CCA3'],name):
      for key in keys.items():
        if key[0] in (6,7,8,9,10,11,12,13):
          labels.append(key[1])
          values.append(int(i[key[1]]))
        if key[0] == 3:
          nombre = i[key[1]]
  return labels,values, nombre

def column(data,columna):
  labels = []
  values = []
  for i in data:
      labels.append(i[keys[3]])
      if columna in (1,6,7,8,9,10,11,12,13):
         values.append(int(i[keys[columna]]))
      elif column in (14,15,16,17):
         values.append(float(i[keys[columna]]))
      else:
         values.append(i[keys[columna]])
      nombre = keys[columna]
  return labels,values, nombre

