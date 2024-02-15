# -*- coding: UTF-8 -*-.
import sys, argparse, zlib, marshal, base64, codecs, binascii, time
from os import system, remove
import os
from sys import argv
from random import choice, shuffle
from py_compile import compile as com_pyc
from pprint import pformat
m = '\x1b[1;31m'
k = '\x1b[1;33m'
h = '\x1b[1;32m'
b = '\x1b[1;34m'
bm = '\x1b[1;36m'
ab = '\x1b[1;30m'
p = '\x1b[1;37m'
res  = "\033[1;0m"
hi = "\033[0;30m"
hitam  = "\033[1;30m"
merah1 = "\033[0;31m" 
merah = "\033[1;31m"
hijau2 = "\033[0;32m"
hijau = "\033[1;32m"
emas = "\033[0;33m"
kuning = "\033[1;33m"
bir = "\033[0;34m"  
biru = "\033[1;34m"
purp = "\033[0;35m"
purple  = "\033[1;35m"
cyan1 = "\033[0;36m"
cyan = "\033[1;36m"
abu2 = "\033[0;37m"
putih = "\033[1;37m"
kur1 = "\033[1;31m"+"["
kur2 = "\033[1;31m"+"]"

__banner__=(f"""{biru}

   {p}TOOLS {h}COMPILE {b}AND {h}OBFUSCATE 		      {p}V.1.0
{b}============================================================
   {p}Autor    : {b}shoaibhassana
   {p}github   : {b}https://github.com/shoaibhassan0
{b}============================================================  	
╔═╗┬ ┬┌┬┐┬ ┬┌─┐┌┐┌    
{p}╠═╝└┬┘ │ ├─┤│ ││││ {p}3.8/3.9   
╩   ┴  ┴ ┴ ┴└─┘┘└┘  """)


class TextRun(object):

	def __init__(self, string):
		for i in string + '\n':
			sys.stdout.write(str(i))
			sys.stdout.flush()
			time.sleep(5e-05)


