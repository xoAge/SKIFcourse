from tkinter import *
from tkinter import messagebox
import random
import time
import copy
import os
import hashlib
def hash_parol(parol): # Хеширование пароля
    return hashlib.sha256(parol.encode('utf-8')).hexdigest()
def registr_user():     # Регистрируем пользователя
    if not login.get() or not parol.get():
        messagebox.showerror("Ошибка", "'Логин' и 'Пароль' должны быть заполнены.")
    elif proverka_logina():
        messagebox.showerror("Ошибка", "Учетная запись уже существует.")
    else:
        with open("users.txt", "a") as file:
            file.write(f"{login.get()}:{hash_parol(parol.get())}\n")
        messagebox.showinfo("Успех","Регистрация успешно завершена.\nВойдите в аккаунт")
def proverka_logina():      # Проверяем наличие логина в файле
    if os.path.exists("users.txt"):
        with open("users.txt", "r") as file:
            lines = file.readlines()
            login_vvod = login.get()
            for line in lines:
                if login_vvod in line:
                    return True
        return False
def proverka_users():  # Проверяем наличие данных в файле о пользователе
    if os.path.exists("users.txt"):
        file = open("users.txt", "r+")
        lines = file.readlines()
        login_vvod = login.get()
        parol_vvod = parol.get()
        for line in lines:
            parts = line.strip().split(':')
            if len(parts) == 2:
                sohranenii_login, sohranenii_parol = parts
                if login_vvod == sohranenii_login and hash_parol(parol_vvod) == sohranenii_parol:
                    return True
        return False
def enter_users():  # Атвторизуем пользователя
    if proverka_users():
        messagebox.showinfo("Успех!", "Вы вошли в свой аккаунт")
        root.destroy()
    else:
        messagebox.showerror("Ошибка", "Неверный логин или пароль.")
root = Tk()  # Создаем окно
root.title("Регистрация/вход")
root.geometry("400x300")
Label_login = Label(text="Логин")
Label_login.pack(padx=6, pady=6)
login = Entry(bd=2)
login.pack(padx=6, pady=6)
Label_parol = Label(text="Пароль")
Label_parol.pack(padx=6, pady=6)
parol = Entry(bd=2)
parol.pack(padx=6, pady=6)
vhod_btn1 = Button(text="Войти",command=enter_users)
vhod_btn1.pack(padx=6, pady=6)
registr_btn2 = Button(text="Зарегистрироваться",command=registr_user)
registr_btn2.pack(padx=6, pady=6)
root.mainloop()

gl_okno=Tk()#создаём окно
gl_okno.resizable(width = False, height = False)
gl_okno.title('Скифские шашки')#заголовок окна
doska=Canvas(gl_okno, width=900,height=900,bg='#FFFFFF')
doska.pack()

spisok_hodov_komputera = ()#конечный список ходов компьютера
predskazanie_hodi = 3#количество предсказываемых компьютером ходов
k_rezult=0#!!!
o_rezult=0
poz1_x=-1#клетка не задана
opredelitel_hoda_igroka=True#определение хода игрока(да)
def izobrazheniya_shashek():#загружаем изображения шашек
    global shashki
    i1=PhotoImage(file="res\\whiter.gif")
    i2=PhotoImage(file="res\\whiteq.gif")
    i3=PhotoImage(file="res\\blackr.gif")
    i4=PhotoImage(file="res\\blackq.gif")
    shashki=[0,i1,i2,i3,i4]
def novaya_igra():#начинаем новую игру
    global pole
    pole=[[3, 0, 3, 0, 4, 0, 3, 0, 3],
          [0, 3, 0, 3, 0, 3, 0, 3, 0],
          [3, 0, 3, 0, 3, 0, 3, 0, 3],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [1, 0, 1, 0, 1, 0, 1, 0, 1],
          [0, 1, 0, 1, 0, 1, 0, 1, 0],
          [1, 0, 1, 0, 2, 0, 1, 0, 1]]
