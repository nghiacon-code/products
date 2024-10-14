import re
danh_sach = [
    {'Ma': 'SP001', 'Don_hang': 'Sản phẩm 1', 'Ngay_chuyen': '2024-09-01', 'Dia_chi_giao': 'Poly 1', 'Trang_thai': 'Đang giao'},
    {'Ma': 'SP003', 'Don_hang': 'Sản phẩm 3', 'Ngay_chuyen': '2024-09-05', 'Dia_chi_giao': 'Poly 3', 'Trang_thai': 'Đã giao'},
    {'Ma': 'SP002', 'Don_hang': 'Sản phẩm 2', 'Ngay_chuyen': '2024-09-03', 'Dia_chi_giao': 'Poly 2', 'Trang_thai': 'Đang giao'},
    {'Ma': 'SP005', 'Don_hang': 'Sản phẩm 5', 'Ngay_chuyen': '2024-09-07', 'Dia_chi_giao': 'Poly 5', 'Trang_thai': 'Đang giao'},
    {'Ma': 'SP004', 'Don_hang': 'Sản phẩm 4', 'Ngay_chuyen': '2024-09-06', 'Dia_chi_giao': 'Poly 4', 'Trang_thai': 'Đã hủy'}
]

def hien_thi_danh_sach():
    if not danh_sach:
        print('Danh sách trống')
    else:
        print('Danh sách hiện tại là:')
        for don_hang in danh_sach:
            print(don_hang)

def tim_kiem():
    while True:
        nhap_tim_kiem = input('Nhập mã đơn hàng để tìm kiếm : ')
        try:
            ket_qua = [
                don_hang for don_hang in danh_sach
                if re.search(nhap_tim_kiem, don_hang['Ma']) 
            ]
            
            if ket_qua:
                print('Kết quả tìm kiếm:')
                for don_hang in ket_qua:
                    print(don_hang)
                break  
            else:
                print("Không có kết quả phù hợp, vui lòng nhập lại.")
        
        except re.loi:
            print("Biểu thức chính quy không hợp lệ, vui lòng nhập lại.")

def them_moi():
    while True:
        nhap_ma = input('Nhập mã đơn hàng: ')
        nhap_don_hang = input('Nhập tên đơn hàng: ')
        nhap_ngay_chuyen = input('Nhập ngày chuyển: ')
        nhap_dia_chi_giao = input('Nhập địa chỉ giao: ')
        nhap_trang_thai = input('Nhập trạng thái: ')
        if not (nhap_ma and nhap_don_hang and nhap_ngay_chuyen and nhap_dia_chi_giao and nhap_trang_thai):
            print('Hãy nhập hết  ')
            continue
        xac_nhan = input('Bạn có chắc chắn muốn thêm đối tượng này? (Y/N): ')
        if xac_nhan.upper() == 'Y':
            danh_sach.append({
                'Ma': nhap_ma, 
                'Don_hang': nhap_don_hang, 
                'Ngay_chuyen': nhap_ngay_chuyen, 
                'Dia_chi_giao': nhap_dia_chi_giao, 
                'Trang_thai': nhap_trang_thai
            })
            
            print('Đã thêm vào danh sách')
            break  
        else:
            print('Thao tác hủy')
def cap_nhat():
    while True:
        ma = input('Nhập mã đơn hàng cần cập nhật: ')
        don_hang_cap_nhat = next((don for don in danh_sach if don['Ma'] == ma), None)
        if don_hang_cap_nhat:
            print('Thông tin đơn hàng trước khi cập nhật:', don_hang_cap_nhat)
            don_hang_cap_nhat['Don_hang'] = input('Nhập đơn hàng mới: ')
            don_hang_cap_nhat['Ngay_chuyen'] = input('Nhập ngày chuyển mới: ')
            don_hang_cap_nhat['Dia_chi_giao'] = input('Nhập địa chỉ giao mới: ')
            don_hang_cap_nhat['Trang_thai'] = input('Nhập trạng thái mới: ')
            print('Cập nhật thành công.')
            break  
        else:
            print("Không có mã đấy vui lòng nhập lại")

