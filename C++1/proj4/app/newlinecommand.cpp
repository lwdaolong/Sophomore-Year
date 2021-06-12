//newlinecommand.cpp
#include "newlinecommand.hpp"


NewLineCommand::NewLineCommand(){
    }

void NewLineCommand::execute(EditorModel& model){ 
    line = model.cursorLine();
    col = model.cursorColumn();
    model.createNewLine();
}
void NewLineCommand::undo(EditorModel& model){
    model.undoNewLine(line,col);
}