def vivod_polya(x_poz_1, y_poz_1, x_poz_2, y_poz_2):#рисуем игровое поле
    global shashki
    global pole
    global kr_ramka,sin_ramka
    k=100
    x=0
    doska.delete('all')
    while x<9*k:#рисуем доску
        y=1*k
        while y<9*k:
            doska.create_rectangle(x, y, x+k, y+k,fill="pink")
            y+=2*k
        x+=2*k
    x=1*k
    while x<9*k:
        y=0
        while y<9*k:
            doska.create_rectangle(x, y, x+k, y+k,fill="pink")
            y+=2*k
        x+=2*k
    x=0
    while x<9*k:
        y=0
        while y<9*k:
            doska.create_rectangle(x, y, x+k, y+k,fill="yellow")
            y+=4*k
        x+=4*k
    x=1 * k
    while x<9*k:
        y=1*k
        while y<9*k:
            doska.create_rectangle(x, y, x+k, y+k,fill="yellow")
            y+=6*k
        x+=6*k
    x = 2 * k
    while x < 9 * k:
        y = 2 * k
        while y < 9 * k:
            doska.create_rectangle(x, y, x + k, y + k, fill="yellow")
            y += 4 * k
        x += 4 * k
    x = 3 * k
    while x < 7 * k:
        y = 3 * k
        while y < 7 * k:
            doska.create_rectangle(x, y, x + k, y + k, fill="yellow")
            y += 2 * k
        x += 2 * k
    x = 0
    while x < 9 * k:
        y = 2 * k
        while y < 9 * k:
            doska.create_rectangle(x, y, x + k, y + k, fill="green")
            y += 4 * k
        x += 8 * k
    x = 2*k
    while x < 9 * k:
        y = 0
        while y < 9 * k:
            doska.create_rectangle(x, y, x + k, y + k, fill="green")
            y += 8 * k
        x += 4 * k
    x = 1 * k
    while x < 9 * k:
        y = 3*k
        while y < 7 * k:
            doska.create_rectangle(x, y, x + k, y + k, fill="green")
            y += 2 * k
        x += 6 * k
    x = 3 * k
    while x < 7 * k:
        y = 1 * k
        while y < 8 * k:
            doska.create_rectangle(x, y, x + k, y + k, fill="green")
            y += 6 * k
        x += 2 * k
    x = 4 * k
    while x < 7 * k:
        y = 2 * k
        while y < 8 * k:
            doska.create_rectangle(x, y, x + k, y + k, fill="green")
            y += 4 * k
        x += 6 * k
    x = 2 * k
    while x < 7 * k:
        y = 4 * k
        while y < 8 * k:
            doska.create_rectangle(x, y, x + k, y + k, fill="green")
            y += 8 * k
        x += 4 * k
    kr_ramka = doska.create_rectangle(-5, -5, -5, -5, outline="red", width=5)
    sin_ramka = doska.create_rectangle(-5, -5, -5, -5, outline="blue", width=5)
    for y in range(9):#рисуем шашки
        for x in range(9):
            z=pole[y][x] #по строкам y и столбцам x
            if z:
                if (x_poz_1,y_poz_1)!=(x,y):
                    doska.create_image(x*k,y*k, anchor=NW, image=shashki[z])
    z=pole[y_poz_1][x_poz_1] #рисуем активную шашку
    if z: #если позиция не равна 0, т. е. есть шашка
        doska.create_image(x_poz_1*k,y_poz_1*k, anchor=NW, image=shashki[z],tag='ani')
    kx = 1 if x_poz_1<x_poz_2 else -1 #анимация
    ky = 1 if y_poz_1<y_poz_2 else -1
    for i in range(abs(x_poz_1-x_poz_2)): #анимация перемещения шашки
        for ii in range(33):
            doska.move('ani',0.03*k*kx,0.03*k*ky)
            doska.update()
            time.sleep(0.01)
def soobsenie(s): #сообщение об окончании игры
    global opredelitel_hoda_igroka
    z='Игра завершена'
    if s==1:
        i=messagebox.askyesno(title=z, message='Вы победили!\nХотите ли сыграть еще раз?',icon='info')
    if s==2:
        i=messagebox.askyesno(title=z, message='Вы проиграли!\nХотите ли сыграть еще раз?',icon='info')
    if s==3:
        i=messagebox.askyesno(title=z, message='Ходов больше нет.\nХотите ли сыграть еще раз?',icon='info')
    if i:
        novaya_igra()
        vivod_polya(-1, -1, -1, -1)#рисуем игровое поле
        opredelitel_hoda_igroka=True#ход игрока доступен
    if not i:
        gl_okno.destroy()
