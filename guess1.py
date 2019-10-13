import random
r = random.randint(1,100)
while True:
	num = input("请输入1到100的整数")
	num = int(num)
	if num == r:
		print("你猜中了!")
		break
	elif num > r:
		print("答案大了")
	else:
		print("答案少了")