class MainCompile:

	def __init__(self):
		self.puki = []
		self.pico = []
		self.chos = '1234567890'
		self.lisi = 'abcdefghijklmnopqrdtuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
		self.mars = "# Obfuscated by shoaib hassan\n# https://github.com/shoaibhassan0/obfuscator_hard\nexec(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 39, 109, 97, 114, 115, 104, 97, 108, 39, 41, 46, 108, 111, 97, 100, 115],chr))(%s))"
		self.mars_zli = "# Obfuscated by shoaib hassan\n# https://github.com/shoaibhassan0/obfuscator_hard\nexec(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 39, 109, 97, 114, 115, 104, 97, 108, 39, 41, 46, 108, 111, 97, 100, 115],chr))(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 122, 108, 105, 98, 34, 41, 46, 100, 101, 99, 111, 109, 112, 114, 101, 115, 115],chr))(%s)))"
		self.mzb = "# Obfuscated by shoaib hassan\n# https://github.com/shoaibhassan0/obfuscator_hard\nexec(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 39, 109, 97, 114, 115, 104, 97, 108, 39, 41, 46, 108, 111, 97, 100, 115],chr))(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 122, 108, 105, 98, 34, 41, 46, 100, 101, 99, 111, 109, 112, 114, 101, 115, 115],chr))(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 98, 97, 115, 101, 54, 52, 34, 41, 46, 98, 54, 52, 100, 101, 99, 111, 100, 101],chr))(%s))))"
		self.ba32 = '# Obfuscated by shoaib hassan\n# https://github.com/shoaibhassan0/obfuscator_hard\nexec((lambda _____, ______ : ______(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))(\'\',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 98, 97, 115, 101, 54, 52, 34, 41, 46, 98, 51, 50, 100, 101, 99, 111, 100, 101],chr))(_____),"<shoaib>","exec"))(%s,compile))'
		self.ba16 = '# Obfuscated by shoaib hassan\n# https://github.com/shoaibhassan0/obfuscator_hard\nexec((lambda _____, ______ : ______(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))(\'\',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 98, 97, 115, 101, 54, 52, 34, 41, 46, 98, 49, 54, 100, 101, 99, 111, 100, 101],chr))(_____),"<shoaib>","exec"))(%s,compile))'
		self.ba64 = '# Obfuscated by shoaib hassan\n# https://github.com/shoaibhassan0/obfuscator_hard\nexec((lambda _____, ______ : ______(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))(\'\',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 98, 97, 115, 101, 54, 52, 34, 41, 46, 98, 54, 52, 100, 101, 99, 111, 100, 101],chr))(_____),"<shoaib>","exec"))(%s,compile))'
		self.zili = '# Obfuscated by shoaib hassan\n# https://github.com/shoaibhassan0/obfuscator_hard\nexec((lambda _____, ______ : ______(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))(\'\',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 122, 108, 105, 98, 34, 41, 46, 100, 101, 99, 111, 109, 112, 114, 101, 115, 115],chr))(_____),"<shoaib>","exec"))(%s,compile))'
		self.enco = '# Obfuscated by shoaib hassan\n# https://github.com/shoaibhassan0/obfuscator_hard\nexec((lambda __, _, : _(%s,__))("%s",__import__(\'codecs\').decode))'
		self.males = "# Obfuscated by shoaib hassan\n# https://github.com/shoaibhassan0/obfuscator_hard\nexec(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 39, 109, 97, 114, 115, 104, 97, 108, 39, 41, 46, 108, 111, 97, 100, 115],chr))(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 98, 105, 110, 97, 115, 99, 105, 105, 34, 41, 46, 117, 110, 104, 101, 120, 108, 105, 102, 121],chr))(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 98, 97, 115, 101, 54, 52, 34, 41, 46, 98, 49, 54, 100, 101, 99, 111, 100, 101],chr))(%s))))"
		self.Main()

	def Main(self):
		os.system('clear' if os.name == 'posix' else 'cls')
		print(__banner__)
		TextRun(f"{b}❚█══[{p}01{b}]{p}══█❚ {b}Compile To Pyc\n{b}❚█══[{p}02{b}]{p}══█❚ {b}Compile To Zlib\n{b}❚█══[{p}03{b}]{p}══█❚ {b}Compile To Base85\n{b}❚█══[{p}04{b}]{p}══█❚ {b}Compile To Base64\n{b}❚█══[{p}05{b}]{p}══█❚ {b}Compile To Base32\n{b}❚█══[{p}06{b}]{p}══█❚ {b}Compile To Base16\n{b}❚█══[{p}07{b}]{p}══█❚ {b}Compile To Marshal\n{b}❚█══[{p}08{b}]{p}══█❚ {b}Compile To Marshal,Zlib\n{b}❚█══[{p}09{b}]{p}══█❚ {b}Compile To Marshal,Zlib,Base64\n{b}❚█══[{p}10{b}]{p}══█❚ {p}Encode To Bz2_Codec\n{b}❚█══[{p}11{b}]{p}══█❚ {p}Encode To Uu_Codec\n{b}❚█══[{p}12{b}]{p}══█❚ {p}Encode To Cp037\n{b}❚█══[{p}13{b}]{p}══█❚ {p}Encode To Cp424\n{b}❚█══[{p}14{b}]{p}══█❚ {p}Encode To Cp500\n{b}❚█══[{p}15{b}]{p}══█❚ {p}Encode To Cp875\n{b}❚█══[{p}16{b}]{p}══█❚ {p}Encode To Cp1026\n{b}❚█══[{p}17{b}]{p}══█❚ {p}Encode To Rot_13\n{b}❚█══[{p}18{b}]{p}══█❚ {p}Encode To Utf-16\n{b}❚█══[{p}19{b}]{p}══█❚ {p}Encode To Utf-32\n{b}❚█══[{p}20{b}]{p}══█❚ {p}Encode To Utf-32_le\n{b}❚█══[{p}21{b}]{p}══█❚ {p}Encode To Utf-16_be\n{b}❚█══[{p}22{b}]{p}══█❚ {k}Simple Obfuscate (1)\n{b}❚█══[{p}CTRL + C {b}]{p}===➣ {m}Exit Tools\n{p}{putih}▀▄▀▄▀{biru}▄▀▄▀{putih}▄▀▄▀{b}▄▀▄▀▄{p}▀▄▀▄▀{b}▄▀▄▀▄{p}▀▄▀▄▀{b}▄▀▄▀▄▀▄{p}▀▄▀▄▀▄▀▄▀{b}▄▀▄▀▄▀▄▀▄▀▄")
		try:
			inp = int(input(f"{b}[{p}❚█════█❚{b}] {p}Choose {m}: {p}"))
			if inp == 1:
				file = input(f"{b}[{p}!{b}]{p} Input File : ")
				com_pyc(file, file + 'c')
				print(f"{b}[{p}!{b}]{p} succses!, saved to {b}{file}c")
				input(f"{b}[{p}!{b}]{p} back")
				self.Main()
			elif inp == 2:
				komter = 0
				file = input(f"{b}[{p}!{b}]{p} Input File : ")
				total = int(input(f"{b}[{p}!{b}]{p} Count  : "))
				if ( total < 300 ):
					out = input(f"{b}[{p}!{b}]{p} Output File : ")
					xos = open(file).read()
					cum = repr(zlib.compress(xos.encode('utf-8')))
					f = open(out, 'w')
					f.write(self.zili % cum)
					f.close()
					while ( total >= komter ):
						sui = open(out).read()
						ses = repr(zlib.compress(sui.encode('utf-8')))
						f = open(out, 'w')
						f.write(self.zili % ses)
						f.close()
						print(f"{b}[{p}~{b}] {p}Obfuscating File At {b}{komter}")
						komter += 1
					print(f"{b}[{p}!{b}]{p} succses !, saved to ->> ``{out}``")
					input(f"{b}[{p}!{b}]{p} back !!")
					self.Main()
				exit(f"{b}[{p}!{b}]{p}you must input Count < {b}300")
			elif inp == 4:
				komter = 0
				file = input(f"{b}[{p}!{b}]{p} Input File : ")
				total = int(input(f"{b}[{p}!{b}]{p} Count  : "))
				if ( total < 300 ):
					out = input(f"{b}[{p}!{b}]{p} Output File : ")
					xos = open(file).read()
					cum = repr(base64.b64encode(xos.encode('utf-8')))
					f = open(out, 'w')
					f.write(self.ba64 % cum)
					f.close()
					while ( total >= komter ):
						sui = open(out).read()
						ses = repr(base64.b64encode(sui.encode('utf-8')))
						f = open(out, 'w')
						f.write(self.ba64 % ses)
						f.close()
						print(f"{b}[{p}~{b}] {p}Obfuscating File At {b}{komter}")
						komter += 1
					print(f"{b}[{p}!{b}]{p} succses !, saved to ->> ``{out}``")
					input(f"{b}[{p}!{b}]{p} back !!")
					self.Main()
				exit(f"{b}[{p}!{b}]{p} you must input Count < {b}300")
			elif inp == 5:
				komter = 0
				file = input(f"{b}[{p}!{b}]{p} Input File : ")
				total = int(input(f"{b}[{p}!{b}]{p} Count  : "))
				if ( total < 300 ):
					out = input(f"{b}[{p}!{b}]{p} Output File : ")
					xos = open(file).read()
					cum = repr(base64.b32encode(xos.encode('utf-8')))
					f = open(out, 'w')
					f.write(self.ba32 % cum)
					f.close()
					while ( total >= komter ):
						sui = open(out).read()
						ses = repr(base64.b32encode(sui.encode('utf-8')))
						f = open(out, 'w')
						f.write(self.ba32 % ses)
						f.close()
						print(f"{b}[{p}~{b}] {p}Obfuscating File At {b}{komter}")
						komter += 1
					print(f"{b}[{p}!{b}]{p} succses !, saved to ->> ``{out}``")
					input(f"{b}[{p}!{b}]{p} back !!")
					self.Main()
				exit(f"{b}[{p}!{b}]{p} you must input Count < {b}300")
			elif inp == 6:
				komter = 0
				file = input(f"{b}[{p}!{b}]{p} Input File : ")
				total = int(input(f"{b}[{p}!{b}]{p} Count  : "))
				if ( total < 300 ):
					out = input(f"{b}[{p}!{b}]{p} Output File : ")
					xos = open(file).read()
					cum = repr(base64.b16encode(xos.encode('utf-8')))
					f = open(out, 'w')
					f.write(self.ba16 % cum)
					f.close()
					while ( total >= komter ):
						sui = open(out).read()
						ses = repr(base64.b16encode(sui.encode('utf-8')))
						f = open(out, 'w')
						f.write(self.ba16 % ses)
						f.close()
						print(f"{b}[{p}~{b}] {p}Obfuscating File At {b}{komter}")
						komter += 1
					print(f"{b}[{p}!{b}]{p} succses !, saved to ->> ``{out}``")
					input(f"{b}[{p}!{b}]{p} back !!")
					self.Main()
				exit(f"{b}[{p}!{b}]{p} you must input Count < {b}300")
			elif inp == 7:
				komter = 0
				file = input(f"{b}[{p}!{b}]{p} Input File : ")
				total = int(input(f"{b}[{p}!{b}]{p} Count  : "))
				if ( total < 300 ):
					out = input(f"{b}[{p}!{b}]{p} Output File : ")
					xos = open(file).read().encode('utf-8')
					xxx = compile(xos, '<shoaib>', 'exec')
					cum = repr(marshal.dumps(xxx))
					f = open(out, 'w')
					f.write(self.mars % cum)
					f.close()
					while ( total >= komter ):
						sui = open(out).read().encode('utf-8')
						sux = compile(sui, '<shoaib>', 'exec')
						ses = repr(marshal.dumps(sux))
						f = open(out, 'w')
						f.write(self.mars % ses)
						f.close()
						print(f"{b}[{p}~{b}] {p}Obfuscating File At {b}{komter}")
						komter += 1
					print(f"{b}[{p}!{b}]{p} succses !, saved to ->> ``{out}``")
					input(f"{b}[{p}!{b}]{p} back !!")
					self.Main()
				exit(f"{b}[{p}!{b}]{p} you must input Count < {b}300")
			elif inp == 8:
				komter = 0
				file = input(f"{b}[{p}!{b}]{p} Input File : ")
				total = int(input(f"{b}[{p}!{b}]{p} Count  : "))
				if ( total < 300 ):
					out = input(f"{b}[{p}!{b}]{p} Output File : ")
					xos = open(file).read().encode('utf-8')
					xxx = compile(xos, '<shoaib>', 'exec')
					cum = repr(zlib.compress(marshal.dumps(xxx)))
					f = open(out, 'w')
					f.write(self.mars_zli % cum)
					f.close()
					while (total  >= komter):
						sui = open(out).read().encode('utf-8')
						sux = compile(sui, '<shoaib>', 'exec')
						ses = repr(zlib.compress(marshal.dumps(sux)))
						f = open(out, 'w')
						f.write(self.mars_zli % ses)
						f.close()
						print(f"{b}[{p}~{b}] {p}Obfuscating File At {b}{komter}")
						komter += 1
					print(f"{b}[{p}!{b}]{p} succses !, saved to ->> ``{out}``")
					input(f"{b}[{p}!{b}]{p} back !!")
					self.Main()
				exit(f"{b}[{p}!{b}]{p} you must input Count < {b}300")
			elif inp == 9:
				komter = 0
				file = input(f"{b}[{p}!{b}]{p} Input File : ")
				total = int(input(f"{b}[{p}!{b}]{p} Count  : "))
				if ( total < 300 ):
					out = input(f"{b}[{p}!{b}]{p} Output File : ")
					xos = open(file).read().encode('utf-8')
					xxx = compile(xos, '<shoaib>', 'exec')
					cum = repr(base64.b64encode(zlib.compress(marshal.dumps(xxx))))
					f = open(out, 'w')
					f.write(self.mzb % cum)
					f.close()
					while ( total >= komter ):
						sui = open(out).read().encode('utf-8')
						sux = compile(sui, '<shoaib>', 'exec')
						ses = repr(base64.b64encode(zlib.compress(marshal.dumps(sux))))
						f = open(out, 'w')
						f.write(self.mzb % ses)
						f.close()
						print(f"{b}[{p}~{b}] {p}Obfuscating File At {b}{komter}")
						komter += 1
					print(f"{b}[{p}!{b}]{p} succses !, saved to ->> ``{out}``")
					input(f"{b}[{p}!{b}]{p} back !!")
					self.Main()
				exit(f"{b}[{p}!{b}]{p} you must input Count < {b}300")
			elif inp == 10:
				komter = 0
				file = input(f"{b}[{p}!{b}]{p} Input File : ")
				total = int(input(f"{b}[{p}!{b}]{p} Count  : "))
				if ( total < 300 ):
					out = input(f"{b}[{p}!{b}]{p} Output File : ")
					xos = open(file).read().encode('utf-8')
					cum = repr(codecs.encode(xos, 'bz2_codec'))
					f = open(out, 'w')
					f.write(self.enco % (cum, 'bz2_codec'))
					f.close()
					while ( total >= komter ):
						sui = open(out).read().encode('utf-8')
						ses = repr(codecs.encode(sui, 'bz2_codec'))
						f = open(out, 'w')
						f.write(self.enco % (
											 ses,
										 'bz2_codec'))
						f.close()
						print(f"{b}[{p}~{b}] {p}Obfuscating File At {b}{komter}")
						komter += 1
					print(f"{b}[{p}!{b}]{p} succses !, saved to ->> ``{out}``")
					input(f"{b}[{p}!{b}]{p} back !!")
					self.Main()
				exit(f"{b}[{p}!{b}]{p} you must input Count < {b}300")
			elif inp == 11:
				komter = 0
				file = input(f"{b}[{p}!{b}]{p} Input File : ")
				total = int(input(f"{b}[{p}!{b}]{p} Count  : "))
				if ( total < 300 ):
					out = input(f"{b}[{p}!{b}]{p} Output File : ")
					xos = open(file).read().encode('utf-8')
					cum = repr(codecs.encode(xos, 'uu_codec'))
					f = open(out, 'w')
					f.write(self.enco % (cum, 'uu_codec'))
					f.close()
					while ( total >= komter ):
						sui = open(out).read().encode('utf-8')
						ses = repr(codecs.encode(sui, 'uu_codec'))
						f = open(out, 'w')
						f.write(self.enco % (
										 ses,
										 'uu_codec'))
						f.close()
						print(f"{b}[{p}~{b}] {p}Obfuscating File At {b}{komter}")
						komter += 1
					print(f"{b}[{p}!{b}]{p} succses !, saved to ->> ``{out}``")
					input(f"{b}[{p}!{b}]{p} back !!")
					self.Main()
				exit(f"{b}[{p}!{b}]{p} you must input Count < {b}300")
			elif inp == 12:
				komter = 0
				file = input(f"{b}[{p}!{b}]{p} Input File : ")
				total = int(input(f"{b}[{p}!{b}]{p} Count  : "))
				if ( total < 300 ):
					out = input(f"{b}[{p}!{b}]{p} Output File : ")
					xos = open(file).read()
					cum = repr(codecs.encode(xos, 'cp037'))
					f = open(out, 'w')
					f.write(self.enco % (cum, 'cp037'))
					f.close()
					while ( total >= komter ):
						sui = open(out).read()
						ses = repr(codecs.encode(sui, 'cp037'))
						f = open(out, 'w')
						f.write(self.enco % (ses,
										 'cp037'))
						f.close()
						print(f"{b}[{p}~{b}] {p}Obfuscating File At {b}{komter}")
						komter += 1
					print(f"{b}[{p}!{b}]{p} succses !, saved to ->> ``{out}``")
					input(f"{b}[{p}!{b}]{p} back !!")
					self.Main()
				exit(f"{b}[{p}!{b}]{p} you must input Count < {b}300")
			elif inp == 13:
				komter = 0
				file = input(f"{b}[{p}!{b}]{p} Input File : ")
				total = int(input(f"{b}[{p}!{b}]{p} Count  : "))
				if ( total < 300 ):
					out = input(f"{b}[{p}!{b}]{p} Output File : ")
					xos = open(file).read()
					cum = repr(codecs.encode(xos, 'cp424'))
					f = open(out, 'w')
					f.write(self.enco % (cum, 'cp424'))
					f.close()
					while ( total >= komter ):
						sui = open(out).read()
						ses = repr(codecs.encode(sui, 'cp424'))
						f = open(out, 'w')
						f.write(self.enco % (ses,
										 'cp424'))
						f.close()
						print(f"{b}[{p}~{b}] {p}Obfuscating File At {b}{komter}")
						komter += 1
					print(f"{b}[{p}!{b}]{p} succses !, saved to ->> ``{out}``")
					input(f"{b}[{p}!{b}]{p} back !!")
					self.Main()
				exit(f"{b}[{p}!{b}]{p} you must input Count < {b}300")
			elif inp == 14:
				komter = 0
				file = input(f"{b}[{p}!{b}]{p} Input File : ")
				total = int(input(f"{b}[{p}!{b}]{p} Count  : "))
				if ( total < 300 ):
					out = input(f"{b}[{p}!{b}]{p} Output File : ")
					xos = open(file).read()
					cum = repr(codecs.encode(xos, 'cp500'))
					f = open(out, 'w')
					f.write(self.enco % (cum, 'cp500'))
					f.close()
					while ( total >= komter ):
						sui = open(out).read()
						ses = repr(codecs.encode(sui, 'cp500'))
						f = open(out, 'w')
						f.write(self.enco % (ses,
										 'cp500'))
						f.close()
						print(f"{b}[{p}~{b}] {p}Obfuscating File At {b}{komter}")
						komter += 1
					print(f"{b}[{p}!{b}]{p} succses !, saved to ->> ``{out}``")
					input(f"{b}[{p}!{b}]{p} back !!")
					self.Main()
				exit(f"{b}[{p}!{b}]{p} you must input Count < {b}300")
			elif inp == 15:
				komter = 0
				file = input(f"{b}[{p}!{b}]{p} Input File : ")
				total = int(input(f"{b}[{p}!{b}]{p} Count  : "))
				if ( total < 300 ):
					out = input(f"{b}[{p}!{b}]{p} Output File : ")
					xos = open(file).read()
					cum = repr(codecs.encode(xos, 'cp875'))
					f = open(out, 'w')
					f.write(self.enco % (cum, 'cp875'))
					f.close()
					while ( total >= komter ):
						sui = open(out).read()
						ses = repr(codecs.encode(sui, 'cp875'))
						f = open(out, 'w')
						f.write(self.enco % (ses,
										 'cp875'))
						f.close()
						print(f"{b}[{p}~{b}] {p}Obfuscating File At {b}{komter}")
						komter += 1
					print(f"{b}[{p}!{b}]{p} succses !, saved to ->> ``{out}``")
					input(f"{b}[{p}!{b}]{p} back !!")
					self.Main()
				exit(f"{b}[{p}!{b}]{p} you must input Count < {b}300")
			elif inp == 16:
				komter = 0
				file = input(f"{b}[{p}!{b}]{p} Input File : ")
				total = int(input(f"{b}[{p}!{b}]{p} Count  : "))
				if ( total < 300 ):
					out = input(f"{b}[{p}!{b}]{p} Output File : ")
					xos = open(file).read()
					cum = repr(codecs.encode(xos, 'cp1026'))
					f = open(out, 'w')
					f.write(self.enco % (cum, 'cp1026'))
					f.close()
					while ( total >= komter ):
						sui = open(out).read()
						ses = repr(codecs.encode(sui, 'cp1026'))
						f = open(out, 'w')
						f.write(self.enco % (ses,
										 'cp1026'))
						f.close()
						print(f"{b}[{p}~{b}] {p}Obfuscating File At {b}{komter}")
						komter += 1
					print(f"{b}[{p}!{b}]{p} succses !, saved to ->> ``{out}``")
					input(f"{b}[{p}!{b}]{p} back !!")
					self.Main()
				exit(f"{b}[{p}!{b}]{p} you must input Count < {b}300")
			elif inp == 17:
				komter = 0
				file = input(f"{b}[{p}!{b}]{p} Input File : ")
				total = int(input(f"{b}[{p}!{b}]{p} Count  : "))
				if ( total < 300 ):
					out = input(f"{b}[{p}!{b}]{p} Output File : ")
					xos = open(file).read()
					cum = repr(codecs.encode(xos, 'rot_13'))
					f = open(out, 'w')
					f.write(self.enco % (cum, 'rot_13'))
					f.close()
					while ( total >= komter ):
						sui = open(out).read()
						ses = repr(codecs.encode(sui, 'rot_13'))
						f = open(out, 'w')
						f.write(self.enco % (ses,
										 'rot_13'))
						f.close()
						print(f"{b}[{p}~{b}] {p}Obfuscating File At {b}{komter}")
						komter += 1
					print(f"{b}[{p}!{b}]{p} succses !, saved to ->> ``{out}``")
					input(f"{b}[{p}!{b}]{p} back !!")
					self.Main()
				exit(f"{b}[{p}!{b}]{p} you must input Count < {b}300")
			elif inp == 18:
				komter = 0
				file = input(f"{b}[{p}!{b}]{p} Input File : ")
				total = int(input(f"{b}[{p}!{b}]{p} Count  : "))
				if ( total < 300 ):
					out = input(f"{b}[{p}!{b}]{p} Output File : ")
					xos = open(file).read()
					cum = repr(codecs.encode(xos, 'utf-16'))
					f = open(out, 'w')
					f.write(self.enco % (cum, 'utf-16'))
					f.close()
					while ( total >= komter ):
						sui = open(out).read()
						ses = repr(codecs.encode(sui, 'utf-16'))
						f = open(out, 'w')
						f.write(self.enco % (ses,
										 'utf-16'))
						f.close()
						print(f"{b}[{p}~{b}] {p}Obfuscating File At {b}{komter}")
						komter += 1
					print(f"{b}[{p}!{b}]{p} succses !, saved to ->> ``{out}``")
					input(f"{b}[{p}!{b}]{p} back !!")
					self.Main()
				exit(f"{b}[{p}!{b}]{p} you must input Count < {b}300")
			elif inp == 19:
				komter = 0
				file = input(f"{b}[{p}!{b}]{p} Input File : ")
				total = int(input(f"{b}[{p}!{b}]{p} Count  : "))
				if ( total < 300 ):
					out = input(f"{b}[{p}!{b}]{p} Output File : ")
					xos = open(file).read()
					cum = repr(codecs.encode(xos, 'utf-32'))
					f = open(out, 'w')
					f.write(self.enco % (cum, 'utf-32'))
					f.close()
					while ( total >= komter ):
						sui = open(out).read()
						ses = repr(codecs.encode(sui, 'utf-32'))
						f = open(out, 'w')
						f.write(self.enco % (ses,
										 'utf-32'))
						f.close()
						print(f"{b}[{p}~{b}] {p}Obfuscating File At {b}{komter}")
						komter += 1
					print(f"{b}[{p}!{b}]{p} succses !, saved to ->> ``{out}``")
					input(f"{b}[{p}!{b}]{p} back !!")
					self.Main()
				exit(f"{b}[{p}!{b}]{p} you must input Count < {b}300")
			elif inp == 20:
				komter = 0
				file = input(f"{b}[{p}!{b}]{p} Input File : ")
				total = int(input(f"{b}[{p}!{b}]{p} Count  : "))
				if ( total < 300 ):
					out = input(f"{b}[{p}!{b}]{p} Output File : ")
					xos = open(file).read()
					cum = repr(codecs.encode(xos, 'utf-32_le'))
					f = open(out, 'w')
					f.write(self.enco % (cum, 'utf-32_le'))
					f.close()
					while ( total >= komter ):
						sui = open(out).read()
						ses = repr(codecs.encode(sui, 'utf-32_le'))
						f = open(out, 'w')
						f.write(self.enco % (ses,
									 'utf-32_le'))
						f.close()
						print(f"{b}[{p}~{b}] {p}Obfuscating File At {b}{komter}")
						komter += 1
					print(f"{b}[{p}!{b}]{p} succses !, saved to ->> ``{out}``")
					input(f"{b}[{p}!{b}]{p} back !!")
					self.Main()
				exit(f"{b}[{p}!{b}]{p} you must input Count < {b}300")
			elif inp == 21:
				komter = 0
				file = input(f"{b}[{p}!{b}]{p} Input File : ")
				total = int(input(f"{b}[{p}!{b}]{p} Count  : "))
				if ( total < 300 ):
					out = input(f"{b}[{p}!{b}]{p} Output File : ")
					xos = open(file).read()
					cum = repr(codecs.encode(xos, 'utf-16_be'))
					f = open(out, 'w')
					f.write(self.enco % (cum, 'utf-16_be'))
					f.close()
					while ( total >= komter ):
						sui = open(out).read()
						ses = repr(codecs.encode(sui, 'utf-16_be'))
						f = open(out, 'w')
						f.write(self.enco % (ses,
									 'utf-16_be'))
						f.close()
						print(f"{b}[{p}~{b}] {p}Obfuscating File At {b}{komter}")
						komter += 1
					print(f"{b}[{p}!{b}]{p} succses !, saved to ->> ``{out}``")
					input(f"{b}[{p}!{b}]{p} back !!")
					self.Main()
				exit(f"{b}[{p}!{b}]{p} you must input Count < {b}300")
			elif inp == 3:
				komter = 0
				file = input(f"{b}[{p}!{b}]{p} Input File : ")
				total = int(input(f"{b}[{p}!{b}]{p} Count  : "))
				if ( total < 300 ):
					out = input(f"{b}[{p}!{b}]{p} Output File : ")
					xos = open(file).read()
					cum = repr(base64.b85encode(xos.encode()))
					f = open(out, 'w')
					f.write(f"exec((lambda _ : (__import__('base64').b85decode(_)))({cum}))")
					f.close()
					while ( total >= komter ):
						sui = open(out).read()
						ses = repr(base64.b85encode(sui.encode()))
						f = open(out, 'w')
						f.write(f"exec((lambda _ : (__import__('base64').b85decode(_)))({ses}))")
						f.close()
						print(f"{b}[{p}~{b}] {p}Obfuscating File At {b}{komter}")
						komter += 1
					print(f"{b}[{p}!{b}]{p} succses !, saved to ->> ``{out}``")
					input(f"{b}[{p}!{b}]{p} back !!")
					self.Main()
				exit(f"{b}[{p}!{b}]{p} you must input Count < {b}300")
			elif inp == 22:
				data = []
				file = input(f"{b}[{p}!{b}]{p} Input File : ")
				out = input(f"{b}[{p}!{b}]{p} Output File : ")
				TextRun(f"{b}[{p}#{b}]{p} Obfuscating Source..")
				xos = open(file).read()
				for i in xos:
					data.append(ord(i))
					f = open('tmp.py', 'w')
					f.write(f"exec(''.join(chr(_) for _ in {data}))")
					f.close()
				scu = open('tmp.py').read()
				fub = compile(scu, '<shoaib>', 'exec')
				xuc = repr(marshal.dumps(fub))
				s = open(out, 'w')
				s.write(f"exec(__import__('marshal').loads({xuc}))")
				s.close()
				del data[:]
				com_pyc(out, out)
				remove('tmp.py')
				print(f"{b}[{p}!{b}]{p} succses !, saved to ->> ``{out}``")
				input(f"{b}[{p}!{b}]{p} back !!")
				self.Main()
			else:
				exit(f"{b}[{p}!{b}]{p} please open your eyes {m}!{p}")
		except (KeyboardInterrupt,EOFError):
			exit(f"{m}[{p}*{m}]{p} Exit !")
		except ValueError:
			exit(f"{m}[{p}*{m}]{p} You must input number!")
		except FileNotFoundError:
			exit(f"{m}[{p}*{m}]{p} File ``{file}`` files could not be found !")
			

if __name__ == '__main__':
    MainCompile()