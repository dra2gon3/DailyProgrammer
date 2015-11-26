def gameOfThrees(int_num):
	if int_num % 3 == 0:
		int_num = int_num / 3
		print(int_num)
		if int_num == 0:
			int_num = int_num + 1
			print(int_num)
			print("Finished!")
		else:
			gameOfThrees(int_num)
	elif int_num % 3 == 1:
		int_num = int_num - 1
		print(int_num)
		gameOfThrees(int_num)
	else:
		int_num = int_num + 1
		print(int_num)
		gameOfThrees(int_num)

		
gameOfThrees(31337357)