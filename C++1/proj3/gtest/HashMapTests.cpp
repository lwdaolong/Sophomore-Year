// HashMapTests.cpp
//
// ICS 45C Spring 2021
// Project #3: Maps and Legends
//
// Write unit tests for your HashMap class here.  I've provided a few tests
// already, though I've commented them out, because they won't compile and
// link until you've implemented some things.
//
// Of course, you'll want to write lots more of these tests yourself, because
// this is an inexpensive way to know whether things are working the way
// you expect -- including scenarios that you won't happen to hit in the
// course of testing your overall program.  (You might also want to be sure
// that your HashMap implementation is complete and correct before you try
// to write the rest of the program around it, anyway; there's a very
// substantial amount of partial credit available if all that works is
// HashMap.)

#include <gtest/gtest.h>
#include "HashMap.hpp"

namespace
{
    unsigned int someHashFunction(const std::string& s)
    {
        return 19;
    }
}


TEST(HashMapTests, sizeOfNewlyCreatedHashMapIsZero)
{
    HashMap empty;
    ASSERT_EQ(0, empty.size());
}

TEST(HashMapTests, HashMapCreatedWithCustomHashFunction)
{
    HashMap hm(someHashFunction);
    HashMap::HashFunction hashfunctionappliedtoobject = hm.getHashFunction();
    ASSERT_EQ(someHashFunction("test"), hashfunctionappliedtoobject("test"));
}


TEST(HashMapTests, emptyMapContainsNoKeys)
{
    HashMap empty;
    ASSERT_FALSE(empty.contains("first"));
    ASSERT_FALSE(empty.contains("second"));
}


TEST(HashMapTests, containKeyAfterAddingIt)
{
    HashMap hm;
    hm.add("Boo", "perfect");
    ASSERT_TRUE(hm.contains("Boo"));
}

TEST(HashMapTests, addBoolTest)
{
    HashMap hm;
    ASSERT_TRUE(hm.addBool("testuser","testpass"));
    ASSERT_EQ(1, hm.size());
    ASSERT_EQ(10,hm.bucketCount());
    ASSERT_EQ(.1, hm.loadFactor());
    ASSERT_EQ(1,hm.maxBucketSize());

    ASSERT_TRUE(hm.addBool("testusertwo","testpass2"));
    ASSERT_EQ(2, hm.size());
    ASSERT_EQ(10,hm.bucketCount());
    ASSERT_EQ(.2, hm.loadFactor());
    ASSERT_EQ(1,hm.maxBucketSize());


    ASSERT_TRUE(hm.contains("testuser"));
    ASSERT_TRUE(hm.contains("testusertwo"));

    ASSERT_FALSE(hm.addBool("testuser","testpass"));
}

TEST(HashMapTests, removeTests)
{
    HashMap hm;
    ASSERT_TRUE(hm.addBool("testuser","testpass"));
    ASSERT_TRUE(hm.addBool("testuser2","testpass2"));


    ASSERT_FALSE(hm.remove("usernoexist"));
    ASSERT_TRUE(hm.remove("testuser"));
    ASSERT_EQ(1, hm.size());
    ASSERT_EQ(10,hm.bucketCount());
    ASSERT_EQ(.1, hm.loadFactor());
    ASSERT_EQ(1,hm.maxBucketSize());

    ASSERT_TRUE(hm.remove("testuser2"));
    ASSERT_EQ(0, hm.size());
    ASSERT_EQ(10,hm.bucketCount());
    ASSERT_EQ(0, hm.loadFactor());
    ASSERT_EQ(0,hm.maxBucketSize());

    ASSERT_FALSE(hm.contains("testuser"));
    ASSERT_FALSE(hm.contains("testuser2"));
}


TEST(HashMapTests, containsKVTest)
{
    HashMap hm;
    ASSERT_TRUE(hm.addBool("testuser","testpass"));
    ASSERT_TRUE(hm.addBool("testusertwo","testpass2"));
  


    ASSERT_TRUE(hm.containsKV("testuser","testpass"));
    ASSERT_TRUE(hm.containsKV("testusertwo","testpass2"));

    ASSERT_FALSE(hm.containsKV("testuser","wrongpass"));
    ASSERT_FALSE(hm.containsKV("testusertwo","wrongpass2"));

    ASSERT_FALSE(hm.containsKV("usernoexist","wrongpass2"));
}

TEST(HashMapTests, valueTest)
{
    HashMap hm;
    ASSERT_TRUE(hm.addBool("testuser","testpass"));
    ASSERT_TRUE(hm.addBool("testusertwo","testpass2"));
  


    ASSERT_EQ("testpass",hm.value("testuser"));
    ASSERT_EQ("testpass2",hm.value("testusertwo"));

    ASSERT_EQ("",hm.value("usernoexist"));
}

TEST(HashMapTests, sizeTest){
    HashMap hm;
    std::string s ="a";
    for(int i=0; i < 21; i++){
        ASSERT_EQ(i,hm.size());
        hm.add(s,s);
        s += s;
    }


}

TEST(HashMapTests, bucketCountTest){
    HashMap hm;
    std::string s ="a";
    for(int i=0; i < 8; i++){
        ASSERT_EQ(10,hm.bucketCount());
        hm.add(s,s);
        s += s;
    }

    hm.add("randomuser","randompass"); // shows resizing as well
    ASSERT_EQ(21,hm.bucketCount());

}

