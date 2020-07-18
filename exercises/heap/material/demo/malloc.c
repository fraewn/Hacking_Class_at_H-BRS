#include <stdlib.h>
#include <stdio.h>

int main(int argc, char **argv)
{
	unsigned int amount = 0;

	while (amount < 0x1000)
	{
		char *temp = (char *)malloc(amount);
		unsigned int chunk_size = *(unsigned int *)(temp - 8) & ~0x7;

		printf("malloc(%u), size=%u; address=%p\n", amount, chunk_size, temp);

		amount += 8;
	}

	return 0;
}

