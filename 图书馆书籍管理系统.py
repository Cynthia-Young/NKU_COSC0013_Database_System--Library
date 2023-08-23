#!/usr/bin/env python
# coding: utf-8

# In[114]:


get_ipython().system('pip install pymysql')


# In[115]:


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import pymysql


# In[116]:


datebase = pymysql.connect(host="localhost", user="root", password="yxy020819", database="library", port=3306, autocommit=True)
cursor = datebase.cursor()


# In[117]:


# 退出查询系统window界面
def CloseWindow():
    window.destroy()


# In[118]:


# 销毁窗口
def onCloseOtherFrame(oF1, otherFrame):
    otherFrame.destroy()
    show(oF1)


# In[119]:


# 返回展示老窗口
def show(oF):
    oF.update()
    oF.deiconify()


# # 4 含有事务应用的删除操作

# ## 4.0删除界面

# ### 主界面

# In[120]:


# 删除信息
def delete():
    otherFrame1 = tk.Toplevel()
    otherFrame1.geometry('700x450')
    otherFrame1.title("删除信息")
    handle = lambda: onCloseOtherFrame(window, otherFrame1)
    b = lambda: delete_book(otherFrame1)
    fb = lambda: delete_floor_book(otherFrame1)
    tk.Button(otherFrame1, text='返回', width=20, command=handle).pack(side='bottom', anchor='center')
    tk.Button(otherFrame1, text='删除书籍信息', font=('黑体', 15), width=25, command=b).pack(padx=5, pady=20)
    tk.Button(otherFrame1, text='删除某楼层书籍所属信息', font=('黑体', 15), width=25, command=fb).pack(padx=5, pady=20)


# ## 4.1删除书籍信息

# In[121]:


# 删除书籍信息
def delete_book(oF):
    otherFrame = tk.Toplevel()
    otherFrame.geometry('700x450')
    otherFrame.title("删除书籍信息")
    handle = lambda: onCloseOtherFrame(oF, otherFrame)
    tk.Button(otherFrame, text='返回', width=20, command=handle).pack(side='top', anchor='nw')
    tk.Label(otherFrame, text="请输入 书籍ID", font=('黑体', 16)).pack()
    e1 = tk.StringVar()
    tk.Entry(otherFrame, show='', textvariable=e1, font=('宋体', 14)).pack(padx=5, pady=10)
    
    click = lambda: delete_book_sql(otherFrame, oF, e1)
    tk.Button(otherFrame, text='删除', command=click, font=('黑体', 16)).pack(side='bottom')


# In[122]:


def delete_book_sql(oF, oF2, e1):
    b_id = e1.get()
    tree = ttk.Treeview(oF)
    title = ["书籍名称", "书籍编号", "书籍单价"]
    tree["columns"] = ("书籍名称", "书籍编号", "书籍单价")
    for i in title:
        tree.column(i, anchor="center")
        tree.heading(i, text=i)
    temp = "SELECT * FROM book WHERE b_id = '" + b_id + "';"
    cursor.execute(temp)
    result = cursor.fetchall()
    for i in range(len(result)):
        tree.insert("", i, values=result[i])
    tree['show'] = 'headings'
    tree.pack(anchor="center", padx=5, pady=10)
    sql = "DELETE FROM book WHERE b_id = '" + b_id + "';"
    click = lambda: cancel(oF, oF2, sql)
    tk.Button(oF, text='取消', command=click, font=('黑体', 12)).pack(side='bottom')
    click = lambda: insist(oF, oF2, sql)
    tk.Button(oF, text='确定', command=click, font=('黑体', 12)).pack(side='bottom')


# ## 4.2删除图书馆某层书的所属信息

# In[123]:


# 删除图书馆某层书的所属信息
def delete_floor_book(oF):
    otherFrame = tk.Toplevel()
    otherFrame.geometry('700x450')
    otherFrame.title("删除某楼层书籍所属信息")
    handle = lambda: onCloseOtherFrame(oF, otherFrame)
    tk.Button(otherFrame, text='返回', width=20, command=handle).pack(side='top', anchor='nw')
    tk.Label(otherFrame, text="请输入 图书馆楼层", font=('黑体', 16)).pack()
    e1 = tk.StringVar()
    tk.Entry(otherFrame, show='', textvariable=e1, font=('宋体', 14)).pack(padx=5, pady=10)
    
    click = lambda: delete_floor_book_sql(otherFrame, oF, e1)
    tk.Button(otherFrame, text='删除', command=click, font=('黑体', 16)).pack(side='bottom')