TEST(HashMapTests, loadFactorTest){
    HashMap hm;
    std::string s ="a";
    for(int i=0; i < 8; i++){
        ASSERT_EQ((i/double(10)),hm.loadFactor());
        hm.add(s,s);
        s += s;
    }

    hm.add("randomuser","randompass"); // shows resizing as well
    ASSERT_EQ((9/double(21)),hm.loadFactor());

}


TEST(HashMapTests, EmptyHashMapClearTest){
    HashMap hm;
    ASSERT_EQ(0, hm.size());
    ASSERT_EQ(10,hm.bucketCount());
    ASSERT_EQ(0, hm.loadFactor());
    ASSERT_EQ(0,hm.maxBucketSize());

    hm.clear();
    ASSERT_EQ(0, hm.size());
    ASSERT_EQ(10,hm.bucketCount());
    ASSERT_EQ(0, hm.loadFactor());
    ASSERT_EQ(0,hm.maxBucketSize());

}

TEST(HashMapTests, NonEmptyHashMapClearTest){
    HashMap hm;
    std::string s ="a";
    for(int i=0; i < 8; i++){
        hm.add(s,s);
        s += s;
    }

    hm.clear();
    ASSERT_EQ(0, hm.size());
    ASSERT_EQ(10,hm.bucketCount());
    ASSERT_EQ(0, hm.loadFactor());
    ASSERT_EQ(0,hm.maxBucketSize());

}


TEST(HashMapTests, coppyConstructorEmptyTest){
    HashMap hm;
    
    HashMap a = hm;
    ASSERT_EQ(0, a.size());
    ASSERT_EQ(10,a.bucketCount());
    ASSERT_EQ(0, a.loadFactor());
    ASSERT_EQ(0,a.maxBucketSize());
}

namespace
{
    HashMap copyconstructemptytestmethod(std::string& z){
        HashMap hm;
    std::string s ="a";
    for(int i=0; i < 8; i++){
        
        hm.add(s,s);
        s += s;
    }

    hm.add("randomuser","randompass"); // shows resizing as well
    
    z= hm.toString();

    HashMap a = hm;
    return a;
    }
}

TEST(HashMapTests, coppyConstructorNonEmptyTest){
    std::string s ="";
    HashMap a = copyconstructemptytestmethod(s); //use this function to force other Hashmaps to be deleted, showing that copy constructor actually copies values not just references
    

    ASSERT_EQ(9, a.size());
    ASSERT_EQ(21,a.bucketCount());
    ASSERT_EQ((9/double(21)), a.loadFactor());
    ASSERT_EQ(2,a.maxBucketSize());

    ASSERT_EQ(s,a.toString());
}

TEST(HashMapTests, coppyAssignmentEmptyTest){
    HashMap hm;
    std::string s ="a";
    for(int i=0; i < 8; i++){
        
        hm.add(s,s);
        s += s;
    }

    hm.add("randomuser","randompass"); // shows resizing as well
    
    HashMap empty;
    hm = empty;
    ASSERT_EQ(0, hm.size());
    ASSERT_EQ(10,hm.bucketCount());
    ASSERT_EQ(0, hm.loadFactor());
    ASSERT_EQ(0,hm.maxBucketSize());
    ASSERT_EQ(hm.toString(),empty.toString());

}

namespace
{
    HashMap copyassignmenttestmethod(std::string& y){

    HashMap hm;
    std::string s ="a";
    for(int i=0; i < 8; i++){
        
        hm.add(s,s);
        s += s;
    }

    hm.add("randomuser","randompass"); // shows resizing as well

    HashMap a;
    std::string z ="b";
    for(int i=0; i < 9; i++){
        
        a.add(z,z);
        z += z;
    }

    a.add("randomuserb","randompassb"); // shows resizing as well
    
    y= a.toString();
    
    hm = a;
    return hm;
    }
}

TEST(HashMapTests, coppyAssignmentNonEmptyTest){
    std::string s = "";
    HashMap hm = copyassignmenttestmethod(s); //use this function to force other Hashmaps to be deleted, showing that copy assignment actually copies values not just references
    


    ASSERT_EQ(10, hm.size());
    ASSERT_EQ(21,hm.bucketCount());
    ASSERT_EQ((10/double(21)), hm.loadFactor());
    ASSERT_EQ(5,hm.maxBucketSize());

    ASSERT_EQ(hm.toString(),s);
}


TEST(HashMapTests, resizeTest){
    HashMap hm;
    hm.add("1","1");
    hm.add("2","1");
    hm.add("3","1");
    hm.add("4","1");
    hm.add("5","1");
    hm.add("6","1");
    hm.add("7","1");
    hm.add("8","1");

    ASSERT_EQ(10,hm.bucketCount());
    
    hm.add("9","1");

    ASSERT_EQ(21,hm.bucketCount());

    hm.add("10","1");
    hm.add("11","1");
    hm.add("12","1");
    hm.add("13","1");
    hm.add("14","1");
    hm.add("15","1");
    hm.add("16","1");

    ASSERT_EQ(21,hm.bucketCount());
    hm.add("17","1");

    ASSERT_EQ(43,hm.bucketCount());
}


TEST(HashMapTests, maxbucketcounTest){
    HashMap hm;
    std::string s = "s";
    std::string p;

    

    for(int j =0; j< 8; j++){
        ASSERT_EQ(j,hm.maxBucketSize());

        for(int i =0; i<10; i++){
            p+=s;
        }
        hm.add(p,"randompass");

    }


}



