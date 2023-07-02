import os
import glob

# 指定要读取的文件夹
directory = r'E:\360MoveData\ts\ttts'

# 指定合并后的文件名
output_file = 'merged.txt'

# 使用glob模块找到所有的.txt文件
txt_files = glob.glob(os.path.join(directory, '*.txt'))

# 按文件名排序
txt_files.sort()

# 打开你要写入的文件
with open(output_file, 'w',encoding='utf-8') as outfile:
    for fname in txt_files:
        # 打开每个.txt文件进行读取和写入
        with open(fname,encoding='utf-8') as infile:
            # 读取文件内容并写入到新的文件中
            for line in infile:
                outfile.write(line)
            # 在每个文件内容之间添加一个换行符，使得合并的文件更加清晰

