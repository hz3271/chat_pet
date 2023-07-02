import os
import re

folder_path = r'D:\pythonProject1\vits-finetuning\wav\降噪'  # 这里填写你要处理的文件夹的路径

for filename in os.listdir(folder_path):
    # 匹配最后一个左括号及其后的所有内容，包括右括号
    new_name = re.sub(r'\([^()]*\)(?=[^()]*$)', '', filename)

    # 获取文件的绝对路径
    old_file_path = os.path.join(folder_path, filename)
    new_file_path = os.path.join(folder_path, new_name)

    # 重命名文件
    os.rename(old_file_path, new_file_path)

