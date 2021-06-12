//deleteline.cpp
#include "deleteline.hpp"

DeleteLine::DeleteLine()
:deletedonlyline(false){
}

void DeleteLine::execute(EditorModel& model){ 
    line = model.cursorLine();
    col = model.cursorColumn();
    a = model.line(line);

    model.deletLine(deletedonlyline);
}
void DeleteLine::undo(EditorModel& model){
    if(deletedonlyline == true){
        model.refillFirstLine(a);
    }else{
        model.setLine(line,a);
        
    }
    model.setCursor(line,col);
}