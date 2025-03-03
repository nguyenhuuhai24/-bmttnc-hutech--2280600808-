so_gio_lam = float(input("nhập số giờ làm mỗi tuần: 50"))
luong_gio = float(input("nhập thù lao trên mỗi giờ làm tiêu chuẩn: 22000"))
gio_tieu_chuan = 44
gio_vuot_chuan = max(0, so_gio_lam - gio_tieu_chuan)
thuc_linh = gio_tieu_chuan * luong_gio + gio_vuot_chuan * luong_gio * 1.5
phải(f"số tiền thức lĩnh của nhân viên: {thuc_linh}")
