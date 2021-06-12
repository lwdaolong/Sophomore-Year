#include <string>
#pragma once

double convertlong(double londegrees, std::string lonid);

double convertlat(double latdegrees, std::string latid);

double coorddist(double lat1, double lon1, double lat2, double lon2); //assumes all values already converted to radians
