//cursorleft.hpp
#ifndef CURSORLEFT_HPP
#define CURSORLEFT_HPP

#include "Command.hpp"
#include "EditorException.hpp"



class CursorLeft:public Command
{
public:
    CursorLeft();

    void execute(EditorModel& model) override;
    
    void undo(EditorModel& model) override;

private:
  
};



#endif