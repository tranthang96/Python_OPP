#class.py
class Test_1:
	pass
A = Test_1() # A chính là một object lop Test_1
print(A)

# thuộc tính
class SieuNhan:
    pass

sieu_nhan_A = SieuNhan()

sieu_nhan_A.ten = "Sieu nhan do"
sieu_nhan_A.vu_khi = "Kiem"
sieu_nhan_A.mau_sac = "Do"

print("Ten cua sieu nhan la:",sieu_nhan_A.ten)
print("Sieu nhan mau:", sieu_nhan_A.mau_sac)
print("Su dung vu khi:", sieu_nhan_A.vu_khi)
# initialize method
class SieuNhan:
    def __init__(self, para_ten, para_vu_khi, para_mau_sac):
    #self chính là thể hiện của SieuNhan
        self.ten = "Sieu nhan " + para_ten
        self.vu_khi = para_vu_khi
        self.mau_sac = para_mau_sac

sieu_nhan_B = SieuNhan("do", "Kiem", "Do")
print("Ten cua sieu nhan la:",sieu_nhan_B.ten)
print("Sieu nhan mau:", sieu_nhan_B.mau_sac)
print("Su dung vu khi:", sieu_nhan_B.vu_khi)
# self : chính là sieu_nhan_A

