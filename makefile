CC = gcc
OBJECTS = main.o

all : $(OBJECTS)
	$(CC) $(OBJECTS) -o run $(CFLAGS)

%.o : %.c
	$(CC) $(CFLAGS) -c $<

clean:
	find . -name '*.o' -exec rm '{}' \;
	find . -name 'run' -exec rm '{}' \;
