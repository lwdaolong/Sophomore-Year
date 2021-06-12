//commands.hpp

#ifndef COMMANDS_HPP
#define COMMANDS_HPP
#include <string>
#include "HashMap.hpp"



class Commands
{
public:
    Commands();

    std::string create(const std::string& user, const std::string& pass);
    std::string login(const std::string& user, const std::string& pass) const;
    std::string remove(const std::string& user);
    std::string clear();
    void invalid() const;
    
    //DEBUG COMMANDS

    std::string debugON();
    std::string debugOFF();
    int loginCount() const;
    int bucketCount() const;
    double loadFactor() const;
    int maxBucketSize() const;

    //TODO BIG THREE, COPY, DESTRUCTOR, ETC>

private:
    bool debugOn;
    HashMap hm;
};



#endif 