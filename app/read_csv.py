import csv

def csv_to_dicts(path):
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
  data = csv_to_dicts("./app/world_population.csv")
  Afghanistan = data[0]
  print(Afghanistan["Rank"])
  print(data[57]["Country/Territory"])
  print(data)