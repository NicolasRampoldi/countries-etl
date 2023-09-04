import os
import pandas as pd

def generate_excel(countries):
    column_names = ['id', 'name', 'capital', 'currency', 'continent', 'language', 'population', 'flag']

    country_data = [(country.id, country.name, country.capital, country.currency, country.continent, country.language, country.population, country.flag) for country in countries]

    df = pd.DataFrame(country_data, columns=column_names)


    assets_folder = "assets"
    if not os.path.exists(assets_folder):
        os.makedirs(assets_folder)

    excel_file = os.path.join(assets_folder, "countries_data.xlsx")
    writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')
    df.to_excel(writer, sheet_name="Paises", index=False)
    workbook = writer.book

    metrics_sheet = workbook.add_worksheet("Metricas")

    population_by_continent = df.groupby('continent')['population'].sum()

    chart = workbook.add_chart({'type': 'bar'})
    chart.add_series({'name': 'Población por Continente',
                      'categories': 'Metricas!$A$2:$A$' + str(len(population_by_continent) + 1),
                      'values': 'Metricas!$B$2:$B$' + str(len(population_by_continent) + 1),
                      })

    chart.set_title({'name': 'Población por Continente'})

    metrics_sheet.insert_chart('D2', chart)

    metrics_sheet.write_column('A2', population_by_continent.index)
    metrics_sheet.write_column('B2', population_by_continent.values)

    writer.close()

    return excel_file