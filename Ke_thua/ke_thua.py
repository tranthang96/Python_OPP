class SieuNhan():
	sucmanh=50
class SieuNhanDo(SieuNhan):
	pass
print(SieuNhanDo.sucmanh)
# Neu khong muon ke thua tu lop sieu nhan
class SieuNhanXanh(object):
	"""docstring for SieuNhanXanh"""
	sucmanh=40
print(SieuNhanXanh.sucmanh)
print(SieuNhan.sucmanh)  #sucmanh ở lớp siêu nhân gốc không thanh đổi

