//cursorend.hpp
#ifndef CURSOREND_HPP
#define CURSOREND_HPP

#include "Command.hpp"
#include "EditorException.hpp"



class CursorEnd:public Command
{
public:
    CursorEnd();

    void execute(EditorModel& model) override;

    void undo(EditorModel& model) override;

private:
    int line;
    int col;
};



#endif