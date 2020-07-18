#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

void plsgivemeshell() {
    system("/bin/sh");
}

void lulz() {
    char buf[64] = {"this function is only here for the lulz."};
    puts(buf);
}

void vuln() {
    char buf[123];
    unsigned int nb;
    
    puts("How many bytes do you want to read?");
    scanf("%u", &nb);
    
    puts("ok.");
    read(STDIN_FILENO, buf, nb);
}

int main() {
    setvbuf(stdin, 0, _IONBF, 0);
    setvbuf(stdout, 0, _IONBF, 0);
    
    puts("Latest security enabled!!!!");
    vuln();
    return 0;
}
