//HashNodeUnitTests.cpp
#include <gtest/gtest.h>
#include <string>
#include "HashNode.hpp"

TEST(HashNode_UnitTests, canConstructwithKeyValuePair)
{
    HashNode testnode("usertest","userpass");
    ASSERT_EQ("usertest",testnode.getKey());
    ASSERT_EQ("userpass",testnode.getValue());
    ASSERT_EQ(NULL,testnode.getNext());
}

TEST(HashNode_UnitTests, canConstructwithKeyValuePairandNextPointer)
{   HashNode testnode1("usertest1","userpass1");
    HashNode* node1ptr = &testnode1;
    HashNode testnode2("usertest2","userpass2",node1ptr);
    ASSERT_EQ("usertest2",testnode2.getKey());
    ASSERT_EQ("userpass2",testnode2.getValue());
    ASSERT_EQ(node1ptr,testnode2.getNext());

    //tests tail node
    ASSERT_EQ("usertest1",(*testnode2.getNext()).getKey());
    ASSERT_EQ("userpass1",(*testnode2.getNext()).getValue());
    ASSERT_EQ(NULL,(*testnode2.getNext()).getNext());
}

TEST(HashNode_UnitTests, setKeyTest)
{
    HashNode testnode("usertest","userpass");
    ASSERT_EQ("usertest",testnode.getKey());
    ASSERT_EQ("userpass",testnode.getValue());
    ASSERT_EQ(NULL,testnode.getNext());

    testnode.setKey("changedkey");
    ASSERT_EQ("changedkey",testnode.getKey());
    ASSERT_EQ("userpass",testnode.getValue());
    ASSERT_EQ(NULL,testnode.getNext());
}

TEST(HashNode_UnitTests, setValueTest)
{
    HashNode testnode("usertest","userpass");
    ASSERT_EQ("usertest",testnode.getKey());
    ASSERT_EQ("userpass",testnode.getValue());
    ASSERT_EQ(NULL,testnode.getNext());

    testnode.setValue("changedvalue");
    ASSERT_EQ("usertest",testnode.getKey());
    ASSERT_EQ("changedvalue",testnode.getValue());
    ASSERT_EQ(NULL,testnode.getNext());
}

TEST(HashNode_UnitTests, setNextTestGeneral)
{
    HashNode testnode1("usertest1","userpass1");
    HashNode* node1ptr = &testnode1;

    HashNode testnode("usertest","userpass");
    ASSERT_EQ("usertest",testnode.getKey());
    ASSERT_EQ("userpass",testnode.getValue());
    ASSERT_EQ(NULL,testnode.getNext());

    testnode.setNext(node1ptr);
    ASSERT_EQ("usertest",testnode.getKey());
    ASSERT_EQ("userpass",testnode.getValue());
    ASSERT_EQ(node1ptr,testnode.getNext());

    ASSERT_EQ("usertest1",(*testnode.getNext()).getKey());
    ASSERT_EQ("userpass1",(*testnode.getNext()).getValue());
    ASSERT_EQ(NULL,(*testnode.getNext()).getNext());
}

TEST(HashNode_UnitTests, setNextTestNull)
{   HashNode testnode1("usertest1","userpass1");
    HashNode* node1ptr = &testnode1;
    HashNode testnode2("usertest2","userpass2",node1ptr);
    ASSERT_EQ("usertest2",testnode2.getKey());
    ASSERT_EQ("userpass2",testnode2.getValue());
    ASSERT_EQ(node1ptr,testnode2.getNext());

    //tests tail node
    ASSERT_EQ("usertest1",(*testnode2.getNext()).getKey());
    ASSERT_EQ("userpass1",(*testnode2.getNext()).getValue());
    ASSERT_EQ(NULL,(*testnode2.getNext()).getNext());

    testnode2.setNext(NULL);
    ASSERT_EQ("usertest2",testnode2.getKey());
    ASSERT_EQ("userpass2",testnode2.getValue());
    ASSERT_EQ(NULL,testnode2.getNext());
}

TEST(HashNode_UnitTests, setNextNullWhenAlreadyNull)
{

    HashNode testnode("usertest","userpass");
    ASSERT_EQ("usertest",testnode.getKey());
    ASSERT_EQ("userpass",testnode.getValue());
    ASSERT_EQ(NULL,testnode.getNext());

    testnode.setNext(NULL);
    ASSERT_EQ("usertest",testnode.getKey());
    ASSERT_EQ("userpass",testnode.getValue());
    ASSERT_EQ(NULL,testnode.getNext());
}