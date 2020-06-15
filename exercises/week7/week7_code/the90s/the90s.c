#include <asm/unistd.h>
#include <string.h>

unsigned long __attribute__((naked)) syscall() {
    __asm__(
        "movq %rdi, %rax \n\t"
        "movq %rsi, %rdi\n\t"
        "movq %rdx, %rsi\n\t"
        "movq %rcx, %rdx\n\t"
        "movq %r8, %r10\n\t"
        "movq %r9, %r8\n\t"
        "movq 8(%rsp),%r9\n\t"
        "syscall\n\t"
        "ret\n\t"
    );
}

int main() {
    char buf[64];
    syscall(__NR_write, 1, "Are we in 2004 yet?:\n", 21);
    syscall(__NR_read, 0, buf, 512);
    return 0;
}

void _start() {
    syscall(__NR_exit_group, main());
}
