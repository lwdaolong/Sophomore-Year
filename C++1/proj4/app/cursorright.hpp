//cursorright.hpp
#ifndef CURSORRIGHT_HPP
#define CURSORRIGHT_HPP

#include "Command.hpp"
#include "EditorException.hpp"



class CursorRight:public Command
{
public:
    CursorRight();

    void execute(EditorModel& model) override;
        
    void undo(EditorModel& model) override;

private:
    
};



#endif