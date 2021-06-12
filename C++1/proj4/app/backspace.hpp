//backspace.hpp
#ifndef BACKSPACE_HPP
#define BACKSPACE_HPP

#include "Command.hpp"
#include "EditorException.hpp"



class BackSpace:public Command
{
public:
    BackSpace();

    void execute(EditorModel& model) override;
    void undo(EditorModel& model) override;

private:
    bool deletesline;
    int line;
    int col;
    char a;
};



#endif