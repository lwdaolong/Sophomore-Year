//HashLinkedListUnitTest.cpp

#include <gtest/gtest.h>
#include <string>
#include "HashLinkedList.hpp"

//tests on LL of size 0

TEST(HashLL_UnitTests, ConstructEmptyLL)
{
    HashLinkedList l;
    ASSERT_EQ(true,l.isEmpty());
    ASSERT_EQ(0,l.getSize());
    ASSERT_EQ(NULL,l.getHeadNode());
    ASSERT_EQ(NULL,l.getTailNode());
}

TEST(HashLL_UnitTests, ClearEmptyLL)
{
    HashLinkedList l;
    ASSERT_EQ(true,l.isEmpty());
    ASSERT_EQ(0,l.getSize());
    ASSERT_EQ(NULL,l.getHeadNode());
    ASSERT_EQ(NULL,l.getTailNode());

    l.clear();
    ASSERT_EQ(true,l.isEmpty());
    ASSERT_EQ(0,l.getSize());
    ASSERT_EQ(NULL,l.getHeadNode());
    ASSERT_EQ(NULL,l.getTailNode());
}

TEST(HashLL_UnitTests, TestGetMethodsOnEmptyLL)
{
    HashNode* testnode = new HashNode("usertest","userpass");
    //HashNode* testptr = &testnode;

    HashLinkedList l;
    ASSERT_EQ(NULL,l.getNodebyKey("test"));
    ASSERT_EQ(NULL,l.getNodebyValue("test"));
    ASSERT_EQ(false,l.contains(testnode));
    ASSERT_EQ(false,l.containsKeyValuePair("testuser","testpass"));
    delete testnode;
}

TEST(HashLL_UnitTests, TestRemoveMethodsOnEmptyLL)
{

    HashLinkedList l;
    int originalsize = l.getSize(); //use to test void methods, kinda janky

    ASSERT_EQ(false,l.removeNodebyKey("testuser"));

    l.removeFirst();
    ASSERT_EQ(originalsize,l.getSize());
    l.removeLast();
    ASSERT_EQ(originalsize,l.getSize());
}

TEST(HashLL_UnitTests, TestPrependToEmptyLL)
{
    HashNode* testnode = new HashNode("usertest","userpass");
    HashLinkedList l;

    l.prependNode(testnode);
    ASSERT_EQ(false,l.isEmpty());
    ASSERT_EQ(1,l.getSize());
    ASSERT_EQ(testnode,l.getHeadNode());
    ASSERT_EQ(testnode,l.getTailNode());
}

TEST(HashLL_UnitTests, TestAppendToEmptyLL)
{
    HashNode* testnode = new HashNode("usertest","userpass");
    HashLinkedList l;

    l.appendNode(testnode);
    ASSERT_EQ(false,l.isEmpty());
    ASSERT_EQ(1,l.getSize());
    ASSERT_EQ(testnode,l.getHeadNode());
    ASSERT_EQ(testnode,l.getTailNode());
}

//tests on LL of length 1

TEST(HashLL_UnitTests, ConstructLLwHeadNode)
{
    HashNode* testnode = new HashNode("usertest","userpass");
    HashLinkedList l(testnode);
    ASSERT_EQ(false,l.isEmpty());
    ASSERT_EQ(1,l.getSize());
    ASSERT_EQ(testnode,l.getHeadNode());
    ASSERT_EQ(testnode,l.getTailNode());
}

TEST(HashLL_UnitTests, ClearLLSizeOne)
{
    HashNode* testnode = new HashNode("usertest","userpass");
    HashLinkedList l(testnode);
    ASSERT_EQ(false,l.isEmpty());
    ASSERT_EQ(1,l.getSize());
    ASSERT_EQ(testnode,l.getHeadNode());
    ASSERT_EQ(testnode,l.getTailNode());

    l.clear();
    ASSERT_EQ(true,l.isEmpty());
    ASSERT_EQ(0,l.getSize());
    ASSERT_EQ(NULL,l.getHeadNode());
    ASSERT_EQ(NULL,l.getTailNode());
}

TEST(HashLL_UnitTests, TestGetMethodsOnLLSizeOne)
{
    HashNode* nodenotinLL = new HashNode("k","v");
    HashNode* testnode = new HashNode("usertest","userpass");
    //HashNode* testptr = &testnode;

    HashLinkedList l(testnode);
    ASSERT_EQ(NULL,l.getNodebyKey("test"));
    ASSERT_EQ(NULL,l.getNodebyValue("test"));
    ASSERT_EQ(testnode,l.getNodebyKey("usertest"));
    ASSERT_EQ(testnode,l.getNodebyValue("userpass"));
    ASSERT_EQ(true,l.contains(testnode));
    ASSERT_EQ(true,l.containsKeyValuePair("usertest","userpass"));
    ASSERT_EQ(false,l.contains(nodenotinLL));
    ASSERT_EQ(false,l.containsKeyValuePair("k","v"));
    delete nodenotinLL;
}

