import random
start = int(input('請決定輸入數字的範圍開始值: '))
end = int(input('請決定輸入數字的範圍結束值: '))
r = random.randint(start, end)
count = 0
while True:
	num = int(input('請猜數字: '))
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