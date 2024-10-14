from chuc_nang_nv import *

def Cc_11():
    while True:
        print("\nQuản lý thông tin nhân viên")
        print(" ++-----------------------------------------++")
        print(" |Chức năng 1: Hiển thị danh sách nhân viên  |")
        print(" |Chức năng 2: Tìm kiếm/Lọc nhân viên        |")
        print(" |Chức năng 3: Thêm mới nhân viên            |")
        print(" |Chức năng 4: Cập nhật thông tin nhân viên  |")
        print(" |Chức năng 5: Xóa nhân viên                 |")
        print(" |Chức năng 6: Xem chi tiết nhân viên        |")
        print(" |Chức năng 7: Phân loại theo phòng ban      |")
        print(" |Chức năng 8: Lương nhân viên               |")
        print(" |Chức năng 9: Gửi thông báo cho nhân viên   |")
        print(" |Chức năng 10: Đánh giá nhân viên           |")
        print(" |Chức năng 11: Thoát                        |")
        print(" ++-----------------------------------------++")

        try:
            chon_5 = int(input("\nChức năng bạn mong muốn: "))
        except ValueError:
            print("Vui lòng nhập số từ 1 đến 11.")
            continue
        
        if chon_5 == 1:
            cc_1()
        elif chon_5 == 2:
            cc_2()
        elif chon_5 == 3:
            cc_3()
        elif chon_5 == 4:
            cc_4()
        elif chon_5 == 5:
            cc_5()
        elif chon_5 == 6:
            cc_6()
        elif chon_5 == 7:
            cc_7()
        elif chon_5 == 8:
            cc_8()
        elif chon_5 == 9:
            cc_9()
        elif chon_5 == 10:
            cc_10()
        elif chon_5 == 11:
            if xac_nhan():
                print("Thoát chương trình.")
                break
        else:
            print("Chức năng không hợp lệ, vui lòng chọn lại.")

Cc_11()