def pozici_1(event):#выбор клетки для хода 1
    x,y=(event.x)//100,(event.y)//100#вычисляем координаты клетки
    doska.coords(sin_ramka, x * 100, y * 100, x * 100 + 100, y * 100 + 100)#рамка в выбранной клетке
def pozici_2(event):#выбор клетки для хода 2
    global poz1_x,poz1_y,poz2_x,poz2_y
    global opredelitel_hoda_igroka
    x,y=(event.x)//100,(event.y)//100#вычисляем координаты клетки
    if pole[y][x]==1 or pole[y][x]==2:#проверяем шашку игрока в выбранной клетке
        doska.coords(kr_ramka,x*100,y*100,x*100+100,y*100+100)#рамка в выбранной клетке
        poz1_x,poz1_y=x,y
    else:
        if poz1_x!=-1:#клетка выбрана
            poz2_x,poz2_y=x,y
            if opredelitel_hoda_igroka:#ход игрока
                hod_igroka()
                if not(opredelitel_hoda_igroka):
                    time.sleep(0.5)
                    hod_komp()#передаём ход компьютеру
            poz1_x=-1#клетка не выбрана
def hod_komp():
    global opredelitel_hoda_igroka
    global spisok_hodov_komputera
    proverka_hodov_komp(1, (), [])
    if spisok_hodov_komputera:#проверяем наличие доступных ходов
        kol_hodov=len(spisok_hodov_komputera)#количество ходов
        th=random.randint(0,kol_hodov-1)#генерируем случайное целое число в диапазоне от 0 до `kol_hodov-1` и сохраняем его в переменной.
                                 # Это число будет использоваться для выбора случайного хода из списка `spisok_hodov_komputera`
        deep_hoda=len(spisok_hodov_komputera[th])#вычисляем длину выбранного случайного хода из списка `spisok_hodov_komputera`
        for i in range(deep_hoda-1):
            peredvizenie_shashki(1, spisok_hodov_komputera[th][i][0], spisok_hodov_komputera[th][i][1], #выполняем ход
                                 spisok_hodov_komputera[th][1 + i][0], spisok_hodov_komputera[th][1 + i][1])
        spisok_hodov_komputera=[]#очищаем список ходов
        opredelitel_hoda_igroka=True#ход игрока доступен
    s_komp,s_igrok=podschet() #определяем победителя
    if not(s_igrok):
            soobsenie(2)
    elif not(s_komp):
            soobsenie(1)
    elif opredelitel_hoda_igroka and not(spisok_hodov_igroka()):
            soobsenie(3)
    elif not(opredelitel_hoda_igroka) and not(spisok_hodov_komp()):
            soobsenie(3)
def spisok_hodov_komp():#составляем список ходов компьютера
    spisok=prosmotr_hodov_k1([])#здесь проверяем обязательные ходы
    if not(spisok):
        spisok=prosmotr_hodov_k2([])#здесь проверяем оставшиеся ходы
    return spisok
def proverka_hodov_komp(tekh_hod, n_spisok, spisok):
    global pole
    global spisok_hodov_komputera
    global l_rezult,k_rezult,o_rezult
    if not(spisok): #если список ходов пустой
        spisok=spisok_hodov_komp() #заполняем
    if spisok:
        k_pole=copy.deepcopy(pole)#копируем поле
        for ((poz1_x,poz1_y),(poz2_x,poz2_y)) in spisok:#проходим все ходы по списку
            t_spisok=peredvizenie_shashki(0, poz1_x, poz1_y, poz2_x, poz2_y)
            if t_spisok:#если существует ещё ход
                proverka_hodov_komp(tekh_hod, (n_spisok + ((poz1_x, poz1_y),)), t_spisok)
            else:
                proverka_hodov_igroka(tekh_hod, [])
                if tekh_hod==1:
                    t_rez=o_rezult/k_rezult
                    if not(spisok_hodov_komputera):#записываем если пустой
                        spisok_hodov_komputera=(n_spisok+((poz1_x,poz1_y),(poz2_x,poz2_y)),)
                        l_rezult=t_rez#сохряняем наилучший результат
                    else:
                        if t_rez==l_rezult:
                            spisok_hodov_komputera=spisok_hodov_komputera+(n_spisok+((poz1_x,poz1_y),(poz2_x,poz2_y)),)
                        if t_rez>l_rezult:
                            spisok_hodov_komputera=()
                            spisok_hodov_komputera=(n_spisok+((poz1_x,poz1_y),(poz2_x,poz2_y)),)
                            l_rezult=t_rez#сохряняем наилучший результат
                    o_rezult, k_rezult = 0, 0
            pole=copy.deepcopy(k_pole)#возвращаем поле
    else:
        s_komp,s_igrok=podschet()#подсчёт результата хода
        o_rezult+=(s_komp-s_igrok)
        k_rezult+=1
