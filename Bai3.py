# Bài 3: 
# Tạo một chương trình thực hiện quản lý danh sách sinh viên lớp học (danh sách chính là danh sách các thành viên đi thực hành buổi học hôm nay) sử dụng OOP với các lớp như: Student, Family.
# (Student sẽ bao gồm các thông tin về: Họ tên, MSSV, Lớp, SĐT, Ngày sinh, địa chỉ
# Family sẽ bao gồm các thông tin của Student và thêm một số trường thông tin khác như: Địa chỉ gia đình, họ tên bố, mẹ - điền bừa)
# Yêu cầu:
# - Hệ thống cho phép thêm, sửa, xóa thông tin, cập nhật thông tin của Student hoặc Family.
# - Dữ liệu sẽ được lưu dưới dạng một file JSON với cấu trúc như sau:
# [
#     {
#         "id": 1,
#         "Thông tin sinh viên": [
#         	"Họ tên": ...,
#         	"MSSV": ...,
#         	"Lớp": ...,
#         	"SĐT": ...,
#         	"Ngày sinh": ...,
#         	"Địa chỉ hiện tại": ...
#         ],
#         "Thông tin gia đình": [
#         	"Địa chỉ gia đình": ...,
#         	"Họ tên bố": ...,
#         	"Họ tên mẹ": ...,
#         ]
#     },
#     {
#         "id": 2,
#         "Thông tin sinh viên": [
#         	"Họ tên": ...,
#         	"MSSV": ...,
#         	"Lớp": ...,
#         	"SĐT": ...,
#         	"Ngày sinh": ...,
#         	"Địa chỉ hiện tại": ...
#         ],
#         "Thông tin gia đình": [
#         	"Địa chỉ gia đình": ...,
#         	"Họ tên bố": ...,
#         	"Họ tên mẹ": ...,
#         ]
#     },
# ]
import json

class Student:
    def __init__(self, name, mssv, class_name, phone, birth_date, address):
        self.name = name
        self.mssv = mssv
        self.class_name = class_name
        self.phone = phone
        self.birth_date = birth_date
        self.address = address

    def to_dict(self):
        return {
            "Họ tên": self.name,
            "MSSV": self.mssv,
            "Lớp": self.class_name,
            "SĐT": self.phone,
            "Ngày sinh": self.birth_date,
            "Địa chỉ hiện tại": self.address
        }

class Family(Student):
    def __init__(self, name, mssv, class_name, phone, birth_date, address,
                 home_address, father_name, mother_name):
        super().__init__(name, mssv, class_name, phone, birth_date, address)
        self.home_address = home_address
        self.father_name = father_name
        self.mother_name = mother_name

    def to_dict(self, id):
        return {
            "id": id,
            "Thông tin sinh viên": super().to_dict(),
            "Thông tin gia đình": {
                "Địa chỉ gia đình": self.home_address,
                "Họ tên bố": self.father_name,
                "Họ tên mẹ": self.mother_name
            }
        }

# Ví dụ tạo và lưu
ds = []
sv1 = Family("Hầu Nhật Ninh", "K225480106077", "K58KTP.K01", "0974493002", "2003-12-20",
             "Ký túc xá K1", "Bách Nhẫn, Mai Trung", "Hầu Văn Nam", "Nguyễn Thị Lệ")
ds.append(sv1.to_dict(id=1))
sv2 = Family(
    "Trần Thảo Mai", "K225480106074", "K58KTP.K01", "0987654321", "2003-02-01",
    "Ký túc xá K2", "Thái Nguyên", "Trần Văn Dũng", "Lê Thị Dung"
)
ds.append(sv2.to_dict(id=2))
# Lưu vào JSON
with open("sinh_vien.json", "w", encoding="utf-8") as f:
    json.dump(ds, f, ensure_ascii=False, indent=4)
