#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 32

signed char array[MAX_SIZE];

int main() {
    setvbuf(stdin, 0, _IONBF, 0);
    setvbuf(stdout, 0, _IONBF, 0);

    printf("(THE_BYTEARRAY_CHALLENGE]\n");
    for(;;) {
        int index;
        signed char value;
        
        printf("which index?\n> ");
        if (scanf("%d", &index) != 1)
            exit(-1);

        if (index >= MAX_SIZE)
            continue;

        printf("the byte at index %d is %hhd.\nprovide a new value.\n> ", index, array[index]);
        if (scanf("%hhd", &value) != 1)
            exit(-1);

        array[index] = value;

	printf("done. the new value is %hhd.\n", value);
    }
}

