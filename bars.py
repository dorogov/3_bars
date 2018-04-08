import json
from geopy.distance import vincenty
import argparse
filepath = '/Users/admin/Desktop/bars.json'

def load_data(filepath):
    with open(filepath) as file:
        return json.load(file)


def bars_list(json_file):
    return json_file['features']


def get_biggest_bar(bars_list):
    biggest_bar = max(
        bars_info,
        key=lambda bar: bar['properties']['Attributes']['SeatsCount']
    )
    return biggest_bar


def get_smallest_bar(bars_list):
    biggest_bar = min(
        bars_info,
        key=lambda bar: bar['properties']['Attributes']['SeatsCount']
    )
    return biggest_bar


def input_longitude_latitude():
    longitude = float(input('inter you longitude: '))
    latitude = float(input('inter you latitude: '))
    return longitude, latitude


def get_closest_bar(bars_list, longitude, latitude):
    list_distance = []
    for num_bar in range(len(bars_info)):
        list_distance.append(
            (
                num_bar,
                vincenty(
                    (longitude, latitude),
                    bars_info[num_bar]["geometry"]["coordinates"]
                ).meters
            )
        )
    min_dist_bar_number = min(list_distance, key=lambda dist: dist[1])[0]
    return bars_info[min_dist_bar_number]


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f',
        '--file',
        required=True,
        metavar='FILE',
        help='way to file .json'
    )
    return parser.parse_args()


def get_bar_name(bar):
    return bar['properties']['Attributes']['Name']


if __name__ == '__main__':
    bars_info = load_data(get_args().file)
    bars_list = bars_list(bars_info)
    try:
        object_geoposition = input_longitude_latitude()
    except ValueError:
        exit('needed to enter two float values')
    print(
        'The biggest bar is: {}\n'
        'The smallest bar is: {}\n'
        'The closest bar is: {}\n'.format(
            get_bar_name(get_biggest_bar(bars_list)),
            get_bar_name(get_smallest_bar(bars_list)),
            get_bar_name(get_closest_bar(bars_list, object_geoposition[0], object_geoposition[1]))
        )

    )
