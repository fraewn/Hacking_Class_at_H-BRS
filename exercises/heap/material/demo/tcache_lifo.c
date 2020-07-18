#include <stdlib.h>

//  pwndbg> tcache
//  {
//    counts = {0 <repeats 64 times>},
//    entries = {0x0 <repeats 64 times>}
//  }
//  
//  after free(a):
//  
//  pwndbg> tcache
//  {
//    counts = {1, 0 <repeats 63 times>},
//    entries = {0x4052a0, 0x0 <repeats 63 times>}
//  }
//  
//  after free(b):
//  
//  pwndbg> tcache
//  {
//    counts = {2, 0 <repeats 63 times>},
//    entries = {0x4052c0, 0x0 <repeats 63 times>}
//  }
//  
//  notice: the counts changed... and the pointer got updated...
//  you will just see the last entry that has been added to the list
//  
//  after free(c):
//  
//  pwndbg> tcache
//  {
//    counts = {2, 1, 0 <repeats 62 times>},
//    entries = {0x4052c0, 0x4052e0, 0x0 <repeats 62 times>}
//  }
//  
//  after free() calls:
//  
//  pwndbg> bins
//  tcachebins
//  0x20 [  2]: 0x4052c0 —▸ 0x4052a0 ◂— 0x0
//  0x30 [  1]: 0x4052e0 ◂— 0x0
//  fastbins
//  0x20: 0x0
//  0x30: 0x0
//  0x40: 0x0
//  0x50: 0x0
//  0x60: 0x0
//  0x70: 0x0
//  0x80: 0x0
//  unsortedbin
//  all: 0x0
//  smallbins
//  empty
//  largebins
//  empty
//  
//  after malloc(1):
//  
//  pwndbg> bins
//  tcachebins
//  0x20 [  1]: 0x4052a0 ◂— 0x0
//  0x30 [  1]: 0x4052e0 ◂— 0x0
//  
//  after malloc(25):
//  
//  pwndbg> bins
//  tcachebins
//  0x20 [  1]: 0x4052a0 ◂— 0x0
//  
//  ...
//
//  pwndbg> x/3i $pc
//  => 0x4011c5 <main+143>:	mov    eax,0x0
//     0x4011ca <main+148>:	leave
//     0x4011cb <main+149>:	ret
//
//  pwndbg> bins
//  tcachebins
//  empty

int main(int argc, char **argv)
{
	void *a, *b, *c;

	a = malloc(24);  // next multiple of 16 is 32 -> 32 (0x20) bytes
	b = malloc(8);   // next multiple of 16 and min. 32 bytes -> 32 (0x20) bytes
	c = malloc(40);  // next multiple of 16 is 48 -> 48 (0x30) bytes

	// LIFO - last in first out
	free(a);  // tcache list for 0x20 bytes
	free(b);  // tcache list for 0x20 bytes
	free(c);  // tcache list for 0x30 bytes

	// tcache[0x20]: -> b -> a
	// tcache[0x30]: -> c

	malloc(1);  // allocates 0x20 bytes -> get b
	malloc(25); // allocates 25+8 = 33 bytes for the chunk; 33 > 32 -> get c
	malloc(40); // no fitting chunk in tcache -> get new chunk d
	malloc(24); // allocates 24+8 = 32 bytes for the chunk -> get a
	malloc(8);  // allocate 32 bytes -> get new chunk e

	return 0;
}

