//HashNode.hpp

#ifndef HASHNODE_HPP
#define HASHNODE_HPP
#include <string>



class HashNode
{
public:
    HashNode(std::string key, std::string value); //creates a new node, where tail points to NULL
    HashNode(std::string key, std::string value,HashNode* n ); //useful constructor for when putting nodes between nodes

    HashNode(const HashNode& other);
    HashNode& operator=(const HashNode& other);

    std::string getKey() const;
    std::string getValue() const;
    HashNode* getNext() const; //returns Pointer to HashNode that must be dereferenced

    void setKey(const std::string& s);
    void setValue(const std::string& s);
    void setNext( HashNode* n);


private:
    std::string key;
    std::string value;
    HashNode* next;
};



#endif 

