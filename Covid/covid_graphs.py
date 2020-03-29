import datetime
import json
import matplotlib.pyplot as plt
# import numpy as np
import os.path
import pandas as pd
import tkinter
import urllib.request
from matplotlib.pyplot import figure
from vincent.colors import brews


data_url = "https://pomber.github.io/covid19/timeseries.json"
# country_list = ['Italy', 'US', 'Spain', 'France', 'Germany', 'Poland']
country_list = ['Italy', 'US', 'Spain', 'France', 'Germany', 'United Kingdom', 'Poland']
# country_list = ['Poland', 'Italy']
pallete = brews['Paired']

today = datetime.datetime.now().strftime("%Y-%m-%d")


def import_data(url):
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode('utf-8'))
    return data


def save_data_to_file(data):
    with open(f'data_{today}.json', 'w') as json_file:
        json.dump(data, json_file)


def load_data_from_file(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data


def pull_fresh_data(url):
    file_path = f'data_{today}.json'

    if not os.path.isfile(file_path):
        data = import_data(url)
        save_data_to_file(data)
        print('Fresh data pulled from the URL')
    else:
        data = load_data_from_file(file_path)
        print('Data loaded from file')
    return pd.DataFrame(data)


def convert_date_to_number(data, date):
    for counter, value in enumerate(data['Poland']):
        if date == value['date']:
            return counter


def return_top_countries_list_by_infected(data, no_of_countries):
    counter = 0
    for country in data:
        print(data[country][-1:]['date'])
        counter += 1
    print(counter)


def plot_graphs(data_dict, list_of_countries, start_date=0, save_graph=False):
    if start_date == 0:
        start_date = convert_date_to_number(data_dict, start_date)
    color_counter = 0

    fig, ax = plt.subplots(dpi=150)

    for country in list_of_countries:
        dates_list = []
        infected_list = []

        for record in data_dict[country]:
            x_value = record["date"]
            y_value = record["confirmed"]
            dates_list.append(x_value)
            infected_list.append(y_value)

        ax.plot(dates_list,
                infected_list,
                label=f'{country}: {y_value}',
                color=pallete[color_counter])
        plt.text(len(data_dict[country]) - 0.75, y_value, y_value,
                 fontsize=8,
                 color=pallete[color_counter])

        color_counter += 1

    plt.title(f'Liczba zarażonych na dzień {today}')
    ax.legend(fontsize='x-small', framealpha=1, edgecolor='black')
    # plt.yscale('log')
    plt.xticks(rotation=90)
    ax.set_ylim(ymin=0)
    ax.set_xlim(xmin=start_date, xmax=len(data_dict[country]) - 1)
    ax.minorticks_on()
    ax.tick_params(axis='x', which='minor', bottom=False)
    ax.tick_params(axis='y', which='minor', left=False)
    ax.grid(which='major', axis='x', linestyle='-', linewidth='0.5', color='black')
    ax.grid(which='major', axis='y', linestyle='-', linewidth='0.5', color='black')
    # ax.grid(which='minor', axis='y', linestyle='-', linewidth='0.25', color='grey')
    plt.xticks(fontsize=6)
    plt.yticks(fontsize=8)

    if save_graph:
        plt.savefig(f"{os.getcwd()}\Graphs\{today}.png", facecolor='grey', dpi=250)
    plt.show()


data_frame_dictionary = pull_fresh_data(data_url)
plot_graphs(data_frame_dictionary, country_list, '2020-3-1')
# return_top_countries_list_by_infected(data_frame_dictionary, 1)