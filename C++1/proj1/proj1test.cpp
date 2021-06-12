// proj1test.cpp : This file contains the 'main' function. Program execution begins and ends there.
//
#include "gpslogic.h"
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
    
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
