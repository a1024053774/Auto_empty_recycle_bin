import zipfile

# 使用原始字符串来修复无效的转义序列警告，并确保路径正确
zip_file_path = r'D:\downloads\Telegram Desktop\14555794_活动风险管理.zip'
password_list_path = r'D:\downloads\Telegram Desktop\passwords.txt'



def try_password(zip_file_path, password_list_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        # 指定以UTF-8编码打开密码文件
        with open(password_list_path, 'r', encoding='utf-8') as pw_list:
            for line in pw_list.readlines():
                password = line.strip()  # 去除可能的换行符
                try:
                    zip_ref.extractall(pwd=bytes(password, 'utf-8'))
                    print(f"成功解锁! 密码是: {password}")
                    return password  # 如果成功解锁，返回密码并终止循环
                except:
                    continue  # 如果密码不正确，继续尝试下一个密码
    print("没有找到正确的密码。")
    return None

# 调用函数尝试解压文件
try_password(zip_file_path, password_list_path)

