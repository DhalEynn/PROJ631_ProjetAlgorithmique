ifeq ($(OS),Windows_NT)
  libs= -lSDL2 -lSDL2main
else
  libs= -lSDL2
endif
EXEC = bin/project

GGDB = -Wall -ggdb
paramC = -std=c++11 -Wall -c

OBJ = obj/main.o

HEADER= src/Case.h src/Jeu_Dames.h

all: $(EXEC)

bin/project: src/main.cpp $(OBJ)
	g++ $(GGBD) src/main.cpp $(OBJ) -o bin/console $(libs)

obj/%.o: src/%.cpp $(HEADER)
	g++ $(paramC) $< -o $@

ifeq ($(OS),Windows_NT)
clean:
	del /f obj\*.o

veryclean: clean
	del /f bin\*.exe
else
clean:
	rm obj/*.o

veryclean:
	rm bin/console bin/graphique bin/test
	make clean
endif