/*
TEST(HashLL_UnitTests, TestRemoveMethodsOnLLSizeOne)
{
    HashNode* nodenotinLL = new HashNode("k","v");
    HashNode* testnode = new HashNode("usertest","userpass");
    //HashNode* testptr = &testnode;

    HashLinkedList l(testnode);

    ASSERT_EQ(false,l.removeNodebyKey("k"));
    ASSERT_EQ(1,l.getSize());
    ASSERT_EQ(true,l.removeNodebyKey("usertest"));
    ASSERT_EQ(0,l.getSize());

    l.prependNode(testnode);
    l.removeFirst();
    ASSERT_EQ(0,l.getSize());

    l.prependNode(testnode);
    l.removeLast();
    ASSERT_EQ(0,l.getSize());
    delete nodenotinLL;
}
*/

TEST(HashLL_UnitTests, TestPrependToLLSizeOne)
{
    HashNode* nodeToAdd = new HashNode("2","2");
    HashNode* testnode = new HashNode("usertest","userpass");
    //HashNode* testptr = &testnode;

    HashLinkedList l(testnode);

    l.prependNode(nodeToAdd);
    ASSERT_EQ(false,l.isEmpty());
    ASSERT_EQ(2,l.getSize());
    ASSERT_EQ(nodeToAdd,l.getHeadNode());
    ASSERT_EQ(testnode,l.getTailNode());
}

TEST(HashLL_UnitTests, TestAppendToLLSizeOne)
{
    HashNode* nodeToAdd = new HashNode("2","2");
    HashNode* testnode = new HashNode("usertest","userpass");
    HashLinkedList l(testnode);

    l.appendNode(nodeToAdd);
    ASSERT_EQ(false,l.isEmpty());
    ASSERT_EQ(2,l.getSize());
    ASSERT_EQ(testnode,l.getHeadNode());
    ASSERT_EQ(nodeToAdd,l.getTailNode());
}

//tests on LL of size n

TEST(HashLL_UnitTests, ClearLLSizeN)
{
    HashNode* node1 = new HashNode("1","1");
    HashNode* node2= new HashNode("2","2");
    HashNode* node3 = new HashNode("3","3");

    HashLinkedList l(node1);
    l.appendNode(node2);
    l.appendNode(node3);
    ASSERT_EQ(false,l.isEmpty());
    ASSERT_EQ(3,l.getSize());
    ASSERT_EQ(node1,l.getHeadNode());
    ASSERT_EQ(node3,l.getTailNode());

    l.clear();
    ASSERT_EQ(true,l.isEmpty());
    ASSERT_EQ(0,l.getSize());
    ASSERT_EQ(NULL,l.getHeadNode());
    ASSERT_EQ(NULL,l.getTailNode());
}

TEST(HashLL_UnitTests, TestGetMethodsOnLLSizeN)
{
    HashNode* nodenotinLL = new HashNode("k","v");
    HashNode* node1 = new HashNode("1","1p");
    HashNode* node2 = new HashNode("2","2p");
    HashNode* node3 = new HashNode("3","3p");

    HashLinkedList l(node1);
    l.appendNode(node2);
    l.appendNode(node3);

    ASSERT_EQ(NULL,l.getNodebyKey("test")); //Node that doesn't exist at all
    ASSERT_EQ(NULL,l.getNodebyValue("v")); //Node that exists, but not in linked list
    ASSERT_EQ(node1,l.getNodebyKey("1"));
    ASSERT_EQ(node2,l.getNodebyKey("2"));
    ASSERT_EQ(node3,l.getNodebyKey("3"));

    ASSERT_EQ(node1,l.getNodebyValue("1p"));
    ASSERT_EQ(node2,l.getNodebyValue("2p"));
    ASSERT_EQ(node3,l.getNodebyValue("3p"));

    ASSERT_EQ(true,l.contains(node1));
    ASSERT_EQ(true,l.contains(node2));
    ASSERT_EQ(true,l.contains(node3));
    ASSERT_EQ(false,l.contains(nodenotinLL));

    ASSERT_EQ(true,l.containsKeyValuePair("1","1p"));
    ASSERT_EQ(true,l.containsKeyValuePair("2","2p"));
    ASSERT_EQ(true,l.containsKeyValuePair("3","3p"));

    ASSERT_EQ(false,l.containsKeyValuePair("1","1")); //username exists, but not corrosponding password
    ASSERT_EQ(false,l.containsKeyValuePair("asjkdla","1p"));  //username does not exist, but password does
    ASSERT_EQ(false,l.containsKeyValuePair("k","v")); //pair exists, not in this linked list
    ASSERT_EQ(false,l.containsKeyValuePair("asdasdsa","adsadadas")); //pair does not exist anyweher
    delete nodenotinLL;
}

