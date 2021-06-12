//writecharcommand.hpp
#ifndef WRITECHARCOMMAND_HPP
#define WRITECHARCOMMAND_HPP

#include "Command.hpp"
#include "EditorException.hpp"



class WriteChar:public Command
{
public:
    WriteChar(char a);

    void execute(EditorModel& model) override;

    void undo(EditorModel& model) override;

private:
    int line;
    int col;
    char a;
};



#endif