while 1:
	try:
		dtb = float(input("nhap diem:"))
		break;
	except Exception:
		print("Ban da nhap sai, xin moi nhap lai:")
if dtb>=5:
	print("ban da dau")
else:
	print("ban truot")