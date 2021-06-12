//cursordown.cpp
#include "cursordown.hpp"

CursorDown::CursorDown(){

}

void CursorDown::execute(EditorModel& model){ 
    if(model.cursorLine()>=model.lineCount()){
        throw EditorException("Already at bottom");
    }else{
        line = model.cursorLine();
        col = model.cursorColumn();
        model.moveCursorDown();
    }           
}

void CursorDown::undo(EditorModel& model){
    model.setCursor(line,col);
}