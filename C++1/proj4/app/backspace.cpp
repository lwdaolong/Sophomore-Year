//backspace.cpp
#include "backspace.hpp"

BackSpace::BackSpace()
:deletesline(false){
}

void BackSpace::execute(EditorModel& model){ 
    line = model.cursorLine();
    col = model.cursorColumn();
    if(col-2 >=0){
        a = model.line(line)[col-2];
        deletesline = false;
        model.backspaceinline(line,col);
        model.decrementCurrColLeft();
    }else if(line-1 >0){
        a = model.line(line-1)[model.line(line-1).length()-1];
        deletesline = true;
        model.backspacedeleteline(line,col);
        
    }else{
        throw EditorException("Already at beginning");
    }
}
void BackSpace::undo(EditorModel& model){
    if(deletesline == true){
        model.createNewLine();
    }else{
        model.insertChar(line,col-1,a);
        model.setCursor(line,col);
    }
}