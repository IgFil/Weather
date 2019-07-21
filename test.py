from tkinter import *
from tkinter import scrolledtext
import pyowm
from yandex.Translater import Translater
trans = Translater()
owm = pyowm.OWM('4613a2063bd329d8886d085321fbf742')


def clicked():
    txt.delete(1.0,END)
    trans.set_key('trnsl.1.1.20190719T155509Z.1bbb471edc0c0bc1.0a6d2b3a0871e6a62f32efb3d559b0457b464c37')
    trans.set_from_lang('en')
    trans.set_to_lang('ru')
    trans.set_default_ui('ru')
    observation = owm.weather_at_place(input1.get())
    w = observation.get_weather()
    weather_satus = w.get_detailed_status()
    weather_wind_speed = w.get_wind()['speed']
    weather_wind_deg = int(w.get_wind()['deg'])
    if 0 <= weather_wind_deg < 90:
        global weather_wind_azimut
        weather_wind_azimut = "Северный"
    if 90 <= weather_wind_deg < 180:
        weather_wind_azimut = "Восточный"
    if 180 <= weather_wind_deg < 270:
         weather_wind_azimut = "Южный"
    if 270 <= weather_wind_deg < 359:
        weather_wind_azimut = "Западный"


    trans.set_text(weather_satus)
    weather_temp_now = w.get_temperature('celsius')['temp']
    txt.insert(1.0,
    "В населённом пункте:" + str(input1.get()) + ".\n Температура сейчас:" + str(weather_temp_now) + "C°"
    + "\n Состояние:" + str(trans.translate())+"\n Ветер: "+ str(weather_wind_azimut) + "\n Скорость вертра: " + str(weather_wind_speed) + "м/c")






#Окно
root = Tk()
root.title("Погода")
root.geometry("900x600")
#Элементы
txt = scrolledtext.ScrolledText(root, width = 80 ,height=20)
lbl1 = Label(root,text="Погода V1.0(BETA)")
lbl2 = Label(root,text="Введите ваш город")
input1 = Entry(root,width=50)
btn_1 = Button(root,text="Ввод",command=clicked)
#Размещенияе
lbl1.place(x=450,y=1)
lbl2.place(x=10,y=20)
input1.place(x=130,y=22)
btn_1.place(x=10,y=40)
txt.place(x=10,y=80)
root.mainloop()

