#include "arrayfunctionality.hpp"
#include "artifacts.hpp"
#include "studentutil.hpp"
#include "rawscoreutil.hpp"
#include "determinegrades.hpp"

int main()
{
   
    artifact a = processAritfactInput();

    artifact* aptr = &a;


    int numstudents;
    std::cin>>numstudents;
    student* s = processStudentInput(numstudents);

    int numscores;
    std::cin>>numscores;
    processRawScores(numscores,numstudents,s,aptr);

    std::cout<<"TOTAL SCORES"<<std::endl;
    for(int i=0;i<numstudents;++i){
        std::cout<<s[i].id<<" "<<s[i].name<<" "<<s[i].grade<<std::endl;
    }

    int numcutpoints;
    std::cin>>numcutpoints;
    processCutPoints(numcutpoints,numstudents,s);



    delete[] s;
    deleteArtifactStruct(a);

    return 0;
}

