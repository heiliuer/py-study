import os;

files = os.listdir();
print(os.listdir());  # 第一次 import 的时候会执行，只需引入一次，重复引入无效
for file in files:
    if file not in ["rename.py", "__init__.py"]:
        os.renames(file, file.replace("demo", ""));
        print(file, " to ", file.replace("demo", ""));
