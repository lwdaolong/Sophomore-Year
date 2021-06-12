#Logan Wang 51603232
'''
 * Project#3 Try Not to Breathe
 * ICS 32A
 * 11/13/20
 * Provides main process of project3, using Paths, the Purple Air API, and the Nominatim API
 * @author Logan Wang
'''
"""
Main processing script
#Handles logic for input, output, and organizing data inputted from classes
#like purpleair_api_handler, purpleair_file_handler, nominatim_api_handler, and nominatim_file_handler

"""
import purpleair_api_handler
import purpleair_file_handler
import nominatim_api_handler
import nominatim_file_handler


def run():
    """main process"""
    center_class = center_method(input())
    center = center_class.return_data_from_query(center_class.query_str, 0)
    range1 = range_input(input())
    threshold = threshold_input(input())
    max1 = max_input(input())
    purpleair_class = aqi_method(input(), center, range1, threshold, max1)
    highest_valid_aqi_vals = purpleair_class.get_n_AQIs_above_threshold_in_range()
    highest_aqi_coords_in_range = purpleair_class.get_n_coords_above_threshold_in_range()
    nominatim_class_objs = reverse_method(input(), highest_aqi_coords_in_range)
    print('CENTER '+ center_class.readable_coords_from_location())
    for i in range(len(nominatim_class_objs)):
        print(f'AQI {highest_valid_aqi_vals[i]}')
        nominatim_class_objs[i].print_details()


def max_input(user_input: str) -> int:
    if 'MAX' in user_input:
        return int(user_input[4:])
    else:
        print('ERROR: invalid input')


def threshold_input(user_input: str) -> int:
    if 'THRESHOLD' in user_input:
        return int(user_input[10:])
    else:
        print('ERROR: invalid input')


def range_input(user_input: str) -> int:
    if 'RANGE' in user_input:
        return int(user_input[6:])
    else:
        print('ERROR: invalid input')


def center_method(user_input: str) -> 'nominatim_class_obj':
    """Given an input, determine whether to use Noominatim API or path system to find center coordinate"""
    if 'CENTER NOMINATIM' in user_input:
        return nominatim_api_handler.NominatimAPIHandler(user_input[17:].strip())
    elif 'CENTER FILE' in user_input:
        return nominatim_file_handler.NominatimFileHandler(user_input[11:].strip())
    else:
        print('ERROR: invalid input')


def center_nominatim(user_input: str) -> 'nominatim_class_obj':
    """Uses nominatim to return a coordinate tuple based on the location description"""
    n = nominatim_api_handler.NominatimAPIHandler(user_input)
    return n.return_data_from_query(user_input, 0)


def center_file(user_input: str)->'nominatim_class_obj':
    """Uses nominatim search.json file to return a coordinate tuple based on the location description"""
    n = nominatim_file_handler.NominatimFileHandler(user_input)
    return n.return_data_from_query(user_input, 0)


def aqi_method(user_input: str, center_coords: (float, float), range: int,
               threshold: int, max: int) -> 'purpleair interfaced class':
    """Given a type of aqi processing 'purpleair' or 'file', will return a purpleair class object"""
    if 'AQI PURPLEAIR' in user_input:
        return aqi_purpleair(center_coords, range, threshold, max)
    elif 'AQI FILE' in user_input:
        return aqi_path(user_input[9:].strip(), center_coords, range, threshold, max)
    else:
        print('ERROR: invalid input')


def aqi_purpleair(coords: (float, float), range: int, threshold: int,
                  num_wanted: int) -> purpleair_api_handler.PurpleAirAPIHandler:
    return purpleair_api_handler.PurpleAirAPIHandler(coords, range, threshold, num_wanted)


def aqi_path(p: str, coords: (float, float), range: int, threshold: int,
             num_wanted: int) -> purpleair_file_handler.PurpleAirFileHandler:
    return purpleair_file_handler.PurpleAirFileHandler(p, coords, range, threshold, num_wanted)


def reverse_method(user_input: str, coords: ['coords']) -> ['Nominatim class obj']:
    """Given a valid input, return a a list of Nominatim class objects"""
    if 'REVERSE NOMINATIM' in user_input:
        return reverse_nominatim(coords)
    elif 'REVERSE FILES' in user_input:
        return reverse_files(user_input[13:].strip())
    else:
        print('ERROR: invalid input')


def reverse_nominatim(coords: ['coords']) -> ['Nominatim class obj']:
    """Constructs list of NominatimeAPIHandler class objects using the Nominatim API to search the given coordinates"""
    nominatim_obj_list = []
    for coord in coords:
        nominatim_obj_list.append(nominatim_api_handler.NominatimAPIHandler(coord))
    return nominatim_obj_list


def reverse_files(user_input: str) -> ['Nominatim class obj']:
    """Constructs list of NominatimFileHandler objects based on a list of paths, each path is aligned to a
    NominatimFileHandler class object"""
    path_list = user_input.split()
    nominatim_obj_list = []
    for path in path_list:
        nominatim_obj_list.append(nominatim_file_handler.NominatimFileHandler(path))
    return nominatim_obj_list


if __name__ == '__main__':
    run()
