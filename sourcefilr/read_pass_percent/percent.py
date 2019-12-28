from tkinter import *
import time
import threading
import tkinter.ttk as ttk

list_result = []
stop = 0


def run():
    th = threading.Thread(target=update_progress_bar)
    th.setDaemon(True)
    th.start()


class DetailInfo:
    def __init__(self, num, str_detail):
        self.num = str(num)
        self.str = str_detail
        t3.delete(0.0, END)
        t3.insert('0.0', self.num + self.str)


def get_list():
    global stop
    list_result[0] = (1, "p")
    for j in range(len(list_result)):
        list_result[j] = (j+1, "p")
        update_progress_bar()
        time.sleep(0.005)
    stop = 1


def get_status():
    th = threading.Thread(target=get_list)
    th.setDaemon(True)
    th.start()


def update_progress_bar():
    test_num = 0
    for k, tuple_p in enumerate(list_result):
        if tuple_p[1] != "p":
            test_num = k
            break
        if k == 99:
            test_num = 100
    percent = test_num
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
    global stop
    if stop == 0 or stop == 1:
        if stop == 1:
            stop = 2
        # 删除原节点
        for _ in map(tree.delete, tree.get_children("")):
            pass
        # 更新插入新节点
        for line in list_result:
            tree.insert("", "end", values=(line[0], line[1]))
        tree.after(50, get_tree)
    elif stop == 2:
        print("stop")
    else:
        print("something maybe wrong")


def set_cell_value(event):  # 双击进入编辑状态
    for item in tree.selection():
        item_text = tree.item(item, "values")
        print(item_text[0:2])  # 输出所选行的值
        DetailInfo(item_text[0], "pp"*100)


if __name__ == "__main__":
    root = Tk()
    root.geometry("1024x768")
    root.config(bg='#535353')

    # 进度条
    sum_length = 630
    canvas_progress_bar = Canvas(root, width=sum_length, height=20)
    canvas_shape = canvas_progress_bar.create_rectangle(0, 0, 0, 25, fill='green')
    canvas_text = canvas_progress_bar.create_text(292, 4, anchor=NW)
    canvas_progress_bar.itemconfig(canvas_text, text='00.00%')
    canvas_progress_bar.place(relx=0.45, rely=0.4, anchor=CENTER)

    t1 = Text(root)
    t1.place(relx=0.2, rely=0.7, anchor=CENTER)
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
    tree.bind('<ButtonRelease-1>', set_cell_value)

    for i in range(0, 100):
        list_result.append((i+1, "N/A"))
    get_tree()
    get_status()

    tree.grid(row=0, column=0, sticky=NSEW)
    vbar.grid(row=0, column=1, sticky=NS)

    t2 = Text(root)
    t2.place(relx=0.7, rely=0.7, anchor=CENTER)
    t3 = Text(t2)
    vbar2 = ttk.Scrollbar(t2, orient=VERTICAL, command=t3.yview)
    t3.config(yscrollcommand=vbar2.set)
    t3.grid(row=0, column=0, sticky=NSEW)
    vbar2.grid(row=0, column=1, sticky=NS)

    root.mainloop()
