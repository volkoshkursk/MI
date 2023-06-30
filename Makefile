.PHONY: clean all

# python version
VER ?= 3.8

all: libmi.so

clean:
	rm -rf mi/*.so mi/*.o *.so

mi/mi.o: mi/mi1.c
	gcc -fPIC -c $$(python${VER}-config  --includes) -o mi/mi.o mi/mi1.c

libmi.so: mi/mi.o
	gcc $$(python${VER}-config --ldflags) -lpython${VER} -shared mi/mi.o -o libmi.so
