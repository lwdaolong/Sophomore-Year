//cursorup.cpp
#include "cursorup.hpp"

CursorUp::CursorUp(){
}

void CursorUp::execute(EditorModel& model){ 
    if(model.cursorLine() == 1){
        throw EditorException("Already at top");
    }else{
        line = model.cursorLine();
        col = model.cursorColumn();
        model.moveCursorUp();
    }           
}

void CursorUp::undo(EditorModel& model){
    model.setCursor(line,col);
}