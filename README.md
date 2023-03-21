# Description
C++ library for python with custom mutual information calculations. Originally was part of https://github.com/volkoshkursk/NB.

In this branch will be latest debugged code. 
In branch `nouveau` you can find newest version of project.
# Requirements
You need have `make` and `python-dev` packages installed.

# Installation

You need create libme.so to run this project. 
For this purpose you need installed python3-dev on your system. For building on library *nix system run

```
make clean && make
```

Default Python version is 3.8. If you need build for another version run 

```
make clean && make VER=<ver>
```

where instead `<ver>` should be your version.