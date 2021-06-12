// EditorModel.cpp
//
// ICS 45C Spring 2021
// Project #4: People Just Love to Play with Words
//
// Implementation of the EditorModel class

#include "EditorModel.hpp"
#include "EditorException.hpp"


EditorModel::EditorModel()
    :row(1),col(1),linecount(1),errormsg(""),textbeingeditted(std::vector<std::string>())
{
    textbeingeditted.push_back("");
}


int EditorModel::cursorLine() const
{
    return row;
}


int EditorModel::cursorColumn() const
{
    return col;
}


int EditorModel::lineCount() const //maybe textbeingeditted.size()? 
{
    return linecount;
}


const std::string& EditorModel::line(int lineNumber) const
{
    //static std::string removeThis = "BooEdit!";
    //return removeThis;
    return textbeingeditted.at(lineNumber-1);
}


const std::string& EditorModel::currentErrorMessage() const
{
    return errormsg;
}


void EditorModel::setErrorMessage(const std::string& errorMessage)
{
    errormsg = errorMessage;
}


void EditorModel::clearErrorMessage()
{
    errormsg="";
}

void EditorModel::setCol(int a){
    col = a;
}

void EditorModel::incrementCurrColRight(){
    col++;
}

void EditorModel::decrementCurrColLeft(){
    col--;
}

void EditorModel::setRow(int a){
    row = a;
}

void EditorModel::incrementRow(){
    row++;
}

void EditorModel::decrementRow(){
    row--;
}

void EditorModel::insertChar(int line, int col,char a){
    std::string temp = textbeingeditted.at(line-1);
    std::string sstart = temp.substr(0,col-1);
    std::string ssend = temp.substr(col-1,temp.length() - col +1);
    temp = sstart + a + ssend;
    textbeingeditted.at(line-1) =temp;
}

void EditorModel::deleteCharatcol(int line, int col){
    std::string temp = textbeingeditted.at(line-1);
    std::string sstart = temp.substr(0,col-1);
    if(col < temp.length()){
        std::string ssend = temp.substr(col,temp.length() - col);
        temp = sstart + ssend;
    }else{
        temp = sstart;
    }
    textbeingeditted.at(line-1) =temp;
}

void EditorModel::setCursor(int x, int y){
    row = x;
    col = y;
}

void EditorModel::createNewLine(){
    std::vector<std::string>::iterator it = textbeingeditted.begin()+row;
    std::string temp = textbeingeditted.at(row-1);
    std::string currline = temp.substr(0,col-1);
    std::string nextline = temp.substr(col-1);
    textbeingeditted.at(row-1) =currline;
    textbeingeditted.insert(it,nextline);
    linecount++;

    

    setCursor(row+1,1);//sets cursor at base of next line
}

void EditorModel::undoNewLine(int r, int c){
    std::vector<std::string>::iterator it = textbeingeditted.begin()+row-1;
    std::string temp = textbeingeditted.at(row-1);
    std::string prevline = textbeingeditted.at(row-2) + temp;
    textbeingeditted.at(row-2) =prevline;
    textbeingeditted.erase(it);
    linecount--;

    

    setCursor(r,c);//sets cursor at base of next line
}

void EditorModel::moveCursorUp(){
    if(col <= line(row-1).length()){
        decrementRow();
    }else{
        col = line(row-1).length()+1;
        decrementRow();
    }
}
void EditorModel::moveCursorDown(){
    if(col <= line(row+1).length()){
        incrementRow();
    }else{
        col = line(row+1).length()+1;
        incrementRow();
    }
}

void EditorModel::deletLine( bool& b){
    std::vector<std::string>::iterator it = textbeingeditted.begin()+row-1;
    if(row == 1 && linecount ==1){
        if(line(row).length() == 0){
            throw EditorException("Already empty");
        }else{
            textbeingeditted[0] = "";
            setCol(1);
            b =true;
        }
    }else if(row == linecount){
        moveCursorUp();
        textbeingeditted.erase(it);
        linecount--;
    }else{
        if(col <= line(row+1).length()){
            //do nothing
        }else{
            col = line(row+1).length()+1;
        }
        textbeingeditted.erase(it);
        linecount--;
        
    }

}

//ONLY for lines deleted that were not the first and only line
void EditorModel::setLine(int a, std::string s){ //only use for deleteline undo command
    std::vector<std::string>::iterator it = textbeingeditted.begin()+a-1;
    textbeingeditted.insert(it,s);
    linecount++;    
}

void EditorModel::refillFirstLine(std::string s){
    textbeingeditted[0] = s;
}

void EditorModel::backspaceinline(int x, int y){

    std::string temp = textbeingeditted.at(x-1);
    temp.erase(y-2,1);
    textbeingeditted.at(x-1) =temp;
}

void EditorModel::backspacedeleteline(int x, int y){
    std::vector<std::string>::iterator it = textbeingeditted.begin()+row-1;
    std::string currline = textbeingeditted.at(x-1);
    col = line(row-1).length()+1;
    row--;
    textbeingeditted[x-2] += currline;
    textbeingeditted.erase(it);
    linecount--;

}
