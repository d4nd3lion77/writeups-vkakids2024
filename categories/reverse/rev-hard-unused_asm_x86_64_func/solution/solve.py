#!/bin/python
xored_flag = b'\x8D\x90\x9A\x80\x95\xCF\x88\x96\xa4\xca\x88\xa4\x8f\xcb\xcb\xa4\xc8\xcf\x81\x82\xa4\x9d\xcb\x89\xa4\x88\x8e\x98\x93\xa4\xcf\x95\xa4\xc8\x83\x8b\xc8\x89\xca\xc8\x95\x98\xc8\x9f\xa4\x89\xc8\x8d\xc8\x89\x88\xc8\x89\x86'
flag = ''
for i in xored_flag:
    flag += chr(i ^ 0xfb)
print(flag)