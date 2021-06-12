//cursorhome.cpp
#include "cursorhome.hpp"

CursorHome::CursorHome(){

}

void CursorHome::execute(EditorModel& model){ 
    line = model.cursorLine();
    col = model.cursorColumn();
    model.setCursor(line,1);
}

void CursorHome::undo(EditorModel& model){
    model.setCursor(line,col);
}