FLAGS = -W -O3
# -Wcounterexamples
.PHONY = all clean cleanall

all: kalkulator

kalkulator: kalkulator.y kalkulator.l lib/operacje.h
	bison -o kalkulator_y.c -d kalkulator.y
	flex -o kalkulator_l.c kalkulator.l
	$(CC) $(FLAGS) -o kalkulator kalkulator_y.c kalkulator_l.c

clean:
	rm -f *.c *.h

cleanall: clean
	rm -f  kalkulator

