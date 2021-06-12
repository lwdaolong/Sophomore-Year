//HashLinkedList.cpp
#include "HashLinkedList.hpp"
HashLinkedList::HashLinkedList()
    :size{0}, head{NULL}, tail{NULL}{

}

HashLinkedList::HashLinkedList(HashNode* head)
    :size{1}, head{head}, tail{head}{

}

bool HashLinkedList::isEmpty() const{
    if(size == 0){
        return true;
    }
    return false;
}

int HashLinkedList::getSize() const{
    return size;
}

HashNode* HashLinkedList::getNodebyKey(const std::string& k) const{
    HashNode* currpointer = head;
    while(currpointer != NULL){
        HashNode temp = *currpointer;
        if(temp.getKey() == k){
            return currpointer;
        }
        currpointer = temp.getNext();
    }
    return NULL;
}

HashNode* HashLinkedList::getNodebyValue(const std::string& v) const{
    HashNode* currpointer = head;
    while(currpointer != NULL){
        HashNode temp = *currpointer;
        if(temp.getValue() == v){
            return currpointer;
        }
        currpointer = temp.getNext();
    }
    return NULL;
}

bool HashLinkedList::contains(HashNode* n) const{
    HashNode* currpointer = head;
    while(currpointer != NULL){
        HashNode temp = *currpointer;
        if(currpointer == n){
            return true;
        }
        currpointer = temp.getNext();
    }
    return false;
}

bool HashLinkedList::containsKey(const std::string& k) const{
    HashNode* currpointer = head;
    while(currpointer != NULL){
        HashNode temp = *currpointer;
        if(temp.getKey() == k){
            return true;
        }
        currpointer = temp.getNext();
    }
    return false;
}

bool HashLinkedList::containsKeyValuePair(const std::string& k, const std::string& v) const{
    HashNode* currpointer = head;
    while(currpointer != NULL){
        HashNode temp = *currpointer;
        if(temp.getValue() == v && temp.getKey() == k){
            return true;
        }
        currpointer = temp.getNext();
    }
    return false;
}

void HashLinkedList::prependNode(HashNode* n){
    //HashNode nodeptr = *n;
    if(isEmpty()){
        head = n;
        tail = n;
    }else{
        n->setNext(head);
        head = n;
    }
    size++;
}

void HashLinkedList::appendNode(HashNode* n){
    //HashNode nodeptr = *n;
    if(isEmpty()){
        head = n;
        tail = n;
    }else{
        tail->setNext(n);
        tail = n;
    }
    size++;
}

bool HashLinkedList::removeNodebyKey(const std::string& k){
    HashNode* prevpointer = NULL;
    HashNode* currpointer = head;
    while(currpointer != NULL){
        HashNode temp = *currpointer;
        if(temp.getKey() == k){
            if(currpointer == head){
                removeFirst();
            }else if(currpointer == tail){
                removeLast();
            }else{
                prevpointer->setNext(currpointer->getNext());
                size--;
                delete currpointer;
            }
            return true;
        }
        prevpointer = currpointer;
        currpointer = temp.getNext();
    }
    return false;
}

void HashLinkedList::removeFirst(){
    if(head == tail && size ==1){
        HashNode* temp = head;
        head = NULL;
        tail = NULL;
        size--;
        delete temp;
    }else if(!isEmpty()){
        HashNode* temp = head;
        head = head->getNext();
        size--;
        delete temp;
    }
}

void HashLinkedList::removeLast(){
    if(isEmpty()){
        //do nothing
    }else if(head == tail){
        HashNode* temp = head;
        head = NULL;
        tail = NULL;
        size--;
        delete temp;
    }else{
        HashNode* prevpointer = NULL;
        HashNode* currpointer = head;
        while(currpointer != tail){
            HashNode temp = *currpointer;
            prevpointer = currpointer;
            currpointer = temp.getNext();
        }
        prevpointer->setNext(NULL);
        size--;
        tail = prevpointer;
        delete currpointer;
    }
}

void HashLinkedList::clear(){
    deleteAllNodes();
    size =0;
    head = NULL;
    tail = NULL;
}

HashNode* HashLinkedList::getHeadNode() const{
    return head;
}

HashNode* HashLinkedList::getTailNode() const{
    return tail;
}

void HashLinkedList::printLL() const{
    HashNode* currpointer = head;
    while(currpointer != NULL){
        HashNode temp = *currpointer;
        
        std::cout<<"user: "<<temp.getKey()<<" pass: "<< temp.getValue()<<std::endl;

        currpointer = temp.getNext();
    }
}

std::string HashLinkedList::toString() const{
    std::string s;
    HashNode* currpointer = head;
    while(currpointer != NULL){
        HashNode temp = *currpointer;
        s+= "user: ";
        s+= temp.getKey();
        s += " pass: ";
        s+= temp.getValue();
        currpointer = temp.getNext();
    }
    return s;
}

HashLinkedList::~HashLinkedList(){
    deleteAllNodes();
}

void HashLinkedList::deleteAllNodes(){
HashNode* currpointer = head;
    while(currpointer != NULL){
        HashNode* next = (*currpointer).getNext();

        delete currpointer;

        currpointer = next;
    }
    
}

HashLinkedList::HashLinkedList(const HashLinkedList& other)
    :size{other.getSize()}, head{NULL}, tail{NULL}{
    if(size == 0){

    }else{
        head = new HashNode(*(other.getHeadNode()));
        HashNode* currpointer = head;
        HashNode* othercurrpointer = other.getHeadNode();
        while(othercurrpointer->getNext() != NULL){
            currpointer->setNext(new HashNode(*(othercurrpointer->getNext())));

            
            
            othercurrpointer = othercurrpointer->getNext();
            currpointer = currpointer->getNext();
        }
        tail = currpointer;
    }
}

HashLinkedList& HashLinkedList::operator=(const HashLinkedList& other){
    if(this != &other){
        if(other.getSize() == 0){
            deleteAllNodes();
            size =0;
            head = NULL;
            tail = NULL;
        }else{
            deleteAllNodes();
            size = other.getSize();
            head = new HashNode(*(other.getHeadNode()));
            HashNode* currpointer = head;
            HashNode* othercurrpointer = other.getHeadNode();
            while(othercurrpointer->getNext() != NULL){
                currpointer->setNext(new HashNode(*(othercurrpointer->getNext())));

                
                
                othercurrpointer = othercurrpointer->getNext();
                currpointer = currpointer->getNext();
            }
            tail = currpointer;
        }
    }
    return *this;


}
