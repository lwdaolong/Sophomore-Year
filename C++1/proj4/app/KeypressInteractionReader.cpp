// KeypressInteractionReader.cpp
//
// ICS 45C Spring 2021
// Project #4: People Just Want to Play with Words
//
// Implementation of the KeypressInteractionReader
//
// YOU WILL NEED TO IMPLEMENT SOME THINGS HERE

#include "KeypressInteractionReader.hpp"
#include "cursorright.hpp"
#include "cursorleft.hpp"
#include "writecharcommand.hpp"
#include "newlinecommand.hpp"
#include "cursorup.hpp"
#include "cursordown.hpp"
#include "cursorhome.hpp"
#include "cursorend.hpp"
#include "backspace.hpp"
#include "deleteline.hpp"

// You will need to update this member function to watch for the right
// keypresses and build the right kinds of Interactions as a result.
//
// The reason you'll need to implement things here is that you'll need
// to create Command objects, which you'll be declaring and defining
// yourself; they haven't been provided already.
//
// I've added handling for "quit" here, but you'll need to add the others.

Interaction KeypressInteractionReader::nextInteraction()
{
    while (true)
    {
        Keypress keypress = keypressReader.nextKeypress();

        if (keypress.ctrl())
        {
            // The user pressed a Ctrl key (e.g., Ctrl+X); react accordingly

            switch (keypress.code())
            {
            case 'X':
                return Interaction::quit();
            case 'Z':
                return Interaction::undo();
            case 'A':
                return Interaction::redo();
            case 'O':
                return Interaction::command(new CursorRight());
            case 'U':
                return Interaction::command(new CursorLeft());
            case 'J':
                return Interaction::command(new NewLineCommand());
            case 'M':
                return Interaction::command(new NewLineCommand());
            case 'I':
                return Interaction::command(new CursorUp());
            case 'K':
                return Interaction::command(new CursorDown());
            case 'Y':
                return Interaction::command(new CursorHome());
            case 'P':
                return Interaction::command(new CursorEnd());
            case 'H':
                return Interaction::command(new BackSpace());
            case 'D':
                return Interaction::command(new DeleteLine());
            }
        }
        else
        {   
            return Interaction::command(new WriteChar(keypress.code()));
            // The user pressed a normal key (e.g., 'h') without holding
            // down Ctrl; react accordingly
        }
    }
}

