# Logan Wang 51603232
'''
 * Project#3 Try Not to Breathe
 * ICS 32A
 * 11/13/20
 * Handles scraping data from a PurpleAir API derived json file
 * @author Logan Wang
'''
from pathlib import Path
import json
import math


class PurpleAirFileHandler:

    def __init__(self, p: str, coords: (float, float), range: int, threshold: int, num_wanted: int):
        purpleair_path = Path(p)
        # ERROR Handling if the given path does not exist, so file is missing
        if purpleair_path.exists() == False:
            print('FAILED')
            print(purpleair_path)
            print('MISSING')
        else:
            # if file exists, proceed assigning attributes
            self.aqi = [
                [0, 0],
                [12.1, 50],
                [35.5, 100],
                [55.5, 150],
                [150.5, 200],
                [250.5, 300],
                [350.5, 400],
                [500.5, 500]
            ]

            self.coords = coords
            self.range = range
            self.threshold = threshold
            self.num_wanted = num_wanted
            try:
                # tries to load a json file, if not a json file-> failure
                self.json_data = json.loads(purpleair_path.read_bytes().decode(encoding='utf-8'))  # TODO sanitize path
                self.max_count = self.json_data['count']
            except:
                print('FAILED')
                print(purpleair_path)
                print('FORMAT')

    def locations_last_hour(self, json_data: []) -> ['locations']:
        """Given a list of location data from a purpleair json file, return a list of locations that have been
                updated within the last hour"""
        valid_locations = []
        for data in json_data:
            try:
                if data[4] < 3600:  # 1 hour in seconds
                    valid_locations.append(data)
            except:
                pass  # Reached a null reference exception, ignores that piece of data
        return valid_locations

    def locations_outdoors(self, json_data: []) -> ['locations']:
        """Given a list of location data from purpleair json file, return a list of locations that
               have outdoor sensors"""
        valid_locations = []
        for data in json_data:
            try:
                if data[25] == 0:
                    valid_locations.append(data)
            except:
                pass  # Reached a null reference exception, ignores that piece of data
        return valid_locations

    def locations_in_range(self, coord: (float, float), json_data: [], range: int) -> ['locations']:
        """Given a list of location data from purpleair json file, return locations that are in range
                Params: one tuple coordinate, list of location data, and a decided range"""
        valid_locations = []
        for data in json_data:
            try:
                if (self.distance_between_coords(coord, (data[27], data[28])) <= range):
                    valid_locations.append(data)
            except:
                pass  # Reached a null reference exception, ignores that piece of data
        return valid_locations

    def distance_between_coords(self, coord1: (float, float), coord2: (float, float)) -> float:
        """given two coordinates that are tuples of floates, find the distance between them
        assuming the coordinates are longitude and latitude values on Earth"""
        dlat = math.radians(coord2[0]) - math.radians(coord1[0])
        dlon = math.radians(coord2[1]) - math.radians(coord1[1])
        alat = (math.radians(coord2[0]) + math.radians(coord1[0])) / 2
        r = 3958.8  # Earth radius constant
        x = dlon * math.cos(alat)
        return math.sqrt(math.pow(x, 2) + math.pow(dlat, 2)) * r

    def locations_above_threshold(self, json_data: [], aqi_thresh: int) -> ['locations']:
        """Given a list of location data from purpleair json file, return locations that are above
                the desired AQI threshold"""
        valid_locations = []
        for data in json_data:
            try:
                if self.calc_AQI(data[1], self.aqi) >= aqi_thresh:
                    valid_locations.append(data)
            except:
                pass  # Reached a null reference exception, ignores that piece of data
        return valid_locations

    def calc_AQI(self, ppm: float, formula: [[float, float]]) -> int:
        """Calculates the AQI based on concentration of 2.5 ppm at a given location
                based on the purpleair data json file."""
        index = 0
        aqi = 0
        c = 0
        for i in range(len(formula)):
            if ppm >= formula[i][0]:
                index = i
        aqi += formula[index][1] + 1
        if (index < len(formula) - 1):
            d = ppm - formula[index][0]
            t = round(d / (formula[index + 1][0] - formula[index][0]), 2)
            c = t * (formula[index + 1][1] - formula[index][1] + 1)

        return round(aqi + c)

    def highest_n_AQI(self, json_data: [], n: int):
        """Returns the highest 'n' AQI valued locations from a given list of locations from purpleair data json file"""
        try:
            valid_locations = []
            sorted_locations_by_aqi = sorted(json_data, key=lambda x: x[1],
                                             reverse=True)  # aqi sorted by descending order
            for data in range(n):
                valid_locations.append(sorted_locations_by_aqi[data])
        except:
            pass
        return valid_locations

    def return_location_coords(self, json_data: []) -> [str]:
        """Given a list of location data from purpleair json file, return a list of location
                coordinates in the form of strings"""
        valid_coords = []
        for data in json_data:
            valid_coords.append((str(data[27]) + ' ' + str(data[28])))

        return valid_coords

    def get_n_coords_above_threshold_in_range(self):
        """From a constructed purpleair handler class, returns a list of locations (ordered by descending
                AQI values) that has:
                been updated in the last hour
                has an outdoor sensor
                is in range of the given center coord
                has an AQI above defined threshold
                and contains at most num_wanted locations"""
        try:
            valid_locations = self.locations_last_hour(self.json_data['data'])
            valid_locations = self.locations_outdoors(valid_locations)
            valid_locations = self.locations_in_range(self.coords, valid_locations, self.range)
            valid_locations = self.locations_above_threshold(valid_locations, self.threshold)
            top_n_locations = self.highest_n_AQI(valid_locations, self.num_wanted)
            return self.return_location_coords(top_n_locations)
        except:
            pass

    def return_AQIvals(self, json_data: []) -> [int]:
        """Given a list of location data from purpleair json file, return a list of AQI's in descending order"""
        valid_coords = []
        for data in json_data:
            valid_coords.append(self.calc_AQI(data[1], self.aqi))
        return valid_coords

    def get_n_AQIs_above_threshold_in_range(self):
        """From a constructed purpleair handler class, returns a list of descending AQI's that has:
                       been updated in the last hour
                       has an outdoor sensor
                       is in range of the given center coord
                       has an AQI above defined threshold
                       and contains at most num_wanted AQI's"""
        try:
            valid_locations = self.locations_last_hour(self.json_data['data'])
            valid_locations = self.locations_outdoors(valid_locations)
            valid_locations = self.locations_in_range(self.coords, valid_locations, self.range)
            valid_locations = self.locations_above_threshold(valid_locations, self.threshold)
            top_n_locations = self.highest_n_AQI(valid_locations, self.num_wanted)
            return self.return_AQIvals(top_n_locations)
        except:
            pass
