//rawscoreutil.cpp
#include "rawscoreutil.hpp"

double processRawScore(artifact *a){
    double sum=0;
    for(int i=0; i < a->num;++i){
        double temp;
        std::cin>>temp;
        double score = temp/(a->maxscores[i]);
        double weightedscore = score * (a->weights[i]);
        sum+= weightedscore;
    }
    return sum;
}

void attachStudentScore(int numstudents, student *s, artifact *a){
    int id;
    std::cin>>id;
    for(int i=0; i< numstudents; ++i){
        if(id==s[i].id){
            s[i].grade = processRawScore(a);
        }
    }
    resolveNewLineChar();
}

void processRawScores(int numscores, int numstudents, student *s, artifact *a){
    resolveNewLineChar();

    for(int i =0; i < numscores; ++i){
        attachStudentScore( numstudents, s, a);
    }
}