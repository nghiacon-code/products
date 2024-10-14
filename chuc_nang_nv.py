import pandas as pd
import datetime
import re

# Đọc dữ liệu từ file Excel
try:
    data = pd.read_excel(r'data.xlsx')
except Exception as e:
    print(f"Có lỗi khi đọc file Excel: {e}")
    exit()

# Kiểm tra xem cột 'ID' có trong dữ liệu hay không
if 'ID' in data.columns:
    # Chuyển đổi dữ liệu thành từ điển
    nhan_vien = data.set_index('ID').T.to_dict()
else:
    print("Cột 'ID' không tồn tại trong DataFrame.")
    exit()

def xac_nhan():
    while True:
        y_n = input("Bạn có chắc chắn muốn thực hiện hành động này? (Y/N): ").upper()
        if y_n == 'Y':
            return True
        elif y_n == 'N':
            return False
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập Y hoặc N.")

def cc_1():
    start_time = datetime.datetime.now()
    for id, info in nhan_vien.items():
        print("-" * 20)
        print("ID:", id)
        print("Tên:", info['Họ tên'])
        print("-" * 20)
    end_time = datetime.datetime.now()
    print(f"Thời gian thực hiện chức năng 1: {end_time - start_time}")

def cc_2():
    start_time = datetime.datetime.now()
    mnv_tim_kiem = input("Nhập ID nhân viên cần tìm: ").strip().upper()
    mnv_tim_kiem = str(mnv_tim_kiem)

    if mnv_tim_kiem in nhan_vien:
        info = nhan_vien[mnv_tim_kiem]
        print('Thông tin nhân viên có ID: ', mnv_tim_kiem)
        print("Tên:", info['Họ tên'])
        print("Chức danh:", info['Chức danh'])
        print("SĐT:", info['Số điện thoại'])
        print("Email:", info['Email'])
        print("-" * 20)
    else:
        print('Không tìm thấy nhân viên với ID: ', mnv_tim_kiem)
    end_time = datetime.datetime.now()
    print(f"thời gian thực hiện chức năng: {end_time - start_time}")

