#Logan Wang 51603232
'''
 * Project#3 Try Not to Breathe
 * ICS 32A
 * 11/13/20
 * Handles search and reverse searching with Nominatim API derived json files
 * @author Logan Wang
'''
from pathlib import Path
import json


class NominatimFileHandler:

    def __init__(self, p: str):
        self.nominatim_path = Path(p)
        self.query_str = p
        # ERROR Handling if the given path does not exist, so file is missing
        if self.nominatim_path.exists() == False:
            print('FAILED')
            print(self.nominatim_path)
            print('MISSING')
        else:
            try:
                # tries to load a json file, if not a json file-> failure
                self.json_data = json.loads(self.nominatim_path.read_bytes().decode(encoding='utf-8')) #TODO sanitize path
            except:
                print('FAILED')
                print(self.nominatim_path)
                print('FORMAT')

    def return_data_from_query(self, location_str: str, type: int) -> (int, int) or str:
        """given a location string, return a piece of data with the Nominatim json file
        if type ==0, then will return coordinates from a search json file
        if type == 1, then will return a location from reverse json file"""

        try:
            if type == 0:  # returns tuple of lat,lon
                return (float(self.json_data[0]['lat']), float(self.json_data[0]['lon']))
            else:  # returns string description of location
                return self.json_data['display_name']
        except:
            print('FAILED')
            print(self.nominatim_path)
            print('FORMAT')


    def make_readable_coords(self, coordinates: str) -> str:
        """Returns readable coordinates of a Nominatim file handler (search)object"""
        coords = (float(self.json_data['lat']), float(self.json_data['lon']))
        readable_coords = ''
        if coords[0] > 0:
            readable_coords += str(abs(float(coords[0]))) + '/N '
        else:
            readable_coords += str(abs(float(coords[0]))) + '/S '
        if coords[1] > 0:
            readable_coords += str(abs(float(coords[1]))) + '/E'
        else:
            readable_coords += str(abs(float(coords[1]))) + '/W'
        return readable_coords

    def print_details(self) -> None:
        """Prints a nominatim handler class' coordinates and display_name"""
        print(self.make_readable_coords('here'))
        print(self.return_data_from_query('here', 1))

    def readable_coords_from_location(self) -> str:
        """Returns readable coordinates of a Nominatim file handler (reverse)object"""
        coords = self.return_data_from_query('here', 0)
        coords_str = str(coords[0]) + ' ' + str(coords[1])
        return self._make_coords_from_str(coords_str)

    def _make_coords_from_str(self, coordinates:str)->str:
        """Constructs a readable coordinates of a Nominatim file handler (reverse)object
        this is a helper method for readable_coords_from_location and
        should NOT be used outside of this class"""
        coords = coordinates.split()
        readable_coords=''
        if float(coords[0]) >0:
            readable_coords+= str(abs(float(coords[0]))) +'/N '
        else:
            readable_coords += str(abs(float(coords[0]))) +'/S '
        if float(coords[1]) >0:
            readable_coords+= str(abs(float(coords[1]))) +'/E'
        else:
            readable_coords += str(abs(float(coords[1]))) +'/W'
        return readable_coords