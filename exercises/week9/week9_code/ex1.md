### ex 1 

## About 
* about stack canaries 
* about buffer overflow 
* about aslr (or no aslr haha)

## how did it go 
1. you could overflow a buffer but then the program would crash because the stack "smashed"
2. it was a stack canary that was implemented in the client() function 
```C

void client(int client_input_file_descriptor)

{
  ssize_t number_of_bytes;
  long offset;
  undefined buf [72];
  long stack_canary;
  
                    /* save value from data type long at the adress of in_FS_OFFSET + 0x28 in a
                       local variable. 0x28 (hex) = 40 (dec) */
  stack_canary = *(long *)(offset + 0x28);
                    /* ssize_t read(int fd, void *buf, size_t count);
                       read() attempts to read up to count bytes from file descriptor fd into the
                       buffer starting at buf. 0x400 (hex) = 1024 (dec)
                        */
  number_of_bytes = read(client_input_file_descriptor,buf,0x400);
  printf("Server received %u bytes\n",number_of_bytes);
                    /* check if stack canary is still the same
                        */
  if (stack_canary == *(long *)(offset + 0x28)) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}
```
3. You could find the stack canary by bruteforcing it
* you needed to brute force one byte at a time
* in a stack canary the first byte is always the zero byte \x00
* then there were 7 to go 
* you write a little loop that goes over all 2⁸ possible combinations of 8 bits which is 1 byte (same as range 1,255)
* you transform the number you have into a byte and tried to append it to the filled buffer
* the buffer had 72 size so you would put 72 * b'A' + <byte>
* then you needed an outer loop to do this 7 times and always append the found bytes to the payload string

4. After you had the stack canary, you needed to place the address of the plsgivemeshell function on the return address 
* see the client code again, there is a "return" that is reached when the stack canary is correct
* in the stack it looks like this: first the buffer, then the canary and then the return address
* in your local binary you could find the plsgivemeshell() address with ghidra: 00101440
* This is not how the address looks in the system: there it is 40141000 and there are more 0-bytes after: 0000000000101440
* so in the system it actually is  4014100000000000
* this representation of number is like this: Every two numbers are one byte 
* so e.g. 40 is one byte, 14 is one byte (this is only in the system like that, e.g. in Ascii is one byte 1 letter/1 number)
* we look for the second lowest byte which is on the left in the system-like numberorder: so 14 is the second lowest byte
* this is the one, that is not the same like locally 
* the 40 is the same because it is the lowest byte (the lowest 8 bits) and aslr does not change it, so it will be the same remote as it is locally 
* since the address starts with 40 we will send the 40 and then append our brute forced second byte 
* therefore we write another four loop (exploit.py) to find this one 
* also we need to put the stack canary twice in front of it, cause there are 8bytes that seperate the stack canary from the return address (we just overwrite them, nobody cares)
* the flag is in on of the attempts after byte 70 

## other good knowledge: 
* in x64 are all addresses 8 byte (64bit)
* in x86 are all addresses 4 byte (32bit)