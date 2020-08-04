![pykattis](https://raw.githubusercontent.com/liuchia/pykattis/media/pykattis.gif)
A command line tool for testing and submitting [kattis](https://open.kattis.com/) solutions. Based on [kattis-cli](https://github.com/Kattis/kattis-cli). 

## Setup
Python 3.7 is required as well as the modules specified in requirements.txt. Like in kattis-cli, a .kattisrc file should be placed in the home directory. This file is obtained from https://open.kattis.com/download/kattisrc

## Usage
Simply run `python kattis XXX` where XXX is the problem id which can be copied from a kattis problem's URL. This will bring the user into a REPL. The edit command 'e' will open the program specified by $EDITOR variable (or vim by default). The next most important commands are testing (t) and submitting (s). A sample workflow is shown in the gif above.
