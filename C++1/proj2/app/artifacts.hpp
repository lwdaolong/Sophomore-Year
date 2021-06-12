//artifacts.hpp

#ifndef ARTIFACTS_HPP
#define ARTIFACTS_HPP

#include <iostream>
#include "stringhelper.hpp"

struct artifact{
    int num;
    int* maxscores; //array pointer
    int* weights; //array pointer
    int totweight;
    
};

//insantiates and returns a struct based off of input
artifact processAritfactInput();

//used before actual deletion of struct, deletes dynamically allocated arrays from within
void deleteArtifactStruct(artifact a);


#endif