//HashMap.cpp
#include "HashMap.hpp"


unsigned int defaultHashFunction(const std::string& s){ //kinda bad but does the job
    int sum =0;
    for (int k =0; k < s.length(); k++){
        sum+= int(s[k]);
    }
    return sum;
}

void fillHashEmptyLL(unsigned int bucketcount, HashLinkedList* l){
    for(int i =0; i < bucketcount; i++){
        l[i] = HashLinkedList(); //places empty LL's
    }
}

void HashMap::resize(){ 
    if(loadFactor() > MAX_LOAD_FACTOR){
        //prepares new array of linked lists
        unsigned int bucketsizenew = (2*bucketcount)+1;
        HashLinkedList* linkedlistnew = new HashLinkedList[bucketsizenew];
        fillHashEmptyLL(bucketsizenew, linkedlistnew);

        unsigned int oldbucketsize = bucketcount;

        currsize = 0;
        bucketcount = bucketsizenew;

        HashLinkedList* linkedlistold = l;
        l = linkedlistnew;

        for(int i =0; i < oldbucketsize; i++){
            HashNode* currpointer = linkedlistold[i].getHeadNode();
            while(currpointer != NULL){
                HashNode temp = *currpointer;
        
                add(temp.getKey(),temp.getValue());

                currpointer = temp.getNext();
            }
        }
        delete[] linkedlistold;
    }
    //else do nothing
}


HashMap::HashMap()
:currsize{0}, bucketcount{INITIAL_BUCKET_COUNT}, l{new HashLinkedList[INITIAL_BUCKET_COUNT]}, hashFunction{defaultHashFunction}{ 
    fillHashEmptyLL(bucketcount,l);
}

HashMap::HashMap(HashFunction hashFunction)
:currsize{0}, bucketcount{INITIAL_BUCKET_COUNT}, l{new HashLinkedList[INITIAL_BUCKET_COUNT]}, hashFunction{hashFunction}{
    fillHashEmptyLL(bucketcount,l);
}

void HashMap::add(const std::string& key, const std::string& value){
    int hashindex = hashFunction(key)%bucketcount;
    if(l[hashindex].containsKey(key)){
        //do nothing, already exists
    }else{
        HashNode* temp = new HashNode(key,value);
        l[hashindex].appendNode(temp);
        currsize++; 
        resize();  
    }
}

bool HashMap::addBool(const std::string& key, const std::string& value){
    int hashindex = hashFunction(key)%bucketcount;
    if(l[hashindex].containsKey(key)){
        return false;
    }else{
        HashNode* temp = new HashNode(key,value);
        l[hashindex].appendNode(temp);
        currsize++; 
        resize();  
        return true;
    }
}

bool HashMap::remove(const std::string& key){
    int hashindex = hashFunction(key)%bucketcount;
    if(l[hashindex].containsKey(key)){
        l[hashindex].removeNodebyKey(key);
        currsize--;
        return true;
    }else{
        return false;
    }
}

bool HashMap::contains(const std::string& key) const{
    int hashindex = hashFunction(key)%bucketcount;
    if(l[hashindex].containsKey(key)){
        return true;
    }else{
        return false;
    }
}

bool HashMap::containsKV(const std::string& key, const std::string& value) const{
    int hashindex = hashFunction(key)%bucketcount;
    if(l[hashindex].containsKeyValuePair(key,value)){
        return true;
    }else{
        return false;
    }
}

std::string HashMap::value(const std::string& key) const{
    int hashindex = hashFunction(key)%bucketcount;
    if(l[hashindex].containsKey(key)){
        return l[hashindex].getNodebyKey(key)->getValue();
    }else{
        return "";
    }
}

unsigned int HashMap::size() const{
    return currsize;
}

unsigned int HashMap::bucketCount() const{
    return bucketcount;
}

double HashMap::loadFactor() const{
    return double(currsize)/double(bucketcount);
}

unsigned int HashMap::maxBucketSize() const{
    int max = l->getSize();
    for(int i =1; i< bucketcount;++i){ //skips first index
        int tempsize = l[i].getSize();
        if(tempsize > max){
            max = tempsize;
        }
    }
    return max;
}


HashMap::~HashMap(){
    currsize =0; //just in case?
    bucketcount =0;
    delete[] l;
}


void HashMap::clear(){ 
    for(int i=0; i <bucketcount;++i){
        l[i].clear();
    }
    currsize =0;
}

void HashMap::printHM(){
    for(int i =0; i < bucketcount; i++){
        std::cout<<"list "<<i<<": "; //places empty LL's
        l[i].printLL();
        std::cout<<"end"<<std::endl;
        
    }
}

std::string HashMap::toString() const{
    std::string s;

    for(int i =0; i < bucketcount; i++){
        s+= "list ";
        s+= i;
        s+= ": ";

        s+= l[i].toString();

        s+= "end";
        
    }

    return s;
}

HashMap::HashFunction HashMap::getHashFunction() const{
    return hashFunction;
}

HashLinkedList* HashMap::getLinkedList() const{
    return l;
}

HashMap::HashMap(const HashMap& hm)
    :currsize{hm.size()}, bucketcount{hm.bucketCount()}, l{new HashLinkedList[hm.bucketCount()]}, hashFunction{hm.getHashFunction()}{ 
        HashLinkedList* linkedlistold = hm.getLinkedList();
        fillHashEmptyLL(bucketcount,l);

        for(int i =0; i < bucketcount; i++){
            l[i] = linkedlistold[i];
        }
}

HashMap& HashMap::operator=(const HashMap& hm){
    if(this != &hm){
        delete[] l;
        currsize = hm.size();
        bucketcount = hm.bucketCount();
        l = new HashLinkedList[bucketcount];
        hashFunction = hm.getHashFunction();

        HashLinkedList* linkedlistold = hm.getLinkedList();
        fillHashEmptyLL(bucketcount,l);

        for(int i =0; i < bucketcount; i++){
            l[i] = linkedlistold[i];
        }
    }

    return *this;
}