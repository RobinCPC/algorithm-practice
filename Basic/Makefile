###########################################################################
# 				Makefile for CPP code
# Use below comand (in bash) to compile the file you want (such as):
# `make ex2-11`  <-- this command will run
# `g++ -std=c++11 -Wall -pedantic    ex2-11.cpp   -o ex2-11`
#
# for debug:
# `make DEBUG=1 ex2-11`  <-- this command will run
# `g++ -DDEBUG -g -std=c++11 -Wall -pedantic    ex2-11.cpp   -o ex2-11`
# note: `-DDEBUG` will work if there is macro `DEBUG` defined in codes
#
# note: `make all` only work for only one project (contain only one
# fiile with `main`).
# TODO: `all` command did not complete
#
# Reference:
# http://stackoverflow.com/questions/16886591/how-do-i-enable-c11-in-gcc
# http://www.cprogramming.com/tutorial/makefiles_continued.html
# http://www.cs.umd.edu/class/fall2002/cmsc214/Tutorial/makefile.html
#
###########################################################################
DEBUG ?= 0  		# default not use debug mode
ifeq ($(DEBUG), 1)
	FLAGS_OPT = -DDEBUG -g -std=c++11 -Wall -Wextra -Wshadow -Wnon-virtual-dtor \
			  -pedantic -Wreorder -Wwrite-strings
else
	FLAGS_OPT = -std=c++11 -Wall -Wextra -Wshadow -Wnon-virtual-dtor -pedantic \
			   -Wreorder -Wwrite-strings
endif

CXX = g++
CXXFLAGS = $(FLAGS_OPT)


BIN = prog

SRC = $(wildcard *.cpp)
OBJ = $(SRC:%.cpp=%.o)

.PHONY: clean \
		all
###########################################################################
# complieing and linking

all: $(OBJ)
	$(CXX) -o $(BIN) $^


%.o: %.c
	$(CXX) $@ -c $<


###########################################################################
# some useful commands
clean:
	rm -f *.o *~
	rm $(BIN)

# debug
#debug: CXXFLAGS += -DDEBUG -g
#debug: all


###########################################################################
# See Cmake/Makefile for a complete commented sample Makefile,
# illustrating separate compilation and dependencies.

# Running "make" can generate many error messages.  Do
#	make .. >& make.log
# to compile XXX and cause the errors to go into the file make.log.
# When "make" finishes you can read the file with "view", "more", or "less".
#
# Many later error messages can be meaningless because they were caused
# by an earlier error.  Always try to correct errors in order.
#
# Do
#       make .. >& make.log
# to create all executable files.
