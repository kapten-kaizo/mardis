## mardis
Great marshal python2 decompiler++
## what's new?
The latest version supports decompilation in memory, no longer involving system commands. and added `multiexec` decompilation, because previously the tool would stop when it got more than 1 `exec` words.
## quick install
here I run this tool using the Termux system. If the system you use is different, the installation may be different. but what is needed remains the same.
needs
- python2.7
- py-module: uncompyle6==3.7.4
- py-module: xdis==5.0.11
````bash
$ apt install python2 git
$ git clone https://github.com/kapten-kaizo/mardis
$ cd mardis
$ python2 -m pip install xdis==5.0.11
$ python2 -m pip install uncompyle6==3.7.4
````
now you can run with the command 
````bash
$ python2 mardis.py
Usage: mardis [filename|output]

filename = the file you want to decompile
output = For files that store decompilation results, the default is `mardis_result.py`
````
go [here](https://youtu.be/dLtvt1Iq-rQ?si=iKJKnaxRuNV9evVQ) for tutorials on YouTube
