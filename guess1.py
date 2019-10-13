import random
start = input("请输入随机数字的开始值(整数): ")
end = input("请输入随机数字的结束值(整数): ")
start = int(start)
end = int(end)
r = random.randint(start, end)
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