def spisok_hodov_igroka():#составляем список ходов игрока
    spisok=prosmotr_hodov_i1([])#здесь проверяем обязательные ходы
    if not(spisok):
        spisok=prosmotr_hodov_i2([])#здесь проверяем оставшиеся ходы
    return spisok
def proverka_hodov_igroka(tekh_hod, spisok):
    global pole,k_rezult,o_rezult
    global predskazanie_hodi
    if not(spisok):
        spisok=spisok_hodov_igroka()
    if spisok:#проверяем наличие доступных ходов
        k_pole=copy.deepcopy(pole)#копируем поле
        for ((poz1_x,poz1_y),(poz2_x,poz2_y)) in spisok:
            t_spisok=peredvizenie_shashki(0, poz1_x, poz1_y, poz2_x, poz2_y)
            if t_spisok:#если существует ещё ход
                proverka_hodov_igroka(tekh_hod, t_spisok)
            else:
                if tekh_hod<predskazanie_hodi:
                    proverka_hodov_komp(tekh_hod + 1, (), [])
                else:
                    s_komp,s_igrok=podschet()#подсчёт результата хода
                    o_rezult+=(s_komp-s_igrok)
                    k_rezult+=1
            pole=copy.deepcopy(k_pole)#возвращаем поле
    else:#доступных ходов нет
        s_komp,s_igrok=podschet()#подсчёт результата хода
        o_rezult+=(s_komp-s_igrok)
        k_rezult+=1
def podschet():#подсчёт шашек на поле
    global pole
    s_igrok=0
    s_komp=0
    for i in range(9):
        for ii in pole[i]:
            if ii==1:s_igrok+=1
            if ii==2:s_igrok+=2
            if ii==3:s_komp+=1
            if ii==4:s_komp+=2
    return s_komp,s_igrok
def hod_igroka():
    global poz1_x,poz1_y,poz2_x,poz2_y
    global opredelitel_hoda_igroka
    opredelitel_hoda_igroka=False#считаем ход игрока выполненным
    spisok=spisok_hodov_igroka()
    if spisok:
        if ((poz1_x,poz1_y),(poz2_x,poz2_y)) in spisok:#проверяем ход на соответствие правилам игры
            t_spisok=peredvizenie_shashki(1, poz1_x, poz1_y, poz2_x, poz2_y)#если всё хорошо, делаем ход
            if t_spisok:#если есть ещё ход той же шашкой
                opredelitel_hoda_igroka=True#считаем ход игрока невыполненным
        else:
            opredelitel_hoda_igroka=True#считаем ход игрока невыполненным
    doska.update()
