//cursorleft.cpp
#include "cursorleft.hpp"

CursorLeft::CursorLeft(){

}

void CursorLeft::execute(EditorModel& model){ 
    if(model.cursorColumn() > 1){
        model.decrementCurrColLeft();
    }else{
        if(model.cursorLine() == 1){
            throw EditorException("Already at beginning");
        }else{
            model.decrementRow();
            model.setCol(model.line(model.cursorLine()).length() + 1);
        }
    }
    
}
void CursorLeft::undo(EditorModel& model) {
    model.incrementCurrColRight();
}