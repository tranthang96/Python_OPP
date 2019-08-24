# cac phuong thuc dac biet trong python
"""Phương thức đặc biệt, tiếng Anh là Special method, đôi lúc người ta còn gọi là Magic method hoặc 
Dunder method. Những phương thức này đã được quy ước sẵn tên. Định dạng chung của các phức thức này 
là __tên phương thức __. Và chúng ta đã tìm hiểu một special method rồi đấy. Nếu bạn đọc chưa nhớ ra 
thì đó chính là hàm constructor của chúng ta. Nó cũng là một special method
https://docs.python.org/3/reference/datamodel.html#special-method-names
"""
a=3
b=2
c=a.__add__(b)
class SieuNhan:
    suc_manh = 50
    def __init__(self, para_ten, para_vu_khi, para_mau_sac):
        self.ten = para_ten
        self.vu_khi = para_vu_khi
        self.mau_sac = para_mau_sac
    def __str__(self):
    	return 'Day la {}, su dung {}'.format(self.ten, self.vu_khi)
    def __repr__(self):
    	return 'ten: {}\nvu khi: {}\nmau sac: {}'.format(self.ten, self.vu_khi, self.mau_sac)

SN_A = SieuNhan('Sieu nhan Do', 'Kiem', 'Do')
print(SN_A)   #uu tien __str__
print('%s' %SN_A)
print('%r' %SN_A)