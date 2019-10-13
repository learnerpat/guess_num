import random
r = random.randint(1,100)
count = 0
while True:
	count += 1
	num = input("请输入1到100的整数: ")
	num = int(num)
	if num == r:
		print("你猜中了!")
		print("这是你猜的第", count, "次.")
		break
	elif num > r:
		print("答案大了")
	else:
		print("答案少了")
	print("这是你猜的第", count, "次.")
