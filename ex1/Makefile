CC=gcc
CFLAGS= -Wl,-z,norelro -fno-toplevel-reorder -no-pie -fcf-protection=none
NFILE=./vuln1

.PHONY: all say_hello generate clean
all: say_hello generate

say_hello:
	@echo "Hello World"

generate:
	@echo "Build vuln program"
	$(CC) $(CFLAGS) -o $(NFILE) $(NFILE).c
clean:
	@echo "Cleaning up"
	rm $(NFILE)

