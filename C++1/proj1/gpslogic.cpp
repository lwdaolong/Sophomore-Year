#include <string>
#include <cmath>

double radianconversionconstant = std::acos(-1) / 180;

double convertlong(double londegrees, std::string lonid) { 
	double newlongradians = londegrees * radianconversionconstant;
	if (lonid == "/E") {
		return newlongradians;
	}
	else {
		return -newlongradians;
	}
}

double convertlat(double latdegrees, std::string latid) {
	double newlatradians = latdegrees * radianconversionconstant;
	if (latid == "/N") {
		return newlatradians;
	}
	else {
		return -newlatradians;
	}
}

double coorddist(double lat1, double lon1, double lat2, double lon2) { //assumes all values already converted to radians
	double dlat = lat2 - lat1;
	double dlon = lon2 - lon1;
	double r = 3959.9; // Earth radius constant

	double a = std::sin(dlat / 2)* std::sin(dlat / 2)+std::cos(lat1)*std::cos(lat2)* std::sin(dlon / 2) * std::sin(dlon / 2);
	double c = 2 * std::atan(std::sqrt(a)/ std::sqrt(1 - a));



	return r * c;
}
