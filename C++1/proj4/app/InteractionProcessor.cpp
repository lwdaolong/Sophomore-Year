// InteractionProcessor.cpp
//
// ICS 45C Spring 2021
// Project #4: People Just Love to Play with Words
//
// Implementation of the InteractionProcessor class

#include "InteractionProcessor.hpp"
#include "EditorException.hpp"
#include "Interaction.hpp"


#include <vector>


// This function implements command execution, but does not handle "undo"
// and "redo"; you'll need to add that handling.

void InteractionProcessor::run()
{
    std::vector<Command*> undostack;
    std::vector<Command*> redostack;


    view.refresh();

    while (true)
    {
        Interaction interaction = interactionReader.nextInteraction();

        if (interaction.type() == InteractionType::quit)
        {
            
            for(int i =0; i < undostack.size();i++){
                delete undostack[i];
            }
            for(int i =0; i < redostack.size();i++){
                delete redostack[i];
            }
            
            undostack.clear();
            redostack.clear();
            break;
        }
        else if (interaction.type() == InteractionType::undo)
        {
            if(undostack.size()>0){
                model.clearErrorMessage();
                Command* tempcommand = undostack.back();
                tempcommand->undo(model);
                /*
                if(redostack.size()<1){
                    redostack.push_back(NULL);
                    redostack.back() = tempcommand;
                }else{
                    redostack.back() = tempcommand;
                }
                undostack.back() = NULL;
                undostack.resize(undostack.size()-1);
                */
                redostack.push_back(tempcommand);
                undostack.pop_back();
                view.refresh();
            }else{
                //throw exception maybe? Nothing to undo
            }
            
        }
        else if (interaction.type() == InteractionType::redo)
        {
            if(redostack.size()>0){
                Command* tempcommand = redostack.back();
                tempcommand->execute(model);
                /*
                if(undostack.size() <1){
                    undostack.push_back(NULL);
                    undostack.back() = tempcommand;
                }else{
                    undostack.back() = tempcommand;
                }
                redostack.back() = NULL;
                redostack.resize(undostack.size()-1);
                */
                undostack.push_back(tempcommand);
                redostack.pop_back();
                view.refresh();
            }else{
                //throw exception maybe? Nothing to redo
            }
            
        }
        else if (interaction.type() == InteractionType::command)
        {
            Command* command = interaction.command();

            try
            {
                command->execute(model);
                model.clearErrorMessage();
                /*
                if(undostack.size() <1){
                    undostack.push_back(NULL);
                    undostack.back() = command;
                }else{
                    undostack.back() = command;
                }
                */

                undostack.push_back(command);
                for(int i =0; i < redostack.size();i++){
                    delete redostack[i];
                }
                redostack.clear();
            }
            catch (EditorException& e)
            {
                delete command; 
                model.setErrorMessage(e.getReason());
            }

            view.refresh();

            // Note that you'll want to be more careful about when you delete
            // commands once you implement undo and redo.  For now, since
            // neither is implemented, I've just deleted it immediately
            // after executing it.  You'll need to wait to delete it until
            // you don't need it anymore.
            
        }
    }
    
}

