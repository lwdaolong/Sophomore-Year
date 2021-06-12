//cursorright.cpp
#include "cursorright.hpp"

CursorRight::CursorRight(){

}

void CursorRight::execute(EditorModel& model){ 
    if(model.cursorColumn() <= model.line(model.cursorLine()).length()){
        model.incrementCurrColRight();
    }else{
        if(model.cursorLine()>=model.lineCount()){
            throw EditorException("Already at end");
        }else{
            model.incrementRow();
            model.setCol(1);
        }
    }
    
}
void CursorRight::undo(EditorModel& model){
    model.decrementCurrColLeft();
}