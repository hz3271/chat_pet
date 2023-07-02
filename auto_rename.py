import os

def rename_files_in_dir(directory):
    files = sorted(os.listdir(directory)) # 获取并排序文件

    for i, filename in enumerate(files, 1):
        old_path = os.path.join(directory, filename)
        # 获取文件的扩展名（如果有的话）
        _, extension = os.path.splitext(filename)
        # 创建新文件名
        new_name = f"{i}{extension}"
        new_path = os.path.join(directory, new_name)
        os.rename(old_path, new_path) # 重命名文件

# 使用
rename_files_in_dir(r"E:\360MoveData\ts\ankeleiqi")
