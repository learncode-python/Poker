import random, emoji, os, sys
from time import sleep

tottaruh=[]
print('Selamat Datang di meja Poker')
tottar = random.randint(1,50000000)
print('Total taruhan : %s' % tottar)
ask = input('Kamu mau ikut? ')
card = [':heart_suit:',':spade_suit:',':diamond_suit:',':club_suit:']
a = random.choice(card)
b = emoji.emojize(a)
c = random.randint(1,10)
#second card
card2 = [':heart_suit:',':spade_suit:',':diamond_suit:',':club_suit:']
e = random.choice(card2)
f = emoji.emojize(e)
g = random.randint(1,10)
chip = random.randint(1,1000000000)
if ask:
	totl = chip - tottar
	print('Selamat Kamu telah bergabung')
if ask == 'tidak':
	exit('Sampai jumpa')
print('Kartu kamu : %s' % c,b,g,f)
print('Chip kamu : %a' % totl)

#bandar
card = [':heart_suit:',':spade_suit:',':diamond_suit:',':club_suit:']
card2 = [':heart_suit:',':spade_suit:',':diamond_suit:',':club_suit:']
card3 = [':heart_suit:',':spade_suit:',':diamond_suit:',':club_suit:']
ran = random.choice(card)
ran2 = random.choice(card2)
ran3 = random.choice(card3)

cd = emoji.emojize(ran)
cd2 = emoji.emojize(ran2)
cd3 = emoji.emojize(ran3)
r1 = random.randint(1,10)
r2 = random.randint(1,10)
r3 = random.randint(1,10)
print('bandar mengeluarkan kartu : %s' % r1,cd,r2,cd2,r3,cd3)

raise_chip = input('Mau raise? ')
if raise_chip == 'iya':
	brp = int(input('Berapa? '))
	if brp:
		num = chip - brp
		chipbot = random.randint(1,100000000)
		num1 = chipbot - brp
		sleep(2)
		print('Bot Ikut')
		tottar = num + num1
		tottaruh.append(tottar)
		print('Total taruhan : %a' % tottaruh[:1])
	else:
		os.system('python poker.py')
else:
	os.system('python poker.py')
#bot

if c and g == r1:
	sleep(3)
	print('Kamu menang')
	sys.exit('Chip yg kamu dapat : %a' % tottaruh[:1])
elif c and g == r2:
	sleep(3)
	print('Kamu menang')
	sys.exit('Chip yg kamu dapat : %a' % tottaruh[:1])
elif c and g == r3:
	sleep(3)
	print('Kamu menang')
	sys.exit('Chip yang kamu dapat : %a' % tottaruh[:1])
else:
	sleep(3)
	sys.exit('Bot menang')
