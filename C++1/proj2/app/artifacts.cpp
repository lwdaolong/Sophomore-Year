//artifacts.cpp
#include "artifacts.hpp"


artifact processAritfactInput(){
    int num;
    int totweights = 0;

    std::cin>>num;
    resolveNewLineChar();
    
    int* maxscores = new int[num];
    int* weights = new int[num];

    for(int i=0; i<num;++i){
        std::cin>>maxscores[i];
    }
    resolveNewLineChar();

    for(int i=0; i<num;++i){
        int tempweight;
        std::cin>>tempweight;
        totweights+=tempweight;
        weights[i] = tempweight;
    }
    resolveNewLineChar();

    return artifact{num,maxscores,weights,totweights};
}

void deleteArtifactStruct(artifact a){
    delete[] a.maxscores;
    delete[] a.weights;

}