def cc_3():
    start_time = datetime.datetime.now()
    if xac_nhan():
        id_moi = input("Nhập ID nhân viên mới: ").upper()
        ten_moi = input("Nhập tên nhân viên mới: ")
        chuc_danh_moi = input("Nhập chức danh: ")
        phong_ban_moi = input("Mời nhập phòng ban: ")
        luong_moi = input("Mơi nhập lương: ")
        while True:
                sdt_moi = input("Nhập số điện thoại mới (hoặc nhấn Enter để giữ nguyên): ")
                if sdt_moi:
                    if re.match(r'^\d{10}$', sdt_moi):
                        break
                    else:
                        print("Số điện thoại không đúng định dạng (Số điện thoại có 10 số). Vui lòng nhập lại.")
                else:
                    break

        # Nhập email mới
        while True:
            email_moi = input("Nhập email mới (hoặc nhấn Enter để giữ nguyên): ")
            if email_moi:
                if re.match(r'^[a-zA-Z0-9_]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email_moi):
                    break
                else:
                    print("Email không đúng định dạng (a@gmail.com). Vui lòng nhập lại.")
            else:
                break
        
        # Cập nhật từ điển nhân viên
        print("-" * 20)
        nhan_vien[id_moi] = {
            'Họ tên': ten_moi,
            'Chức danh': chuc_danh_moi,
            'Phòng ban': phong_ban_moi,
            'Số điện thoại': sdt_moi,
            'Email': email_moi,
            'Lương': luong_moi
        }
        print("-" * 20)
        end_time = datetime.datetime.now()
        print(f"Thời gian thực hiện chức năng 1: {end_time - start_time}")
        
        # Chuyển đổi lại từ điển thành DataFrame
        updated_data = pd.DataFrame.from_dict(nhan_vien, orient='index')
        updated_data.index.name = 'ID'
        # Ghi đè lên file Excel
        try:
            updated_data.to_excel(r'data.xlsx', index=True)
            print("Dữ liệu đã được cập nhật thành công trong file Excel.")
        except Exception as e:
            print(f"Có lỗi khi ghi đè file Excel: {e}")


def cc_4():
    if xac_nhan():
        start_time = datetime.datetime.now()
        mnv_cap_nhat = input("Nhập ID của nhân viên muốn cập nhật: ").upper()

        if mnv_cap_nhat in nhan_vien:
            ten_moi = input("Nhập tên mới (hoặc nhấn Enter để giữ nguyên): ")
            chuc_danh_moi = input("Nhập chức danh mới (hoặc nhấn Enter để giữ nguyên): ")   
            luong_moi = input("Nhập lương mới (hoặc nhấn Enter để giữ nguyên): ")

            if ten_moi:
                nhan_vien[mnv_cap_nhat]['Họ tên'] =        ten_moi
            if chuc_danh_moi:
                nhan_vien[mnv_cap_nhat]['Chức danh'] =     chuc_danh_moi
            if luong_moi:
                nhan_vien[mnv_cap_nhat]['Số điện thoại'] = luong_moi
               # Nhập số điện thoại mới
            while True:
                sdt_moi = input("Nhập số điện thoại mới (hoặc nhấn Enter để giữ nguyên): ")
                if sdt_moi:
                    if re.match(r'^\d{10}$', sdt_moi):
                        break
                    else:
                        print("Số điện thoại không đúng định dạng (Số điện thoại có 10 số). Vui lòng nhập lại.")
                else:
                    break

            # Nhập email mới
            while True:
                email_moi = input("Nhập email mới (hoặc nhấn Enter để giữ nguyên): ")
                if email_moi:
                    if re.match(r'^[a-zA-Z0-9_]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email_moi):
                        break
                    else:
                        print("Email không đúng định dạng (a@gmail.com). Vui lòng nhập lại.")
                else:
                    break

            print("Đã cập nhật thông tin nhân viên có ID: " + mnv_cap_nhat )
            end_time = datetime.datetime.now()
            print(f"Thời gian thực hiện chức năng 1: {end_time - start_time}")
        else:
            print("Không tìm thấy nhân viên có ID: " + mnv_cap_nhat)

def cc_5():
    if xac_nhan():
        start_time = datetime.datetime.now()
        mnv_xoa = input("Nhập ID nhân viên muốn xóa: ").upper()
        if mnv_xoa in nhan_vien:
            del nhan_vien[mnv_xoa]  # Xóa nhân viên khỏi từ điển
            print("Đã xóa nhân viên có ID: " + mnv_xoa)
            end_time = datetime.datetime.now()
            print(f"Thời gian thực hiện chức năng 1: {end_time - start_time}")
            
        else:
            print("Không tìm thấy nhân viên có ID: " + mnv_xoa)
            end_time = datetime.datetime.now()
            print(f"Thời gian thực hiện chức năng 1: {end_time - start_time}")
        
        # Cập nhật lại file Excel
        updated_data = pd.DataFrame.from_dict(nhan_vien, orient='index')
        updated_data.index.name = 'ID'
        try:
            updated_data.to_excel(r'data.xlsx', index=True)
            print("Dữ liệu đã được cập nhật thành công trong file Excel.")
        except Exception as e:
            print(f"Có lỗi khi ghi đè file Excel: {e}")


def cc_6():
    for id, info in nhan_vien.items():
        print("ID:", id)
        print("Tên:", info['Họ tên'])
        print("Chức danh:", info['Chức danh'])
        print("SĐT:", info['Số điện thoại'])
        print("Email:", info['Email'])
        print("-" * 38)

def cc_7():
    start_time = datetime.datetime.now()
    if 'Phòng ban' in data.columns:
    # Phân loại nhân viên theo phòng ban
        nhan_vien_theo_phong_ban = data.groupby('Phòng ban')

    # Hiển thị danh sách nhân viên theo từng phòng ban
        for phong_ban, group in nhan_vien_theo_phong_ban:
            print("Nhân viên thuộc phòng ban: ", phong_ban)
            print(group[['ID', 'Họ tên']])
            print("-" * 20)
            end_time = datetime.datetime.now()
            print(f"Thời gian thực hiện chức năng 1: {end_time - start_time}")
    else:
        print("Cột 'Phòng ban' không tồn tại trong dữ liệu.")

def cc_8():
    start_time = datetime.datetime.now()
    for id, info in nhan_vien.items():
        print("ID:", id)
        print("Tên:", info['Họ tên'])
        print("Chức danh:", info['Chức danh'])
        print("Lương:", info['Lương'])
        print("-" * 38)
        end_time = datetime.datetime.now()
        print(f"Thời gian thực hiện chức năng 1: {end_time - start_time}")

def cc_9():
    start_time = datetime.datetime.now()
    print("\nChức năng gửi thông báo cho nhân viên")
    print(" ++-----------------------------------------++")

    if len(data) == 0:
        print("Không có thông tin nhân viên để gửi thông báo.")
        return
    thong_bao = input("Nhập thông báo bạn muốn gửi cho nhân viên: ")
    id_nhan_vien = input("Nhập ID nhân viên bạn muốn gửi thông báo: ").strip().upper()

    if id_nhan_vien not in data['ID'].values:
        print("Không tìm thấy nhân viên với ID: " + id_nhan_vien)
        return

    nhan_vien = data[data['ID'] == id_nhan_vien].iloc[0]
    ten_nv = nhan_vien['Họ tên']
    sdt_nv = nhan_vien['Số điện thoại']
    email_nv = nhan_vien['Email']

    thong_bao_nhan_vien = f"""
    Kính gửi {ten_nv},

    {thong_bao}

    Trân trọng,
    Bộ phận nhân sự thông báo đến bạn
    """
    
    print(f"Thông báo cho nhân viên {ten_nv} (SDT: {sdt_nv}, Email: {email_nv}):")
    print(thong_bao_nhan_vien)
    end_time = datetime.datetime.now()
    print(f"Thời gian thực hiện chức năng 1: {end_time - start_time}")

    print("Đã gửi thông báo cho nhân viên.")

def cc_10():
    start_time = datetime.datetime.now()
    print("\nChức năng đánh giá nhân viên")
    print(" ++-----------------------------------------++")
    print(" | Đánh giá dựa trên các tiêu chí sau:       |")
    print(" | 1. Hiệu suất công việc (1-5)              |")
    print(" | 2. Đúng hạn (1-5)                         |")
    print(" | 3. Tinh thần làm việc nhóm (1-5)          |")
    print(" | 4. Kỹ năng chuyên môn (1-5)               |")
    print(" ++-----------------------------------------++")

    def danh_gia_nhan_vien(row):
        # Lấy thông tin về nhân viên để hiển thị cho người dùng đánh giá
        ten_nv = row['Họ tên']
        
        # Đánh giá hiệu suất với điểm từ 1 đến 5
        while True:
            try:
                hieu_suat = input("Nhập điểm hiệu suất cho nhân viên " + ten_nv + " (1-5): ")
                hieu_suat = int(hieu_suat)
                if 1 <= hieu_suat <= 5:
                    break
                else:
                    print("Vui lòng nhập điểm từ 1 đến 5.")
            except ValueError:
                print("Vui lòng nhập số.")

        # Đánh giá đúng hạn với điểm từ 1 đến 5
        while True:
            try:
                dung_han = input("Nhập điểm đúng hạn cho nhân viên 099" + ten_nv + " (1-5): ")
                dung_han = int(dung_han)
                if 1 <= dung_han <= 5:
                    break
                else:
                    print("Vui lòng nhập điểm từ 1 đến 5.")
            except ValueError:
                print("Vui lòng nhập số.")

        # Đánh giá làm việc nhóm với điểm từ 1 đến 5
        while True:
            try:
                lam_viec_nhom = input("Nhập điểm tinh thần làm việc nhóm cho nhân viên " + ten_nv + " (1-5): ")
                lam_viec_nhom = int(lam_viec_nhom)
                if 1 <= lam_viec_nhom <= 5:
                    break
                else:
                    print("Vui lòng nhập điểm từ 1 đến 5.")
            except ValueError:
                print("Vui lòng nhập số.")

        # Đánh giá kĩ năng chuyên môn với điểm từ 1 đến 5
        while True:
            try:
                ky_nang = input("Nhập điểm kỹ năng chuyên môn cho nhân viên " + ten_nv +  " (1-5): ")
                ky_nang = int(ky_nang)
                if 1 <= ky_nang <= 5:
                    break
                else:
                    print("Vui lòng nhập điểm từ 1 đến 5.")
            except ValueError:
                print("Vui lòng nhập số.")
        
        # Tính tổng điểm đánh giá
        tong_diem = hieu_suat + dung_han + lam_viec_nhom + ky_nang
        
        # Trả về tổng điểm đánh giá
        return tong_diem

    # Thêm cột đánh giá cho từng nhân viên
    data['Điểm đánh giá'] = data.apply(danh_gia_nhan_vien, axis=1)

    # Hiển thị danh sách nhân viên và điểm đánh giá
    print("\nBảng đánh giá nhân viên:")
    print(data[['ID', 'Họ tên', 'Chức danh', 'Điểm đánh giá']])
    
    try:
        data[['ID', 'Họ tên', 'Chức danh', 'Điểm đánh giá']].to_excel('bang_danh_gia_nhan_vien.xlsx', index=False)
        print("Dữ liệu đã được xuất ra file Excel thành công.")
    except Exception as e:
        print(f"Có lỗi khi xuất ra file Excel: {e}")
        
    end_time = datetime.datetime.now()
    print(f"Thời gian thực hiện chức năng 1: {end_time - start_time}")