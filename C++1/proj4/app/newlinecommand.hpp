//newlinecommand.hpp
#ifndef NEWLINECOMMAND_HPP
#define NEWLINECOMMAND_HPP

#include "Command.hpp"
#include "EditorException.hpp"



class NewLineCommand:public Command
{
public:
    NewLineCommand();

    void execute(EditorModel& model) override;
    void undo(EditorModel& model) override;

private:
    int line;
    int col;
};



#endif