import csv

'''
def read_csv(path):
  with open(path, "r") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data
    
if __name__ == "__main__":
  data = read_csv("./app/world_population.csv")
  print(data)
  for dict in data:
    dict.pop("Rank")
    dict.pop("CCA3")
    dict.pop("Country/Territory")
    dict.pop("Capital")
    dict.pop("Continent")    
    dict.pop("Area (km²)")    
    dict.pop("Density (per km²)")    
    dict.pop("Growth Rate")
    dict.pop("World Population Percentage")

  print(data)
  '''

'''
with open('app/world_population.csv','r') as data:
  reader1 = csv.reader(data)
  header = next(reader1)
  data1=[]
  for line in reader1:
    codict = dict() # dict vacío
    for i,j in zip(header,line):
      if '20' in i or "19" in i:
        codict[i]=j
    data1.append(codict)

print(data1)
'''

''' No funciona aún:
with open("./app/world_population.csv", "r") as data:
  reader = csv.reader(data)
  column_to_read = input("qué columna pa ? => ")
  header = next(reader)
  world_pop = []
  one_column = []
  for row in reader:
    country_dict = dict(zip(header, row))
    world_pop.append(country_dict)
    for country_dict in world_pop:
      column = {i: j for i, j in country_dict if column_to_read in i}
      one_column.append(column)
print(one_column)
'''


def joder():
  with open('app/world_population.csv','r') as data:
    reader = csv.reader(data)
    header = next(reader)
    column_to_read = input("qué columna pa => ")
    country_names = []
    column = []
    country_column = []
    for row in reader:
      codict_names = dict() # dict vacío
      codict = dict()
      for i, j in zip(header, row):
        if "Country/Territory" in i:
          codict_names[i] = j
          country_names.append(j)
      for i, j in zip(header, row):
        if column_to_read in i:
          codict[i] = j
          column.append(j)
    country_column_zip = list(zip(country_names, column))
    country_column_dicts = {i: j for i, j in country_column_zip}
    country_column.append(country_column_dicts)
    print(country_column)
    

joder()