TEST(HashLL_UnitTests, TestRemoveFirstLLSizeN)
{
    HashNode* nodenotinLL = new HashNode("k","v");
    HashNode* node1 = new HashNode("1","1p");
    HashNode* node2 = new HashNode("2","2p");
    HashNode* node3 = new HashNode("3","3p");

    HashLinkedList l(node1);
    l.appendNode(node2);
    l.appendNode(node3);

    ASSERT_EQ(false,l.removeNodebyKey("k"));
    ASSERT_EQ(3,l.getSize());

    l.removeFirst();
    ASSERT_EQ(2,l.getSize());
    ASSERT_EQ(node2,l.getHeadNode());
    ASSERT_EQ(node3,l.getTailNode());
    delete nodenotinLL;
}

TEST(HashLL_UnitTests, TestRemoveLastLLSizeN)
{
    HashNode* nodenotinLL = new HashNode("k","v");
    HashNode* node1 = new HashNode("1","1p");
    HashNode* node2 = new HashNode("2","2p");
    HashNode* node3 = new HashNode("3","3p");

    HashLinkedList l(node1);
    l.appendNode(node2);
    l.appendNode(node3);

    ASSERT_EQ(false,l.removeNodebyKey("k"));
    ASSERT_EQ(3,l.getSize());

    l.removeLast();
    ASSERT_EQ(2,l.getSize());
    ASSERT_EQ(node1,l.getHeadNode());
    ASSERT_EQ(node2,l.getTailNode());
    delete nodenotinLL;
}

TEST(HashLL_UnitTests, TestRemoveKeyMiddleLLSizeN)
{
    HashNode* nodenotinLL = new HashNode("k","v");
    HashNode* node1 = new HashNode("1","1p");
    HashNode* node2 = new HashNode("2","2p");
    HashNode* node3 = new HashNode("3","3p");

    HashLinkedList l(node1);
    l.appendNode(node2);
    l.appendNode(node3);

    ASSERT_EQ(false,l.removeNodebyKey("k"));
    ASSERT_EQ(3,l.getSize());

    l.removeNodebyKey("2");
    ASSERT_EQ(2,l.getSize());
    ASSERT_EQ(node1,l.getHeadNode());
    ASSERT_EQ(node3,l.getTailNode());
    delete nodenotinLL;
}

TEST(HashLL_UnitTests, TestRemoveKeyHeadLLSizeN)
{
    HashNode* nodenotinLL = new HashNode("k","v");
    HashNode* node1 = new HashNode("1","1p");
    HashNode* node2 = new HashNode("2","2p");
    HashNode* node3 = new HashNode("3","3p");

    HashLinkedList l(node1);
    l.appendNode(node2);
    l.appendNode(node3);

    ASSERT_EQ(false,l.removeNodebyKey("k"));
    ASSERT_EQ(3,l.getSize());

    l.removeNodebyKey("1");
    ASSERT_EQ(2,l.getSize());
    ASSERT_EQ(node2,l.getHeadNode());
    ASSERT_EQ(node3,l.getTailNode());
    delete nodenotinLL;
}

TEST(HashLL_UnitTests, TestRemoveKeyTailLLSizeN)
{
    HashNode* nodenotinLL = new HashNode("k","v");
    HashNode* node1 = new HashNode("1","1p");
    HashNode* node2 = new HashNode("2","2p");
    HashNode* node3 = new HashNode("3","3p");

    HashLinkedList l(node1);
    l.appendNode(node2);
    l.appendNode(node3);

    ASSERT_EQ(false,l.removeNodebyKey("k"));
    ASSERT_EQ(3,l.getSize());

    l.removeNodebyKey("3");
    ASSERT_EQ(2,l.getSize());
    ASSERT_EQ(node1,l.getHeadNode());
    ASSERT_EQ(node2,l.getTailNode());
    delete nodenotinLL;
}



TEST(HashLL_UnitTests, TestPrependToLLSizeN)
{
    HashNode* nodeToAdd = new HashNode("k","v");
    HashNode* node1 = new HashNode("1","1p");
    HashNode* node2 = new HashNode("2","2p");
    HashNode* node3 = new HashNode("3","3p");

    HashLinkedList l(node1);
    l.appendNode(node2);
    l.appendNode(node3);

    l.prependNode(nodeToAdd);
    ASSERT_EQ(false,l.isEmpty());
    ASSERT_EQ(4,l.getSize());
    ASSERT_EQ(nodeToAdd,l.getHeadNode());
    ASSERT_EQ(node3,l.getTailNode());
}

TEST(HashLL_UnitTests, TestAppendToLLSizeN)
{
    HashNode* nodeToAdd = new HashNode("k","v");
    HashNode* node1 = new HashNode("1","1p");
    HashNode* node2 = new HashNode("2","2p");
    HashNode* node3 = new HashNode("3","3p");

    HashLinkedList l(node1);
    l.appendNode(node2);
    l.appendNode(node3);

    l.appendNode(nodeToAdd);
    ASSERT_EQ(false,l.isEmpty());
    ASSERT_EQ(4,l.getSize());
    ASSERT_EQ(node1,l.getHeadNode());
    ASSERT_EQ(nodeToAdd,l.getTailNode());
}