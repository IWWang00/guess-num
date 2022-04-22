import random

r = random.randint(1, 100)
while True:
	num = int(input('請輸入1到100的任一數字: '))
	if r == num:
		print ('你猜對了')
		break
	elif r > num:
		print('你的數字比答案小')
	elif r < num:
		print('你的數字比答案大') 
