import utils
import read_csv
import charts

def run():
    data = read_csv.csv_to_dicts('world_population.csv')
    data = list(filter(lambda key: key['Continent'] == 'South America', data))

    countries = list(map(lambda x: x['Country/Territory'], data))
    percentages = list(map(lambda x: x['World Population Percentage'], data))
    charts.gen_pie_chart(countries, percentages)

    country = input("Type country => ")

    result = utils.population_by_country(data, country)

    if len(result) > 0:
        country_dict = result[0]
        labels, values = utils.get_population(country_dict)
        charts.generate_bar_chart(country, labels, values)


if __name__ == "__main__":
    run()