#include <iostream>
#include <string>

std::string repeatString(int num, std::string re){
    std::string tmp_str = "";
    for(int i =0; i < num; i++){
        tmp_str += re;
    }
    return tmp_str;
}

int main()
{
    int input;
    std::cin >> input;
    int indent = input -1;

    for( int i = 1; i <= input; i++){
        std::string temp_indent = repeatString(indent-i+1," ");
        std::string top_chars =  repeatString(i,"**");
        std::string middle_chars = repeatString(i-1," *");
        std::cout<<temp_indent<<top_chars<<"*"<< std::endl;
        std::cout<<temp_indent<<"* *"<<middle_chars<<std::endl;

    }

    std::string temp_s = "";
    for (int i =0 ; i< input;i++){
        temp_s += "**";
    }

    std::cout<<temp_s<<"*"<<std::endl;


    return 0;
}

