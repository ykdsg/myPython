import pandas as pd
import os

# Excel文件路径
directory = '/Users/ykdsg/Downloads/exc'

# 记录开始时间
start_time = pd.Timestamp.now()
# 遍历目录中的文件
for filename in os.listdir(directory):
    # 检查文件是否为.xlsx文件
    if filename.endswith(".xlsx"):
        # 构建完整文件路径
        excel_file = os.path.join(directory, filename)

        # 读取Excel文件
        df = pd.read_excel(excel_file)

        # 获取没有扩展名的文件名，用于生成CSV文件名
        base_name = os.path.splitext(filename)[0]

        # 保存为CSV文件，使用与原文件相同的文件名，但扩展名为.csv
        csv_file = os.path.join(directory, f"{base_name}.csv")
        df.to_csv(csv_file, index=False)  # 不保存索引

# 计算花费的时间
end_time = pd.Timestamp.now() - start_time
print(f"转换完成！，花费{end_time}s")
