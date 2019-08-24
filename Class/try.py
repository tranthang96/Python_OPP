while 1:
	try:
		dtb = float(input("nhap diem:"))
		if ( dtb>10 or dtb < 0):
			print("Ban da nhap sai(0<diem<10)")
		else:
			break;
	except Exception:
		print("Ban da nhap sai, xin moi nhap lai:")
if dtb>=5:
	print("Bạn đã đậu , Xin chúng mừng")
else:
	print("Bạn đã trượt, Xin chia buồn")