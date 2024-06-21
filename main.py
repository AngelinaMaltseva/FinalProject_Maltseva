from Apartments_for_rent.Apartment import Apartment
if __name__ == '__main__':
    apartment = Apartment("Дубна, Университетская, 19", 300, 5, 4000, "Отличный вариант для семьи. Рядом парк, больница, магазины, школы")
    print(apartment)
    from tkinter import *
    root = Tk() # создаем корневой объект - окно
    root.title("аренда квартир") # устанавливаем заголовок окна
    root.geometry ("600x400") # устанавливаем размер окна

    label_address = Label(text="Введите адрес") # создаем текстовую метку
    # поле ввода для адреса
    label_address.pack()# размещаем текстовую метку в окне
    entry_address = Entry() # создаем поле ввода
    entry_address.pack() # размещаем поле ввода в окне
    label_square = Label(text="Площадь") # создаем текстовую метку
    label_square.pack()# размещаем текстовую метку в окне
    # поле ввода для площади
    entry_square = Entry() # создаем поле ввода
    entry_square.pack() # размещаем поле ввода в окне
    label_number_of_rooms = Label(text="Количество комнат") # создаем текстовую метку
    label_number_of_rooms.pack()# размещаем текстовую метку в окне
    # поле ввода для количества комнат
    entry_number_of_rooms = Entry() # создаем поле ввода
    entry_number_of_rooms.pack() # размещаем поле ввода в окне
    label_rent_price = Label(text="Стоимость аренды за сутки") # создаем текстовую метку
    label_rent_price.pack()# размещаем текстовую метку в окне
    # поле ввода для стоимости аренды за сутки
    entry_rent_price = Entry() # создаем поле ввода
    entry_rent_price.pack() # размещаем поле ввода в окне
    label_description = Label(text="Описание")# создаем текстовую метку
    label_description.pack() # размещаем текстовую метку в окне
    # поле ввода для описания
    entry_description = Entry() # создаем поле ввода
    entry_description.pack() # размещаем поле ввода в окне
# кнопка для добавления квартиры
    btn_add_apartment = Button(text="Добавить квартиру")
    btn_add_apartment.pack()
list_flat = [] # список для хранения квартир
# создать объект "квартира"
apartment = Apartment("Дубна, Университетская, 19", 300, 5, 4000, "Отличный вариант для семьи. Рядом парк, больница, магазины, школы")
# добавить объект в список
list_flat.append(apartment)
# сохранить созданный и заполненный объект в переменную Variable
list_flat_var = Variable(value=list_flat)
# создать ListBox, шириной 50 символов,
# в котором будет отображаться список list_flat_var
apartments_listbox = Listbox(width=50, listvariable=list_flat_var)
# добавить ListBox на форму
apartments_listbox.pack()
def add_apartment():
    # для считывания данных из поля ввода
    # используется метод get()
    address = entry_address.get()
    square = entry_square.get()
    number_of_rooms = entry_number_of_rooms.get()
    rent_price = entry_rent_price.get()
    description = entry_description.get()
    # создается объект
    apartment = Apartment (address, square,number_of_rooms,rent_price,description)
    # добавить обЪект в список
    list_flat.append(apartment)
    # обновить ListBox
    list_flat_var.set(list_flat)

def delete():
    # получить индекс выбранного элемента
    index = apartments_listbox.curselection()
    # удалить элемент
    # remove удаляет по значению, а не по индексу
    # index[0] - так как curselection()
    # возвращает список всех выбранных элементов
    # берем единственный, поэтому указываем индекс 0
    list_flat_var.set(list_flat[index[0]])
    # и переопределяем ListBox
    list_flat_var.set(list_flat)
def rental():
    index = apartments_listbox.curselection()
    list_flat[index[0]].to_rent()
    list_flat_var.set(list_flat)
def cancel():
    index = apartments_listbox.curselection()
    list_flat[index[0]],cancel_rental()
    list_flat_var.set(list_flat)
# кнопка для удаления квартиры
btn_del_apartment = Button(text="Удалить", command=delete)
btn_del_apartment.pack()
# кнопка "Сдать квартиру"
btn_rent_apartment = Button(text="Сдать квартиру", command=rental)
btn_rent_apartment.pack()
# кнопка "Освободить квартиру"
btn_change_rent_apartment = Button(text="Освободить квартиру", command=cancel)
btn_change_rent_apartment.pack()

# кнопка всегда должна быть последней
root.mainloop()