//HashNode.cpp

#include "HashNode.hpp"

HashNode::HashNode(std::string key, std::string value)
    :key{key}, value{value}, next{NULL}{

}

HashNode::HashNode(std::string key, std::string value,HashNode* n )
    :key{key}, value{value}, next{n}{

}

std::string HashNode::getKey() const{
    return key;
}

std::string HashNode::getValue() const{
    return value;
}

HashNode* HashNode::getNext() const{ // return pointer to HashNode
    if(next == NULL){
        return NULL;    
    }
    return next;
}

void HashNode::setKey(const std::string& s){
    key = s;
}

void HashNode::setValue(const std::string& s){
    value = s;
}

void HashNode::setNext( HashNode* n){
    next = n;
}

HashNode::HashNode(const HashNode& other)
    :key{other.getKey()}, value{other.getValue()}, next{other.getNext()}{

}

HashNode& HashNode::operator=(const HashNode& other){
    if(this != &other){
        key = other.getKey();
        value = other.getValue();
        next = other.getNext();
    }
    return *this;
}
