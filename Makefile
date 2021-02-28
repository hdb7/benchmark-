CC = gcc
all: binsrch lnsrch
binsrch: binsrch.c 
	${CC} -Wall -Wextra binsrch.c -o binsrch
lnsrch: lnsrch.c 
	${CC} -Wall -Wextra lnsrch.c -o lnsrch
clean:
	@echo "Cleaning all binaries ..."
	rm binsrch lnsrch
