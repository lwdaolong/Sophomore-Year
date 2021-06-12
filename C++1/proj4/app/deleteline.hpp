//deleteline.hpp
#ifndef DELETELINE_HPP
#define DELETELINE_HPP

#include "Command.hpp"
#include "EditorException.hpp"



class DeleteLine:public Command
{
public:
    DeleteLine();

    void execute(EditorModel& model) override;
    void undo(EditorModel& model) override;

private:
    bool deletedonlyline; //deleted first line when it was the only line
    int line;
    int col;
    std::string a;
};



#endif