def xoa():
    while True:
        ma = input('Nhập mã đơn hàng cần xóa: ')
        don_hang_xoa = next((don for don in danh_sach if don['Ma'] == ma), None)
        if don_hang_xoa:
            xac_nhan = input('Bạn có chắc chắn muốn xóa đơn hàng này? (Y/N): ')
            if xac_nhan.upper() == 'Y':
                danh_sach.remove(don_hang_xoa)
                print('Xóa đơn hàng thành công.')
            else:
                print('Thao tác hủy.')
            break  
        else:
            print("Không có mã đấy vui lòng nhập lại")

def xem_chi_tiet():
    while True:
        ma = input('Nhập mã đơn cần xem chi tiết: ')
        don_hang_xem = next((don for don in danh_sach if don['Ma'] == ma), None)
        if don_hang_xem:
            print('Chi tiết đơn hàng:', don_hang_xem)
            break  
        else:
            print("Không có mã đấy vui lòng nhập lại")

def in_danh_sach():
    print('Danh sách là:')
    hien_thi_danh_sach()

def sap_xep():
    while True:
        chon = input("Chọn tiêu chí sắp xếp (1: Mã, 2: Ngày chuyển, 3: Địa chỉ, 4: Trạng thái): ")
        tieu_chi = {'1': 'Ma', '2': 'Ngay_chuyen', '3': 'Dia_chi_giao', '4': 'Trang_thai'}
        if chon in tieu_chi:
            danh_sach.sort(key=lambda x: x[tieu_chi[chon]])
            hien_thi_danh_sach()
            break
        print("Lựa chọn không hợp lệ, vui lòng chọn lại.")

def trang_thai_don_hang():
    while True:
        chon = input("Chọn trạng thái (1: Đang giao, 2: Đã giao, 3: Đã hủy): ")
        trang_thai = {'1': 'Đang giao', '2': 'Đã giao', '3': 'Đã hủy'}
        if chon in trang_thai:
            ket_qua = [don_hang for don_hang in danh_sach if don_hang['Trang_thai'] == trang_thai[chon]]
            print(ket_qua )
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại.")


def lich_su_don_hang():
    while True:
        ma = input("Nhập mã đơn hàng cần xem lịch sử: ")
        don_hang = None
        for item in danh_sach:
            if item['Ma'] == ma:
                don_hang = item
                break  
        if don_hang:
            print("Lịch sử đơn hàng với mã", ma, ":")
            print(don_hang)  
            break
        else:
            print("Không có mã đơn hàng này, vui lòng nhập lại.")


def van_chuyen():
    while True:
        print('---Vận chuyển---')
        print('1. Hiển thị danh sách')
        print('2. Tìm kiếm/Lọc')
        print('3. Thêm mới')
        print('4. Cập nhật')
        print('5. Xóa')
        print('6. Sắp xếp')
        print('7. Xem chi tiết')
        print('8. In danh sách')
        print('9. Trạng thái đơn hàng')
        print('10. Lịch sử đơn hàng')
        print('0. Thoát')

        chon_chuc_nang = input('Chọn chức năng: ')
        if chon_chuc_nang == '1':
            hien_thi_danh_sach()
        elif chon_chuc_nang == '2':
            tim_kiem()
        elif chon_chuc_nang == '3':
            them_moi()
        elif chon_chuc_nang == '4':
            cap_nhat()
        elif chon_chuc_nang == '5':
            xoa()
        elif chon_chuc_nang == '6':
            sap_xep()
        elif chon_chuc_nang == '7':
            xem_chi_tiet()
        elif chon_chuc_nang == '8':
            in_danh_sach()
        elif chon_chuc_nang == '9':
            trang_thai_don_hang()
        elif chon_chuc_nang == '10':
            lich_su_don_hang()
        elif chon_chuc_nang == '0':
            xac_nhan = input('Bạn có chắc chắn muốn thoát? (Y/N): ')
            if xac_nhan.upper() == 'Y':
                print('Thoát chương trình.')
                break
        else:
            print("Chức năng không hợp lệ, vui lòng chọn lại.")

van_chuyen()


    