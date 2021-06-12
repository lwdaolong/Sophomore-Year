//writecharcommand.cpp
#include "writecharcommand.hpp"

WriteChar::WriteChar(char a)
:a(a){

}

void WriteChar::execute(EditorModel& model){ 
    line = model.cursorLine();
    col = model.cursorColumn();
    model.insertChar(line,col,a);
    model.incrementCurrColRight();
}
void WriteChar::undo(EditorModel& model){
    model.deleteCharatcol(line,col);
    model.decrementCurrColLeft();
}