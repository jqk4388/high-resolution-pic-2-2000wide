import os
from PIL import Image
import concurrent.futures
import time

# 获取 .py 文件的绝对路径
file_path = os.path.abspath (__file__)
# 获取 .py 文件所在的目录
dir_path = os.path.dirname (file_path)
# 将当前目录切换到 .py 文件所在的目录
os.chdir (dir_path)

start_time = time.time()  # 记录程序开始时间

# 获取当前目录下所有的jpg格式图片
image_list = []
for filename in os.listdir('.'):
    if filename.endswith('.jpg'):
        image_list.append(filename)

# 获取用户输入的文件夹名字
folder_name = "2000w"
os.makedirs(folder_name, exist_ok=True)

# 拉伸或等比例缩小宽度到2000像素，并保存成95%质量的jpg
def process_image(image_name):
    with Image.open(image_name) as im:
        # 计算调整后的大小
        width, height = im.size
        new_width = 2000
        new_height = int(new_width * height / width)
        # 等比例缩放或拉伸图片
        if width <= new_width:
            new_size = (new_width, new_height)
        else:
            new_size = (new_width, new_height)
        new_im = im.resize(new_size, resample=Image.LANCZOS)
        # 保存调整后的图片
        new_im.save(os.path.join(folder_name, image_name), quality=95)
    return f'{image_name}处理完成'

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(process_image, image_name) for image_name in image_list]
    for future in concurrent.futures.as_completed(futures):
        print(future.result())

end_time = time.time()  # 记录程序结束时间
print(f"是否删除大分辨率jpg？")
input("按任意键继续...")
#删除当前目录下的所有jpg文件
def delete_jpg_files():
    """
    删除当前目录中的所有jpg文件。
    
    该函数遍历当前目录下的所有文件，如果文件以“.jpg”结尾，则将其删除。
    这样做的目的是为了清理或整理当前目录，避免jpg文件占用过多空间或干扰。
    """
    # 遍历当前目录下的所有文件
    for file in os.listdir():
        # 判断文件是否以jpg结尾
        if file.endswith(".jpg"):
            # 删除jpg文件
            os.remove(file)
            # 输出文件名，提示文件已删除
            print(f"{file}已删除")

delete_jpg_files()
print(f'处理完成，总共用时{end_time - start_time:.2f}秒')
input("按任意键结束")
