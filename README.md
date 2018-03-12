# chcd
Change directory (i.e. cd command) to zprezto abbreviated paths

## What?
The default zprezto prompt contains an abbreviated version of the current path, for example */etc/X11/xinit/xinitrc.d* is printed as */e/X/x/xinitrc.d* and chcd will try to cd to a path using its abbreviation. This is done using a depth first search of the file system and it will select the first match, so you might end up in the wrong place if there are several matching paths. If chcd comes across a directory with the same name as your user name it will try to match that directory first, other than that directories are tried in the order that they are returned from *os.listdir()*.

## Why?
I have lots of ssh sessions to a server I'm working on, and when I get disconnected I want to quickly get back to where I was working.

## Example
    $ chcd ~/.z/m/p/functions
    > Directory changed to ~/.zprezto/modules/prompt/functions
    
## Installation
1. Clone into *~/.zprezto/modules/chcd*
2. Add *'chcd'* to module list in your *zpreztorc*
