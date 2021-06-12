
#include "commands.hpp"
#include <iostream>
#include <sstream>

int numInputsInString(std::string& str){
    std::stringstream s(str);  
    std::string word; 
   
    int count = 0; 
    while (s >> word) 
        count++;
         
    return count;
}

bool isValidInput(std::string s, int t){
    bool temp = true;
    if(s == "QUIT"){
        if(t == 1){
            temp = false;
        }
    }
    return temp;
}
    

int main()
{
  
    //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Commands c;
    std::string input;
    std::getline(std::cin,input); 

    std::string arr[3]; //holds array of up to 3 input
    std::stringstream s(input);  
    std::string word; 
   
    int numinputs = numInputsInString(input);

    if( numinputs<4){
        int count = 0; 
        while (s >> word){
            arr[count] = word;
            count++;
        }
    }

    while(isValidInput(arr[0],numinputs)){
        if(numinputs == 1){
            if(arr[0] == "CLEAR"){
                std::cout<<c.clear()<<std::endl;
            }else{
                c.invalid();
            }
        }else if (numinputs ==2){
            if(arr[0] == "DEBUG" && arr[1]=="ON"){
                std::cout<<c.debugON()<<std::endl;
            }else if(arr[0] == "DEBUG" && arr[1]=="OFF"){
                std::cout<<c.debugOFF()<<std::endl;
            }else if(arr[0] == "LOGIN" && arr[1]=="COUNT"){
                int temp =c.loginCount();
                if(temp > -1){
                std::cout<<temp<<std::endl;
                }
            }else if(arr[0] == "BUCKET" && arr[1]=="COUNT"){
            int temp = c.bucketCount();
            if(temp > -1){
                std::cout<<temp<<std::endl;
            }
            }else if(arr[0] == "LOAD" && arr[1]=="FACTOR"){
                double temp = c.loadFactor();
                if(temp > -1){
                    std::cout<<temp<<std::endl;
                }
            }else if(arr[0] == "REMOVE"){
                std::cout<<c.remove(arr[1])<<std::endl;
            }else{
                c.invalid();
            }
        }else if(numinputs == 3){
            if(arr[0] == "CREATE"){
                std::cout<<c.create(arr[1],arr[2])<<std::endl;
            }else if(arr[0] == "LOGIN"){
                std::cout<<c.login(arr[1],arr[2])<<std::endl;
            }else if(arr[0] == "MAX" && arr[1] == "BUCKET" && arr[2] == "SIZE"){
                int temp = c.maxBucketSize();
                if(temp > -1){
                std::cout<<temp<<std::endl;
            }
            }else{
                c.invalid();
            }

        }else{
            c.invalid();
        }


        std::getline(std::cin,input); 
        s =  std::stringstream(input);   
   
        numinputs = numInputsInString(input);

        if( numinputs<4){
        int count = 0; 
        while (s >> word){
            arr[count] = word;
            count++;
        }
    }
    }
    std::cout<<"GOODBYE"<<std::endl;

    return 0;
}


