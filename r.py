import random

r = random.randint(1, 100)
count = 0
while True:
	num = int(input('請輸入1到100的任一數字: '))
	count += 1
	if r == num:
		print('你猜對了')
		print('這是你猜的', count, '次')
		break
	elif r > num:
		print('你的數字比答案小')
	elif r < num:
		print('你的數字比答案大') 
	print('這是你猜的', count, '次')