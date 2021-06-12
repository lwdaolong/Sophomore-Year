//studentutil.cpp
#include "studentutil.hpp"


student processIndividualStudent(){
    int id;
    char gradeoption;
    std::string name;

    std::cin>>id>>gradeoption;
    std::getline(std::cin,name);
    return student{id,gradeoption,name.substr(1),0};
}

student* processStudentInput(int numstudents){
    resolveNewLineChar();

    student* arr = new student[numstudents];

    for(int i =0; i < numstudents; ++i){
        arr[i] = processIndividualStudent();
    }
    return arr;
}

