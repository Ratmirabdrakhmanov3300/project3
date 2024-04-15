import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
def newfile():
    text.delete('1.0', tk.END)

def openfile():
    name = askopenfilename()
    f = open(name, 'r')
    text.delete('1.0', tk.END)
    text.insert('1.0', f.read())
    f.close()

def savefile():
    f = open(asksaveasfilename(), 'w')
    f.write(text.get('1.0', tk.END))
    f.close()

def about():
    tk.messagebox.showinfo(title="О программе ", message='Редактор версия 1.0')

def help_cmd():
    help_win = tk.Toplevel(win)
    help_win.title('Окно помощи')
    help_win.geometry('800x600')
    help_text = tk.Text(help_win)
    help_text.pack(expand=True, fill='both')
    f = open('helpfile.txt', 'r')
    help_text.delete('1.0', tk.END)
    help_text.insert('1.0', f.read())
    f.close()


win = tk.Tk()
win.title('Блокнот')
win.geometry('600x400')

text = tk.Text(win)
text.pack(expand=True, fill='both')

mainmenu = tk.Menu(win)

filemenu = tk.Menu(mainmenu, tearoff=0)
filemenu.add_command(label='Новый', command=newfile)
filemenu.add_command(label='Открыть', command=openfile)
filemenu.add_command(label='Сохранить', command=savefile)
filemenu.add_separator()
filemenu.add_command(label='Закрыть', command=win.destroy)

helpmenu = tk.Menu(mainmenu, tearoff=0)
helpmenu.add_command(label="Справка", command=help_cmd)
helpmenu.add_command(label="О программе", command=about)

mainmenu.add_cascade(label='Файл', menu=filemenu)
mainmenu.add_cascade(label='Помощь', menu=helpmenu)
win.config(menu=mainmenu)

win.mainloop()