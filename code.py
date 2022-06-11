while True:
	m = input("请输入模式（1.文件转文件码 2.文件码转文件 3.退出）")
	if m=="1":
		with open(input("请输入要打开的文件路径："),"rb") as file:
			with open("output.txt","w") as o:
				o.write(str(file.read()))
		print("写入完成，文件码在output.txt")
	elif m=="2":
		with open(input("请输入要保存的文件路径："),"wb") as file:
			exec("file.write({})".format(input("请输入文件码：")))
	elif m=="3":
		exit()