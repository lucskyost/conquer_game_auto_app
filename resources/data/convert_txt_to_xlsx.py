import pandas as pd
import os
print(os.getcwd())
# Đọc dữ liệu từ tệp văn bản
data = []
with open("data.txt", "r") as file:
    for line in file:
        data.append(line.strip().split("|"))

# Tạo DataFrame từ dữ liệu
df = pd.DataFrame(data, columns=["USER", "PASSWORD", "GROUP", "SEVER", "LEVEL", "GOLD"])

# Ghi DataFrame vào tệp Excel
df.to_excel("data.xlsx", index=False)
