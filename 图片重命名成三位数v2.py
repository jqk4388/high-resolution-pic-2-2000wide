import os

# 获取 .py 文件的绝对路径
file_path = os.path.abspath (__file__)
# 获取 .py 文件所在的目录
dir_path = os.path.dirname (file_path)
# 将当前目录切换到 .py 文件所在的目录
os.chdir (dir_path)

# 获取当前目录下所有的jpg和png格式图片
image_list = []
for filename in os.listdir('.'):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        image_list.append(filename)

# 以最后一个数字为顺序将图片排序
def get_image_index(image_name):
    try:
        return int(os.path.splitext(image_name)[0].split('-')[-1])
    except ValueError:
        return 0

image_list.sort(key=get_image_index)

# 重新命名图片，以001、002、003等顺序命名
for index, image_name in enumerate(image_list):
    _, ext = os.path.splitext(image_name)
    new_filename = '{:03d}{}'.format(index + 1, ext)
    os.rename(image_name, new_filename)