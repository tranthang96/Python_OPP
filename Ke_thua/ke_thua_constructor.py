# ke thua ham constructor
class SieuNhan:
    suc_manh = 50
    def __init__(self, para_ten, para_vu_khi, para_mau_sac):
        self.ten = para_ten
        self.vu_khi = para_vu_khi
        self.mau_sac = para_mau_sac

class SieuNhanGao(SieuNhan):
    suc_manh = 40
    def __init__(self, para_ten, para_vu_khi, para_mau_sac, para_su_thu):
        # doi luc nguoi ta cung co the
        # SieuNhan.__init__(para_ten, para_vu_khi, para_mau_sac)
        # nhung dung super van la chu yeu
        super().__init__(para_ten, para_vu_khi, para_mau_sac) #ke thua
        self.su_thu = para_su_thu
# voi python 2x
class SieuNhanDen(SieuNhan):
	"""docstring for SieuNhanDen"""
	def __init__(self, para_ten, para_vu_khi, para_mau_sac, para_mu_bao_hiem, para_su_thu):
		super(SieuNhanDen, self).__init__(para_ten, para_vu_khi, para_mau_sac)
		self.mu_bao_hiem = para_mu_bao_hiem
		self.su_thu = para_su_thu


gao_do = SieuNhanGao("Gao do", "Cung", "Do", "Su tu")
print(gao_do.__dict__)
print(gao_do.suc_manh)

sieunhan_mau_den = SieuNhanDen('Den','kiem','den xi','Ho',"heeee")
print("==========================")
print(sieunhan_mau_den.__dict__)
print(type(sieunhan_mau_den.__dict__))
print(sieunhan_mau_den.suc_manh)