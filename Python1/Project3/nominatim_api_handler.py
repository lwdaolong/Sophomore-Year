#Logan Wang 51603232
'''
 * Project#3 Try Not to Breathe
 * ICS 32A
 * 11/13/20
 * Handles search and reverse searching with Nominatim API
 * @author Logan Wang
'''
import urllib.request
import urllib.parse
import json
import math
import time


class NominatimAPIHandler:
    def __init__(self, query_string: str):
        self.query_str = query_string
        self.base_url = 'https://nominatim.openstreetmap.org'

    def _convert_location_query(self, query_string: str) -> str:
        """given a query_string, return a formatted string that can be used to do a search on Nominatim's API with the given
        query details"""
        query_list = query_string.split()
        real_query = ''
        for element in query_list:
            real_query += element + '+'
        real_query = real_query[:-1]
        real_query = real_query.replace(',', '%2C')
        formatted_query = f'/search?q={real_query}&format=json'
        return formatted_query

    def _convert_coords_query(self, query_string: str) -> str:
        """given a query_string, return a formatted string that can be used to do a reverse search on Nominatim's API
        with the given query latitude and longitude"""
        query_list = query_string.split()
        query_parameters = [
            ('format', 'json'), ('lat', query_list[0]), ('lon', query_list[1])
        ]
        real_query = urllib.parse.urlencode(query_parameters)
        formatted_query = f'/reverse?{real_query}'
        return formatted_query

    def return_data_from_query(self, location_str: str, type: int) -> (int, int) or str:
        """given a location string, return a piece of data with the Nominatim API
        if type ==0, then will return coordinates from a location
        if type == 1, then will return a location from coordinates"""
        time.sleep(1)
        try:
            # Makes HTTP request to Nominatim API
            url_resource = ''
            if (type == 0):
                url_resource = self._convert_location_query(location_str)
            else:
                url_resource = self._convert_coords_query(location_str)

            url = self.base_url + url_resource
            request = urllib.request.Request(url, headers={
                'Referer': 'https://www.ics.uci.edu/~thornton/ics32a/ProjectGuide/Project3/loganw1'})
            response = urllib.request.urlopen(request)

            # If Response status not correct, do not even attempt to read file
            if response.status != 200:
                print('FAILED')
                print(response.status)
                print(url)
                print('NOT 200')
            else:  # If correct response status, put url's data in a variable to convert into dictoinary later
                try:
                    urldata = response.read().decode(encoding='utf-8')
                    try:
                        # tries to load a json file, if not a json file-> failure
                        json_data = json.loads(urldata)
                        if type == 0:  # returns tuple of lat,lon
                            return (float(json_data[0]['lat']), float(json_data[0]['lon']))
                        else:  # returns string description of location
                            return json_data['display_name']
                    except:
                        print('FAILED')
                        print(response.status)
                        print(url)
                        print('FORMAT')

                finally:
                    response.close()
        except:  # If error in HTTP request, assume network error
            print('FAILED')
            print(url)
            print('NETWORK')

    def make_readable_coords(self, coordinates:str)->str:
        """Given coordinates of latitude and longitude separated by a space,
        return a string coordinate that indicated North,South,East,West directions"""
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

    def print_details(self)->None:
        """Prints a nominatim handler class' coordinates and display_name"""
        print(self.make_readable_coords(self.query_str))
        print(self.return_data_from_query(self.query_str,1))

    def readable_coords_from_location(self)->str:
        """If a nominatim handler class was constructed with a location, return its coordinates in a readable format"""
        coords = self.return_data_from_query(self.query_str,0)
        coords_str = str(coords[0]) +' ' + str(coords[1])
        return self.make_readable_coords(coords_str)