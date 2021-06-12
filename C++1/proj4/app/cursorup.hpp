//cursorup.hpp
#ifndef CURSORUP_HPP
#define CURSORUP_HPP

#include "Command.hpp"
#include "EditorException.hpp"



class CursorUp:public Command
{
public:
    CursorUp();

    void execute(EditorModel& model) override;

    void undo(EditorModel& model) override;

private:
    int line;
    int col;
};



#endif