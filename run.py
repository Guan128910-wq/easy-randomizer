#导入模块
from tkinter import *
from tkinter.messagebox import *
import random
import webbrowser
import os
import time
#搭建主窗口
root = Tk()
root.title('随机生成器')
root.geometry("780x100")
root.resizable(0, 0)
# 搭建报错/提示/警告窗口
window = Tk()
window.withdraw()
# 变量初始化
xr = True  # 随机结果写入
xunhuantime = 1  # 循环次数
sett = []  # 随机列表存储
# 导入配置文件
try:
    with open('setting.txt', 'r', encoding='utf-8') as file:
        for line1 in file:
            line1 = line1.strip('\n')
            sett.append(str(line1))
        xr = str(sett[0])
        xunhuantime = int(sett[1])
finally:
    pass
# 生成随机
def rdm():
    # 初始化变量
    rdm1 = []
    rdmfi = 'None'
    global xr
    global xunhuantime
    try:
    # 写入列表
        with open('rdm.txt', 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip('\n')
                rdm1.append(str(line))
        # 循环
        for i in range(xunhuantime):
            rdmfi = random.choice(rdm1)
            # 写入文件
            if xr == 'Allow':
                with open('logs.txt', 'a', encoding='utf-8') as file:
                    file.write(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()) + ' 输出结果：' + rdmfi + '\n')
            result = showinfo('输出结果', rdmfi)
    # 报错说明
    except:
        result = showerror('错误', '无法找到文件或读取文件')
        result = showwarning('警告', '请确保文件已存在、权限正常且里面存在内容')
# 查看使用说明
def useinfo():
    usefile = '使用说明.docx'
    os.startfile(usefile)
# 查看随机列表
def rdminfo():
    usefile = 'rdm.txt'
    os.startfile(usefile)
# 查看配置文件
def settings():
    usefile = 'setting.txt'
    os.startfile(usefile)
# 查看输出历史
def history():
    usefile = 'logs.txt'
    os.startfile(usefile)
# 查看github项目地址
def github():
    url = "https://github.com/Guan128910-wq/easy-randomizer"
    webbrowser.open(url)
# 查看作者博客
def blog():
    url = "https://blog.guange.top/"
    webbrowser.open(url)
#按钮文字配置
btn = Button(root, text='生成随机', command=rdm)
btn1 = Button(root, text='查看使用说明', command=useinfo)
btn2 = Button(root, text='查看随机列表', command=rdminfo)
btn3 = Button(root, text='查看配置文件', command=settings)
btn4 = Button(root, text='作者博客', command=blog)
btn5 = Button(root, text='查看输出历史', command=history)
btn6 = Button(root, text='github项目地址', command=github)
label_maker = Label(root, text='guan管哥制作，请勿售卖，已在github开源')
# 按钮文字放置
btn.place(x=10, y=10, width=100, height=50)
btn1.place(x=120, y=10, width=100, height=50)
btn2.place(x=230, y=10, width=100, height=50)
btn3.place(x=340, y=10, width=100, height=50)
btn4.place(x=560, y=10, width=100, height=50)
btn5.place(x=450, y=10, width=100, height=50)
btn6.place(x=670, y=10, width=100, height=50)
label_maker.place(x=280, y=70)
# 运行窗口
root.mainloop()