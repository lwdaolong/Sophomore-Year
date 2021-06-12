//arrayfunctionality.cpp
#include "arrayfunctionality.hpp"

int sumarraystatic(int arr[], int size){
    int sum = 0;
    for(int i =0; i< size;++i){
        sum += arr[i];
    }
    return sum;
}


int sumarraydynamic(int* arr, int size){
    int sum = 0;
    for(int i =0; i< size;++i){
        sum += arr[i];
    }
    return sum;
}

void printarraystatic(int arr[], int size){
    for(int i =0; i< size;++i){
        std::cout<<arr[i]<<std::endl;
    }
}

void printarraystatic(double arr[], int size){
    for(int i =0; i< size;++i){
        std::cout<<arr[i]<<std::endl;
    }
}

void printarraydynamic(int* arr, int size){
    for(int i =0; i< size;++i){
        std::cout<<arr[i]<<std::endl;
    }
}
