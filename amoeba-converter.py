# Assembler to machine code for Amoeba

import sys

commands = {
	'LDA':'0000',
	'STA':'0001',
	'LDAN':'0010',
	'ADD':'0011',
	'SUB':'0100',
	'MLT':'0101',
	'DIV':'0110',
	'JF':'0111',
	'JB':'1000',
	'JFE':'1001',
	'JBE':'1010',
	'CLO':'1011',
	'PAN':'1100',
	'PAC':'1101',
	'NOP':'1110',
	'END':'1111'
}

try:
	fn = sys.argv[1]
except IndexError:
	fn = 'program.txt'

with open(fn, 'r') as f:
	out = []
	for line in f.readlines():
		split = line.split(' ')
		cmd = commands[split[0]]
		out.append(cmd + split[1])

with open(fn, 'w') as f:
	for line in out:
		f.write(line)
	f.write('\n')