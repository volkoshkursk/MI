# Description
C++ library for python with custom mutual information calculations. Originally was part of https://github.com/volkoshkursk/NB.

There are two approach to calculate the MI: based on the Pandas framework and based on the custom C++ library. Pandas-based approach is faster, however you need to construct a DataFrame with columns ``` doc_id target token ``` where `token` is the column with only one token in the row. If you have a much data it can be memory-expensive operation. 

From the other hand, the custom library - based approach does not need in some special dataframe. It needs only two iterables with same lengthes: the targets and the textes. However, it is slower than the pandas-based approach.

# Requirements
C++ based approach: You need have `make` and `python-dev` packages installed.
Pandas-based approach: 

# Installation

C++ based approach:

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

Pandas-based approach: