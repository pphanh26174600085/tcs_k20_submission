ma_quan_sat = input("Nhập mã quan sát: ")
gia_tri_do = float(input("Nhập giá trị đo: "))
gia_tri_f = gia_tri_do * 9 / 5 + 32
ten_dai_luong = input("Nhap ten dai luong:")
don_vi = input('Nhap don vi:')
print("Mã quan sát:")
print(ma_quan_sat)
print("Giá trị đo:")
print(gia_tri_do)
print("Giá trị sau chuyển đổi:")
print(gia_tri_f)
from datetime import datetime
thoi_diem = datetime.now()
print(thoi_diem)
thoi_diem_text = thoi_diem
print(f"Ma quan sat: {ma_quan_sat}")
print(f"Dai luong: {ten_dai_luong}")
print(f"Gia tri: {gia_tri_do:.2f}{don_vi}")
print(f"Thoi diem: {thoi_diem_text}")
