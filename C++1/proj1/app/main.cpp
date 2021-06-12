#include "gpslogic.hpp"
#include <string>
#include <iostream>

int main()
{
	int numlocations = 0;
	std::string startlocation;
	std::string startlongid;
	std::string startlatid;
	double startlong;
	double startlat;

	double startradlat;
	double startradlon;

	std::string temp;

	double mindist = 0;
	double maxdist = 0;

	std::string minlocation;
	std::string minlongid;
	std::string minlatid;
	double minlong;
	double minlat;
	std::string maxlocation;
	double maxlong;
	double maxlat;
	std::string maxlongid;
	std::string maxlatid;


	std::string currlocation;
	double currlong;
	double currlat;
	std::string currlongid;
	std::string currlatid;




	std::cin >> startlat >> startlatid >> startlong >> startlongid;
	std::getline(std::cin, startlocation);
	std::cin >> numlocations;
	std::getline(std::cin, temp);//dumps newline character

	startradlat = convertlat(startlat,startlatid);
	startradlon = convertlong(startlong,startlongid);

	for (int i = 0; i < numlocations; i++){

		std::cin >> currlat >> currlatid >> currlong >> currlongid;
		std::getline(std::cin, currlocation);
		double radlat = convertlat(currlat, currlatid);
		double radlon = convertlong(currlong, currlongid);
		double dist = coorddist(startradlat, startradlon, radlat, radlon);

		if (i==0) {//first run of loop
			mindist = dist;
			maxdist = dist;

			minlat = currlat;
			minlatid = currlatid;
			minlong = currlong;
			minlongid = currlongid;
			minlocation = currlocation;

			maxlat = currlat;
			maxlatid = currlatid;
			maxlong = currlong;
			maxlongid = currlongid;
			maxlocation = currlocation;
		}
		else {
			if(dist < mindist){
				mindist = dist;
				minlat = currlat;
				minlatid = currlatid;
				minlong = currlong;
				minlongid = currlongid;
				minlocation = currlocation;
			}
			if (dist > maxdist) {
				maxdist = dist;
				maxlat = currlat;
				maxlatid = currlatid;
				maxlong = currlong;
				maxlongid = currlongid;
				maxlocation = currlocation;
			}
		}
	}
	//checks against curr min and max dist. locations and updates, loop extends as long as user originally defines

	std::cout << "Start Location: " << startlat << startlatid << " " << startlong << startlongid << " (" << startlocation.substr(1) << ")" << std::endl;
	std::cout << "Closest Location: " << minlat << minlatid << " " << minlong << minlongid << " (" << minlocation.substr(1) << ") (" << mindist<<" miles)"<<std::endl;
	std::cout << "Farthest Location: " << maxlat << maxlatid << " " << maxlong << maxlongid << " (" << maxlocation.substr(1) << ") (" << maxdist<<" miles)"<<std::endl;
    
    return 0;
}

