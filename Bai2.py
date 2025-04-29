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