def peredvizenie_shashki(f, poz1_x, poz1_y, poz2_x, poz2_y):
    global pole
    if f:vivod_polya(poz1_x, poz1_y, poz2_x, poz2_y)#рисуем игровое поле
    if poz2_y==0 and pole[poz1_y][poz1_x]==1: #превращение
        pole[poz1_y][poz1_x]=2
    if poz2_y==8 and pole[poz1_y][poz1_x]==3:
        pole[poz1_y][poz1_x]=4
    pole[poz2_y][poz2_x]=pole[poz1_y][poz1_x]
    pole[poz1_y][poz1_x]=0
    kx=ky=1  #перепрыгиваем шашку игрока
    if poz1_x<poz2_x:kx=-1  # если координаты x позиции начальной шашки меньше координаты x позиции конечной шашки
    if poz1_y<poz2_y:ky=-1 # если координаты y позиции начальной шашки меньше координаты y позиции конечной шашки
    x_poz,y_poz=poz2_x,poz2_y # переменные x_poz и y_poz устанавливаются равными координатам конечной позиции шашки
    while (poz1_x!=x_poz) or (poz1_y!=y_poz): # переменные x_poz и y_poz устанавливаются равными координатам конечной позиции шашки
        x_poz+=kx
        y_poz+=ky
        # перебираем все клетки на пути атакующей шашки от начальной до конечной позиции
        if pole[y_poz][x_poz]!=0: # если текущая клетка на игровом поле не пуста, то она считается занятой шашкой противника...
            pole[y_poz][x_poz]=0 #эта шашка удаляется из игры
            if f:vivod_polya(-1, -1, -1, -1)#рисуем игровое поле
            #проверяем ход той же шашкой
            if pole[poz2_y][poz2_x]==3 or pole[poz2_y][poz2_x]==4:#компьютера
                return prosmotr_hodov_k1p([],poz2_x,poz2_y)#возвращаем список доступных ходов
            elif pole[poz2_y][poz2_x]==1 or pole[poz2_y][poz2_x]==2:#игрока
                return prosmotr_hodov_i1p([],poz2_x,poz2_y)#возвращаем список доступных ходов
    if f:vivod_polya(poz1_x, poz1_y, poz2_x, poz2_y)#рисуем игровое поле
def prosmotr_hodov_k1(spisok):#проверка наличия обязательных ходов
    for y in range(9):#сканируем всё поле
        for x in range(9):
            spisok=prosmotr_hodov_k1p(spisok,x,y)
    return spisok
def prosmotr_hodov_k1p(spisok,x,y):
    if pole[y][x]==3:#шашка
        for ix,iy in (-1,-1),(-1,1),(1,-1),(1,1):
            if 0<=y+iy+iy<=8 and 0<=x+ix+ix<=8:
                if pole[y+iy][x+ix]==1 or pole[y+iy][x+ix]==2:  # проверяем возможность "перепрыгнуть" через вражескую шашку
                    if pole[y+iy+iy][x+ix+ix]==0: # понимаем, что есть возможность сделать ход, так как клетка равна 0
                        spisok.append(((x,y),(x+ix+ix,y+iy+iy)))#запись хода в конец списка
    if pole[y][x]==4:#шашка с короной
        for ix,iy in (-1,-1),(-1,1),(1,-1),(1,1):
            true_hod=0#определение правильности хода
            for i in  range(1,9):
                if 0<=y+iy*i<=8 and 0<=x+ix*i<=8:
                    if true_hod==1:
                        spisok.append(((x,y),(x+ix*i,y+iy*i)))#запись хода в конец списка
                    if pole[y+iy*i][x+ix*i]==1 or pole[y+iy*i][x+ix*i]==2:
                        true_hod+=1
                    if pole[y+iy*i][x+ix*i]==3 or pole[y+iy*i][x+ix*i]==4 or true_hod==2:
                        if true_hod>0:spisok.pop()#удаление хода из списка
                        break
    return spisok
def prosmotr_hodov_k2(spisok):#проверка наличия остальных ходов
    for y in range(9):#сканируем всё поле
        for x in range(9):
            if pole[y][x]==3:#шашки
                for ix,iy in (-1,1),(1,1):
                    if 0<=y+iy<=8 and 0<=x+ix<=8:
                        if pole[y+iy][x+ix]==0:
                            spisok.append(((x,y),(x+ix,y+iy)))#запись хода в конец списка
                        if pole[y+iy][x+ix]==1 or pole[y+iy][x+ix]==2:
                            if 0<=y+iy*2<=8 and 0<=x+ix*2<=8:
                                if pole[y+iy*2][x+ix*2]==0:
                                    spisok.append(((x,y),(x+ix*2,y+iy*2)))#запись хода в конец списка
            if pole[y][x]==4:#шашка с короной
                for ix,iy in (-1,-1),(-1,1),(1,-1),(1,1):
                    true_hod=0#определение правильности хода
                    for i in range(1,9):
                        if 0<=y+iy*i<=8 and 0<=x+ix*i<=8:
                            if pole[y+iy*i][x+ix*i]==0:
                                spisok.append(((x,y),(x+ix*i,y+iy*i)))#запись хода в конец списка
                            if pole[y+iy*i][x+ix*i]==1 or pole[y+iy*i][x+ix*i]==2:
                                true_hod+=1
                            if pole[y+iy*i][x+ix*i]==3 or pole[y+iy*i][x+ix*i]==4 or true_hod==2:
                                break
    return spisok
