//determinegrades.cpp
#include "determinegrades.hpp"

std::string lettergrades[5] = {"A","B","C","D","F"};

std::string getLetterGrade(double cutpoints[],double studentscore){
    for(int i=0;i< 4; i++){
        if(studentscore>= cutpoints[i]){
            return lettergrades[i];
        }
    }
    return lettergrades[4];
}

std::string determineGradeChar(double cutpoints[],char gradeoption,double studentscore){
    std::string lettergrade= getLetterGrade(cutpoints,studentscore);
    if(gradeoption == 'G'){
        return lettergrade;
    }else{ //naive, but assumes only other option is 'P'
        if(lettergrade == "D" || lettergrade == "F"){
            return "NP";
        }else{
            return "P";
        }
    }
}

void printStudentwGrades(double cutpoints[],int numstudents, student *s){
    for(int i=0;i<numstudents;++i){
        std::cout<<s[i].id<<" "<<s[i].name<<" "<<determineGradeChar(cutpoints,s[i].gradeoption,s[i].grade)<<std::endl;
    }
}

void makeCutPointArray(double (&arr)[4]){ //fills array passed by reference with cut points values taken by input
    for(int i=0; i < 4; i++){
        std::cin>>arr[i];
    }
    resolveNewLineChar();   
}

void evaluateCutPoint(int numstudents, student *s){ 
    double cutpointarr[4];
    makeCutPointArray(cutpointarr);
    //printarraystatic(cutpointarr,4); //TODO REMOVE DEBUG PRINT

    printStudentwGrades(cutpointarr, numstudents, s);
}

void processCutPoints(int numcutpoints, int numstudents, student *s){
    resolveNewLineChar();

    for(int i =0; i < numcutpoints; ++i){
        std::cout<<"CUTPOINT SET "<<i+1<<std::endl;
        evaluateCutPoint( numstudents, s);
    }
}