# Bài 2:
# Lấy dữ liệu từ file excel từ link: https://docs.google.com/spreadsheets/d/1e9rRiwAmRYq60Lx2PBMZcSOA8jC-rmoL/edit?usp=sharing&ouid=115874127894901285908&rtpof=true&sd=true

# Hãy thực hiện lọc dữ liệu của các dữ liệu với điều kiện sau:
# - Trường dữ liệu có cột vpv1 và pCharge khác 0, cột SOC trên 8% lưu vào trong file mới có tên: Data_new.csv
# - Thực hiện tính tổng dữ liệu của từng hàng ppv1, ppv2, ppv3, tạo một cột mới có tên Sum_PPV và ghi kết quả vào đó.

import pandas as pd

# Đọc file Excel
df = pd.read_excel("data.xlsx")

# Chuyển cột SOC từ dạng chuỗi "10%" → 10 (int)
df["SOC"] = df["SOC"].str.replace("%", "").astype(float)

# Lọc dữ liệu theo điều kiện
filtered_df = df[(df["vpv1"] != 0) & (df["pCharge"] != 0) & (df["SOC"] > 8)]

# Tính tổng ppv1 + ppv2 + ppv3
filtered_df["Sum_PPV"] = filtered_df["ppv1"] + filtered_df["ppv2"] + filtered_df["ppv3"]

# Lưu vào file CSV mới
filtered_df.to_csv("Data_new.csv", index=False)

# In số dòng để xác nhận
print("Số dòng sau khi lọc:", len(filtered_df))