# In[124]:


def delete_floor_book_sql(oF, oF2, e1):
    floor = e1.get()
    tree = ttk.Treeview(oF)
    title = [ "类别编号","书籍编号","类别名称","所在楼层"]
    tree["columns"] = ( "类别编号","书籍编号","类别名称","所在楼层")
    for i in title:
        tree.column(i, anchor="center")
        tree.heading(i, text=i)
    temp = "SELECT * FROM belong natural join class WHERE c_floor = '" + floor  + "';"
    cursor.execute(temp)
    result = cursor.fetchall()
    for i in range(len(result)):
        tree.insert("", i, values=result[i])
    tree['show'] = 'headings'
    tree.pack(anchor="center", padx=5, pady=10)
    sql = "DELETE belong FROM belong natural join class WHERE c_floor = '" + floor  + "';"
    click = lambda: cancel(oF, oF2, sql)
    tk.Button(oF, text='取消', command=click, font=('黑体', 12)).pack(side='bottom')
    click = lambda: insist(oF, oF2, sql)
    tk.Button(oF, text='确定', command=click, font=('黑体', 12)).pack(side='bottom')


# ### 确认还是取消

# In[125]:


def cancel(otherFrame, oF2, sql):
    cursor.execute("START TRANSACTION")
    cursor.execute(sql)
    cursor.execute("ROLLBACK")
    messagebox.showinfo(message='已取消')
    onCloseOtherFrame(oF2, otherFrame)


def insist(otherFrame, oF2, sql):
    cursor.execute("START TRANSACTION")
    cursor.execute(sql)
    cursor.execute("COMMIT")
    messagebox.showinfo(message='已删除')
    onCloseOtherFrame(oF2, otherFrame)


# # 5.	触发器控制下的添加操作

# ## 5.0主界面

# In[126]:


# 添加信息
def append():
    otherFrame1 = tk.Toplevel()
    otherFrame1.geometry('960x600')
    otherFrame1.title("添加信息")
    handle = lambda: onCloseOtherFrame(window, otherFrame1)
    p = lambda: append_lend(otherFrame1)
    t = lambda: append_book(otherFrame1)
    tk.Button(otherFrame1, text='返回', width=20, command=handle).pack(side='top', anchor='nw')
    tk.Button(otherFrame1, text='添加借阅信息', font=('隶书', 14), width=20, command=p).pack(padx=5, pady=5)
    tk.Button(otherFrame1, text='添加书籍信息', font=('隶书', 14), width=20, command=t).pack(padx=5, pady=5)


# ### 5.1添加借阅信息

# In[127]:


# 添加借阅信息
def append_lend(oF):
    otherFrame = tk.Toplevel()
    otherFrame.geometry('560x660')
    otherFrame.title("添加借阅信息")
    handle = lambda: onCloseOtherFrame(oF, otherFrame)
    tk.Button(otherFrame, text='返回', width=20, command=handle).pack(side='top', anchor='nw')
    tk.Button(otherFrame, text="请输入书籍编号", font=('隶书', 12)).pack()
    e3 = tk.StringVar()
    tk.Entry(otherFrame, show='', textvariable=e3, font=('宋体', 10)).pack(padx=4, pady=8)
    tk.Button(otherFrame, text="请输入你的学号", font=('隶书', 12)).pack()
    e1 = tk.StringVar()
    tk.Entry(otherFrame, show='', textvariable=e1, font=('宋体', 10)).pack(padx=4, pady=8)
    tk.Button(otherFrame, text="请输入借阅起始日期", font=('隶书', 12)).pack()
    e2 = tk.StringVar()
    tk.Entry(otherFrame, show='', textvariable=e2, font=('宋体', 10)).pack(padx=4, pady=8)
    tk.Button(otherFrame, text="请输入借阅截止日期", font=('隶书', 12)).pack()
    e8 = tk.StringVar()
    tk.Entry(otherFrame, show='', textvariable=e8, font=('宋体', 10)).pack(padx=4, pady=8)
    click = lambda: insert_lend(otherFrame, e3, e1, e2, e8)
    tk.Button(otherFrame, text='插入', command=click).pack(side='bottom')


# In[128]:


