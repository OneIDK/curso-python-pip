import utils
import read_csv
import charts


def run():
  data = read_csv.csv_to_dicts("world_population.csv")
  which_column = input("qué columna ? => ")
  which_continent = input("qué continente ? => ")
  data = list(filter(lambda key: key["Continent"] == which_continent, data))
  countries = list(map(lambda key: key["Country/Territory"], data))
  column = list(map(lambda key: key[which_column], data))
  charts.gen_pie_chart(countries, column)

  '''
  country = input("Type country => ").title()
  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    
    charts.generate_bar_chart(labels, values)
    #charts.gen_pie_chart(labels, values)
    #charts.gen_graph_chart(labels, values)
    '''

if __name__ == "__main__":
  run()