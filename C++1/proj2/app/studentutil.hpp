//studentutil.hpp
#ifndef STUDENTUTIL_HPP
#define STUDENTUTIL_HPP

#include <iostream>
#include <string>
#include "stringhelper.hpp"

struct student{
    int id;
    char gradeoption;
    std::string name;
    double grade;
};

//insantiates and returns a struct based off of input
//TODO make take input of size, from std::cin, to keep track of max size of students
student* processStudentInput(int numstudents);



#endif