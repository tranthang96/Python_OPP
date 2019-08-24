class HoVaTen:
    def __init__(self, ho_ten, ten_dem, ten):
        self.ho_ten = ho_ten
        self.ten_dem = ten_dem
        self.ten = ten
        self.email = ho_ten + ten_dem + ten +"@gmail.com"
    def hoten(self):
        return '{}{}'.format(self.hoten, self.ten)

ten_1 = HoVaTen("Tran", "Viet", "Thang")
print(ten_1.ho_ten)
print(ten_1.email)

print(ten_1.hoten())




