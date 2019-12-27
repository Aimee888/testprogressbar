from tkinter import *
import time
import threading
import tkinter.ttk as ttk


list = []


def run():
    th = threading.Thread(target=update_progress_bar)
    th.setDaemon(True)
    th.start()


def get_list():
    print(list[0])
    list[0] = (1, "p")
    for j in range(len(list)):
        list[j] = (j+1, "p")
        update_progress_bar()
        time.sleep(1)


def get_status():
    th = threading.Thread(target=get_list)
    th.setDaemon(True)
    th.start()


def update_progress_bar():
    test_num = 0
    for k, tuple_p in enumerate(list):
        if tuple_p[1] != "p":
            test_num = k
            break
        if k == 99:
            test_num = 100
    percent = test_num
    print(test_num)
    green_length = int(sum_length * percent / 100)
    canvas_progress_bar.coords(canvas_shape, (0, 0, green_length, 25))
    canvas_progress_bar.itemconfig(canvas_text, text='%0.2f %%' % percent)
    # for percent in range(1, 101):
    #     # hour = int(percent/3600)
    #     # minute = int(percent/60) - hour*60
    #     # second = percent % 60
    #     green_length = int(sum_length * percent / 100)
    #     canvas_progress_bar.coords(canvas_shape, (0, 0, green_length, 25))
    #     # canvas_progress_bar.itemconfig(canvas_text, text='%02d:%02d:%02d' % (hour, minute, second))
    #     canvas_progress_bar.itemconfig(canvas_text, text='%0.2f %%' % percent)
    #     # var_progress_bar_percent.set('%0.2f %%' % percent)
    #     time.sleep(1)


# 表格内容插入
def get_tree():
    # 删除原节点
    for _ in map(tree.delete, tree.get_children("")):
        pass
    # 更新插入新节点
    for line in list:
        tree.insert("", "end", values=(line[0], line[1]))
    tree.after(50, get_tree)


if __name__ == "__main__":
    root = Tk()
    root.geometry("1024x768")
    root.config(bg='#535353')

    # 进度条
    sum_length = 630
    canvas_progress_bar = Canvas(root, width=sum_length, height=20)
    canvas_shape = canvas_progress_bar.create_rectangle(0, 0, 0, 25, fill='green')
    canvas_text = canvas_progress_bar.create_text(292, 4, anchor=NW)
    # canvas_progress_bar.itemconfig(canvas_text, text='00:00:00')
    canvas_progress_bar.itemconfig(canvas_text, text='00.00%')
    # var_progress_bar_percent = StringVar()
    # var_progress_bar_percent.set('00.00 %')
    # label_progress_bar_percent = Label(root, textvariable=var_progress_bar_percent, fg='#F5F5F5', bg='#535353')
    canvas_progress_bar.place(relx=0.45, rely=0.4, anchor=CENTER)
    # label_progress_bar_percent.place(relx=0.89, rely=0.4, anchor=CENTER)
    # # 按钮
    # button_start = Button(root, text='开始', fg='#F5F5F5', bg='#7A7A7A', command=run, height=1,
    #                       width=15, relief=GROOVE, bd=2, activebackground='#F5F5F5',
    #                       activeforeground='#535353')
    # button_start.place(relx=0.45, rely=0.3, anchor=CENTER)

    # t1 = Text(root, width=45, height=30)
    # t1.place(relx=0.45, rely=0.7, anchor=CENTER)
    # Label(t1, text=" test1", font="Arial, 10", width=45, anchor=NW).grid(row=0, column=0, padx=1)
    # Label(t1, text=" test2", font="Arial, 10", width=45, anchor=NW).grid(row=0, column=1, padx=1)

    t1 = Text(root)
    t1.place(relx=0.45, rely=0.7, anchor=CENTER)
    tree = ttk.Treeview(t1, show="headings", height=18, columns=("d", "e"))
    vbar = ttk.Scrollbar(t1, orient=VERTICAL, command=tree.yview)
    # 定义树形结构与滚动条
    tree.configure(yscrollcommand=vbar.set)
    tree.tag_configure("ttk", foreground="black")
    # print(ttk.Style().theme_names())
    ttk.Style().theme_use('default')
    # ttk.Style().configure("Treeview", background="#383838", foreground="white")
    ttk.Style().configure("Treeview.Heading", background="gray")

    # 表格的标题
    tree.column("d", width=200, anchor="center")
    tree.column("e", width=100, anchor="center")
    tree.heading("d", text="打印任务编号")
    tree.heading("e", text="打印状态")

    for i in range(0, 100):
        list.append((i+1, "N/A"))
    get_tree()
    get_status()

    tree.grid(row=0, column=0, sticky=NSEW)
    vbar.grid(row=0, column=1, sticky=NS)

    root.mainloop()
