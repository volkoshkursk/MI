.PHONY: clean all

# python version
VER ?= 3.8

all: libmi.so

clean:
	rm -rf mi/*.so mi/*.o

mi/mi.o: mi/mi1.cpp 
	g++ -fPIC -c $$(python${VER}-config  --includes) -o mi/mi.o mi/mi1.cpp

libmi.so: mi/mi.o
	g++ $$(python${VER}-config --ldflags) -lpython${VER} -shared mi/mi.o -o libmi.so