def prosmotr_hodov_i1(spisok):#проверка наличия обязательных ходов
    spisok=[]#список ходов
    for y in range(9):#сканируем всё поле
        for x in range(9):
            spisok=prosmotr_hodov_i1p(spisok,x,y)
    return spisok
def prosmotr_hodov_i1p(spisok,x,y):
    if pole[y][x]==1:#шашки
        for ix,iy in (-1,-1),(-1,1),(1,-1),(1,1):
            if 0<=y+iy+iy<=8 and 0<=x+ix+ix<=8:
                if pole[y+iy][x+ix]==3 or pole[y+iy][x+ix]==4:
                    if pole[y+iy+iy][x+ix+ix]==0:
                        spisok.append(((x,y),(x+ix+ix,y+iy+iy)))#запись хода в конец списка
    if pole[y][x]==2:#шашка с короной
        for ix,iy in (-1,-1),(-1,1),(1,-1),(1,1):
            true_hod=0#определение правильности хода
            for i in  range(1,9):
                if 0<=y+iy*i<=8 and 0<=x+ix*i<=8:
                    if true_hod==1:
                        spisok.append(((x,y),(x+ix*i,y+iy*i)))#запись хода в конец списка
                    if pole[y+iy*i][x+ix*i]==3 or pole[y+iy*i][x+ix*i]==4:
                        true_hod+=1 # увеличиваем на 1, если на пути встречается вражеская фигура
                    if pole[y+iy*i][x+ix*i]==1 or pole[y+iy*i][x+ix*i]==2 or true_hod==2: #если на пути встречается своя фигура
                        if true_hod>0:spisok.pop()#удаление хода из списка
                        break
    return spisok
def prosmotr_hodov_i2(spisok):      #проверка наличия остальных ходов
    for y in range(9):      #сканируем всё поле
        for x in range(9):
            if pole[y][x]==1:       #шашка
                for ix,iy in (-1,-1),(1,-1):
                    if 0<=y+iy<=8 and 0<=x+ix<=8:
                        if pole[y+iy][x+ix]==0:
                            spisok.append(((x,y),(x+ix,y+iy)))      #запись хода в конец списка
                        if pole[y+iy][x+ix]==3 or pole[y+iy][x+ix]==4:
                            if 0<=y+iy*2<=8 and 0<=x+ix*2<=8:
                                if pole[y+iy*2][x+ix*2]==0:
                                    spisok.append(((x,y),(x+ix*2,y+iy*2)))      #запись хода в конец списка
            if pole[y][x]==2:     #шашка с короной
                for ix,iy in (-1,-1),(-1,1),(1,-1),(1,1):
                    true_hod=0      #определение правильности хода
                    for i in range(1,9):
                        if 0<=y+iy*i<=8 and 0<=x+ix*i<=8:
                            if pole[y+iy*i][x+ix*i]==0:
                                spisok.append(((x,y),(x+ix*i,y+iy*i)))#запись хода в конец списка
                            if pole[y+iy*i][x+ix*i]==3 or pole[y+iy*i][x+ix*i]==4:
                                true_hod+=1
                            if pole[y+iy*i][x+ix*i]==1 or pole[y+iy*i][x+ix*i]==2 or true_hod==2:
                                break
    return spisok
izobrazheniya_shashek()  # здесь загружаем изображения шашек
novaya_igra()  # начинаем новую игру
vivod_polya(-1, -1, -1, -1)  # рисуем игровое поле
doska.bind("<Motion>", pozici_1)  # движение мышки по полю
doska.bind("<Button-1>", pozici_2)  # нажатие левой кнопки
mainloop()