def insert_lend(otherFrame, e3, e1, e2, e8):
    b_id= e3.get()
    std_id = e1.get()
    begin_t = e2.get()
    end_t = e8.get()
    sql = "INSERT INTO lend values('" + b_id + "', '" + std_id + "', '" + begin_t + "', '" + end_t +  "');"
    print( "INSERT INTO lend values('" + b_id + "', '" + std_id + "', '" + begin_t + "', '" + end_t +  "');")
    try:
        cursor.execute(sql)
        messagebox.showinfo(message='插入成功！')
    except Exception as m:
        messagebox.showerror('警告', m.args)


# ### 5.2添加书籍信息

# In[129]:


# 添加书籍信息
def append_book(oF):
    otherFrame = tk.Toplevel()
    otherFrame.geometry('560x600')
    otherFrame.title("添加书籍信息")
    handle = lambda: onCloseOtherFrame(oF, otherFrame)
    tk.Button(otherFrame, text='返回', width=20, command=handle).pack(side='top', anchor='nw')
    tk.Button(otherFrame, text="请输入书籍名称", font=('隶书', 12)).pack()
    e1 = tk.StringVar()
    tk.Entry(otherFrame, show='', textvariable=e1, font=('宋体', 10)).pack(padx=4, pady=8)
    tk.Button(otherFrame, text="请输入书籍编号", font=('隶书', 12)).pack()
    e2 = tk.StringVar()
    tk.Entry(otherFrame, show='', textvariable=e2, font=('宋体', 10)).pack(padx=4, pady=8)
    tk.Button(otherFrame, text="请输入书籍价格", font=('隶书', 12)).pack()
    e3 = tk.StringVar()
    tk.Entry(otherFrame, show='', textvariable=e3, font=('宋体', 10)).pack(padx=4, pady=8)
    click = lambda: insert_book(otherFrame, e1, e2, e3)
    tk.Button(otherFrame, text='插入', command=click).pack(side='bottom')


# In[130]:


def insert_book(otherFrame, e1, e2, e3):
    b_name = e1.get()
    b_id = e2.get()
    b_price = e3.get()
    sql = "INSERT INTO book values('" + b_name + "', '" + b_id + "', '" + b_price +  "');"
    try:
        cursor.execute(sql)
        messagebox.showinfo(message='插入成功！')
    except Exception as m:
        messagebox.showerror('警告', m.args)


# # 6.	存储过程控制下的更新操作

# In[131]:


# 更新信息
def update():
    otherFrame1 = tk.Toplevel()
    otherFrame1.geometry('960x600')
    otherFrame1.title("更新信息")
    handle = lambda: onCloseOtherFrame(window, otherFrame1)
    p = lambda: update_price(otherFrame1)
    tk.Button(otherFrame1, text='返回', width=20, command=handle).pack(side='top', anchor='nw')
    tk.Button(otherFrame1, text='更新 某出版社书籍价格信息', font=('隶书', 16), width=30, command=p).pack(padx=5, pady=5)


# In[132]:


# 更新某出版社书籍价格信息
def update_price(oF):
    otherFrame = tk.Toplevel()
    otherFrame.geometry('960x600')
    otherFrame.title("更新某出版社书籍价格信息")
    handle = lambda: onCloseOtherFrame(oF, otherFrame)
    tk.Button(otherFrame, text='返回', width=20, command=handle).pack(side='top', anchor='nw')
    tk.Label(otherFrame, text="请输入 出版社名称", font=('隶书', 16)).pack()
    e1 = tk.StringVar()
    tk.Entry(otherFrame, show='', textvariable=e1, font=('宋体', 14)).pack(padx=5, pady=10)
    tk.Label(otherFrame, text="请输入 书籍名称", font=('隶书', 16)).pack()
    e2 = tk.StringVar()
    tk.Entry(otherFrame, show='', textvariable=e2, font=('宋体', 14)).pack(padx=5, pady=10)
    tk.Label(otherFrame, text="请输入 书籍价格", font=('隶书', 16)).pack()
    e3 = tk.StringVar()
    tk.Entry(otherFrame, show='', textvariable=e3, font=('宋体', 14)).pack(padx=5, pady=10)
    click = lambda: update_price_sql(otherFrame, e1,e2,e3)
    tk.Button(otherFrame, text='更新', command=click, font=('隶书', 16)).pack(side='bottom')


# In[133]:


def update_price_sql(oF, e1, e2, e3):
    publish_name = e1.get()
    book_name = e2.get()
    book_price = e3.get()
    try:
        sql = "call book_update('" + publish_name + "', '" + book_name + "', '" + book_price + "');"
        cursor.execute(sql)
        messagebox.showinfo(message='更新成功！')
    except Exception as m:
        messagebox.showerror('警告', m.args)


