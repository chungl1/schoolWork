OBJS = dot.o matvec.o matmat.o checkres.o fillrand.o

all: main main2
main: main.o $(OBJS)
	$(CC) -o $@ $?
main2: main2.o $(OBJS)
	$(CC) -o $@ $?
clean:
	rm *.o main main2 
