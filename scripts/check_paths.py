from pathlib import Path

# 终端当前所在的目录
current_dir = Path.cwd()

# 当前脚本的完整路径
script_path = Path(__file__).resolve()

# 脚本所在的文件夹
script_dir = script_path.parent

# 项目根目录：scripts 的上一级
project_root = script_dir.parent

# 项目中的 data 文件夹
data_dir = project_root / "data"

print("当前工作目录：", current_dir)
print("脚本文件位置：", script_path)
print("脚本所在目录：", script_dir)
print("项目根目录：", project_root)
print("数据目录：", data_dir)

if data_dir.is_dir():
    print("data 文件夹存在。")

    items = list(data_dir.iterdir())

    if items:
        print("data 中的内容：")
        for item in items:
            print("-", item.name)
    else:
        print("data 文件夹目前为空。")
else:
    print("没有找到 data 文件夹，检查项目目录。")