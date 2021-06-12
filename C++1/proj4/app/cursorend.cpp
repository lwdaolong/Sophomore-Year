//cursorend.cpp
#include "cursorend.hpp"

CursorEnd::CursorEnd(){

}

void CursorEnd::execute(EditorModel& model){ 
    line = model.cursorLine();
    col = model.cursorColumn();
    model.setCursor(line,model.line(line).length()+1);
}

void CursorEnd::undo(EditorModel& model){
    model.setCursor(line,col);
}