# # 7.	含有视图的查询操作

# In[134]:


# 查询信息
def search():
    otherFrame1 = tk.Toplevel()
    otherFrame1.geometry('960x600')
    otherFrame1.title("查询信息")
    handle = lambda: onCloseOtherFrame(window, otherFrame1)
    tk.Button(otherFrame1, text='返回', width=20, command=handle).pack(side='top', anchor='nw')
    p = lambda: search_book(otherFrame1)
    tk.Button(otherFrame1, text='查询某作者著作数量', font=('隶书', 14), width=20, command=p).pack(padx=5, pady=5)


# In[135]:


# 查询书籍信息
def search_book(oF):
    otherFrame = tk.Toplevel()
    otherFrame.geometry('960x600')
    otherFrame.title("查询某作者著作数量")
    handle = lambda: onCloseOtherFrame(oF, otherFrame)
    tk.Button(otherFrame, text='返回', width=20, command=handle).pack(side='top', anchor='nw')
    tk.Label(otherFrame, text="请输入 作者姓名", font=('隶书', 16)).pack()
    e2 = tk.StringVar()
    tk.Entry(otherFrame, show='', textvariable=e2, font=('宋体', 14)).pack(padx=5, pady=10)
    tk.Label(otherFrame, text="请输入 至少著作数量", font=('隶书', 16)).pack()
    e3 = tk.StringVar()
    tk.Entry(otherFrame, show='', textvariable=e3, font=('宋体', 14)).pack(padx=5, pady=10)
    click = lambda: find_book(otherFrame, e2, e3)
    tk.Button(otherFrame, text='查询', command=click, font=('隶书', 16)).pack(side='bottom')


# In[136]:


def find_book(oF, e2, e3):
    aut_name = e2.get()
    works_num = e3.get()
    tree = ttk.Treeview(oF)
    title = ["作者姓名", "著作数量"]
    tree["columns"] = ("作者姓名", "著作数量")
    for i in title:
        tree.column(i, anchor="center")
        tree.heading(i, text=i)
    temp = 'select * from author_find '
    if aut_name != '' and works_num != '':
        temp = temp + "where author_name = '" + str(aut_name) + "' and countworks >= '" + str(works_num) + "';"
    elif aut_name != '':
        temp = temp + "where author_name = '" + str(aut_name) + "';"
    elif works_num != '':
        temp = temp + "where countworks >= '" + str(works_num) + "';"
    else:
        tk.Label(oF, text='查 询 失 败', font=('楷书', 22), width=30, height=2).pack()
        return
    cursor.execute(temp)
    result = cursor.fetchall()
    if len(result) == 0:
        tk.Label(oF, text='查 询 失 败', font=('楷书', 22), width=30, height=2).pack()
        return
    for i in range(len(result)):
        tree.insert("", i, values=result[i])
    tree['show'] = 'headings'
    tree.pack(anchor="center", padx=5, pady=10)


# # 文件保存

# In[137]:


def get_image(filename, width, height):
    im = Image.open(filename).resize((width, height))
    return ImageTk.PhotoImage(im)


# In[138]:


window = tk.Tk()
window.title("数据库系统设计")
window.geometry('800x650+400+200')
window.resizable(False, False)

canvas_root = tk.Canvas(window, width=200, height=150)
im_root = get_image("C:\\Users\\vivia\\Desktop\\1.gif", 200, 150)
canvas_root.create_image(100, 70,image=im_root)
canvas_root.pack()


# In[139]:


tk.Label(window, text='图书馆书籍管理系统', font=("黑体", 25), width=40, height=5).pack(padx=5,pady=5)

tk.Button(window, text='D E L E T E', font=('楷书', 16), width=20, command=delete).pack(padx=5, pady=5)
tk.Button(window, text='I N S E R T', font=('楷书', 16), width=20, command=append).pack(padx=5, pady=5)
tk.Button(window, text='U P D A T E', font=('楷书', 16), width=20, command=update).pack(padx=5, pady=5)
tk.Button(window, text='S E A R C H', font=('楷书', 16), width=20, command=search).pack(padx=5, pady=5)

handler = lambda: CloseWindow()
tk.Button(window, text='Q U I T', font=('黑体', 14), width=20, command=handler).pack(side='bottom')

window.mainloop()


# In[ ]:




