import os
w = '\x1b[1;37m'
b = '\x1b[1;36m'
g = '\x1b[1;32m'
y = '\x1b[1;33m'
r = '\x1b[1;31m'

def banner():
	os.system('clear')
	print(f'''{b}╔╦╗┬ ┬┬ ┌┬┐┬   ╔╗ ╔═╗
║║║│ ││  │ │───╠╩╗╠╣
╩ ╩└─┘┴─┘┴ ┴   ╚═╝╚{r} v0.2
{b}╔═════════════════════════════════════════╗
{b}║{y}*{g} Author{w} :{g} UPIL KOCLOK             {b}      ║
{b}║{y}*{b} Github{w} :{b} \x1b[4mhttps://github.com/aryhas\x1b[0m{b}     ║
{b}╚═════════════════════════════════════════╝ ''')
