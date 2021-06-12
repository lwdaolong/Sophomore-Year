//HashLinkedList.hpp

#ifndef HASHLINKEDLIST_HPP
#define HASHLINKEDLIST_HPP
#include "HashNode.hpp"
#include <iostream>


class HashLinkedList
{
public:
    HashLinkedList(); //creates a new empty LinkedList, head points to null
    HashLinkedList(HashNode* head); //creates a new LinkedList, head points to HashNode argument

    HashLinkedList(const HashLinkedList& other);
    HashLinkedList& operator=(const HashLinkedList& other);

    ~HashLinkedList();

    bool isEmpty() const;
    int getSize() const;
    HashNode* getNodebyKey(const std::string& k) const;
    HashNode* getNodebyValue(const std::string& v) const;
    HashNode* getHeadNode() const;
    HashNode* getTailNode() const;
    bool contains(HashNode* n)const;
    bool containsKey(const std::string& k) const;
    bool containsKeyValuePair(const std::string& k, const std::string& v) const;

    void prependNode(HashNode* n); //TODO mayber overload with something that takes user/pass, automatically makes node, and adds it to linked list
    void appendNode(HashNode* n); //TODO mayber overload with something that takes user/pass, automatically makes node, and adds it to linked list
    void insertAfterNode(HashNode* nodetoadd,HashNode* nodereference); //TODO probably don't need for this proj
    bool removeNodebyKey(const std::string& k);
    void removeFirst();
    void removeLast();
    void clear();

    void printLL() const;
    std::string toString() const;


private:

    void deleteAllNodes();

    int size;
    HashNode* head;
    HashNode* tail;
    
    

};



#endif 