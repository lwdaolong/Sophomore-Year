//commands.cpp
#include "commands.hpp"

Commands::Commands()
    :debugOn{false}, hm{HashMap()}{

}

std::string Commands::create(const std::string& user, const std::string& pass){
    if(hm.addBool(user,pass)){
        return "CREATED";
    }else{
        return "EXISTS";
    }
}

std::string Commands::login(const std::string& user, const std::string& pass) const{
    if(hm.containsKV(user,pass)){
        return "SUCCEEDED";
    }else{
        return "FAILED";
    }
}

std::string Commands::remove(const std::string& user){
    if(hm.remove(user)){
        return "REMOVED";
    }else{
        return "NONEXISTENT";
    }
}

std::string Commands::clear(){
    hm.clear();
    return "CLEARED";
}

void Commands::invalid() const{
    std::cout<< "INVALID"<<std::endl;
}

//DEBUG COMMANDS

std::string Commands::debugON() {
    if(debugOn){
        return "ON ALREADY";
    }else{
        debugOn = true;
        return "ON NOW";
    }
}

std::string Commands::debugOFF(){
    if(debugOn == false){
        return "OFF ALREADY";
    }else{
        debugOn = false;
        return "OFF NOW";
    }
}

int Commands::loginCount() const{
    if(debugOn){
        return hm.size();
    }else{
        invalid();
        return -1;
    }
}

int Commands::bucketCount() const{
    if(debugOn){
        return hm.bucketCount();
    }else{
        invalid();
        return -1;
    }  
}

double Commands::loadFactor() const{
    if(debugOn){
        return hm.loadFactor();
    }else{
        invalid();
        return -1;
    }
}

int Commands::maxBucketSize() const{
    if(debugOn){
        return hm.maxBucketSize();
    }else{
        invalid();
        return -1;
    }
}