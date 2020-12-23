from random import *
from guizero import *
import time
# TODO: -Read sensor for CO2 and H20
#       -Convert analog input to digital (for sensors)
#       -Save data in txt file

pies=0 #SCFH shown by sensor
pies_acumulado=0 #CO2 used up until now (lbs)
gal=0 #Gallons used given by pulse(GPM)
gal_acum = 0 #Gallons used up until now (ac/ft)

#KeyPad Functions, just for input on touchscreen
def Keypad__1():
   input_water.append('1')
def Keypad__2():
   input_water.append('2')
def Keypad__3():
   input_water.append('3')
def Keypad__4():
   input_water.append('4')
def Keypad__5():
   input_water.append('5')
def Keypad__6():
   input_water.append('6')
def Keypad__7():
   input_water.append('7')
def Keypad__8():
   input_water.append('8')
def Keypad__9():
   input_water.append('9')
def Keypad__0():
   input_water.append('0')
def Clearapp():
   input_water.clear()

#Close the program (Exit button)
def goto_main():
    exit()

#Read sensor for CO2 and H2O
def read_sensor():
    return random()*5

def read_sensor_h2o():
    return random()*500

#Change value of gallons
def change_gal():
    global gal
    gal = round(read_sensor_h2o(),2)
    text_3.value = gal

#Change value of ac/ft
def change_gal_acum():
    global gal_acum
    gal_acum+=round((gal/325851),3)
    text_3_1.value=gal_acum

#Manual change (for systems without flowmeter)
def change_gal_acum_manual():
    global input_water
    global gal_acum
    gal_acum+=int(input_water.value)
    text_3_1.value = round(gal_acum/325857,3)

#Change value of scfh
def change_feet():
    global pies
    pies =round((read_sensor() * 40)*2.118876,2)
    text.value = pies

#Change value of lbs
def change_feet_acum():
    global pies_acumulado
    pies_acumulado+=pies
    text_2.value = round(pies_acumulado*0.11379227,2)

#Window for auto mode
def change_mode_auto():
    global text
    global text_2
    global text_3
    global text_3_1
    app.hide()
    window_1.set_full_screen()
    window_1.show()
    Sensor = Text(window_1, 'Sensor value:',size=50)
    title_box = Box(window_1,layout='grid',height="fill")
    text = Text(title_box, "0",grid=[0,1],size=50)
    unidades = Text(title_box, "[SCFH]",grid=[1,1],size=50)
    Acum = Text(window_1, 'Usage:',size=50)
    title_box_2 = Box(window_1,layout='grid',height="fill")
    text_2 = Text(title_box_2,"0",grid=[0,1],size=50)
    unidades_2 = Text(title_box_2,"[lbs]",grid=[1,1],size=50)
    Water_sensor = Text(window_1,'Water flow:',size=25)
    title_box_3 = Box(window_1,layout='grid',height="fill")
    text_3 = Text(title_box_3,"0",grid=[0,1],size=25)
    unidades_3 = Text(title_box_3,"[GPM]",grid=[1,1],size=25)
    text_3_1=Text(title_box_3,"0",grid=[0,2],size=25)
    unidades_3_1 = Text(title_box_3,"[ac/ft]",grid=[1,2],size=25)
    menu = PushButton(window_1,command=goto_main, text="Exit",width=8,height=4)
    text_3.repeat(10000,change_gal)
    text_3_1.repeat(10000,change_gal_acum)
    text.repeat(10000, change_feet)
    text_2.repeat(10000,change_feet_acum)

#Window for manual mode
def change_mode_manual():
    global text
    global text_2
    global text_3
    global text_3_1
    window_2.hide()
    window_3.set_full_screen()
    window_3.show()
    Sensor = Text(window_3, 'Flow:',size=50)
    title_box = Box(window_3,layout='grid',height="fill")
    text = Text(title_box, "0",grid=[0,1],size=50)
    unidades = Text(title_box, "[SCFH]",grid=[1,1],size=50)
    Acum = Text(window_3, 'Usage:',size=50)
    title_box_2 = Box(window_3,layout='grid',height="fill")
    text_2 = Text(title_box_2,"0",grid=[0,1],size=50)
    unidades_2 = Text(title_box_2,"[lbs]",grid=[1,1],size=50)
    Water_sensor = Text(window_3,'Water flow:',size=25)
    title_box_3 = Box(window_3,layout='grid',height="fill")
    text_3 = Text(title_box_3,input_water.value,grid=[0,1],size=25)
    unidades_3 = Text(title_box_3,"[GPM]",grid=[1,1],size=25)
    text_3_1=Text(title_box_3,"0",grid=[0,2],size=25)
    unidades_3_1 = Text(title_box_3,"[ac/ft]",grid=[1,2],size=25)
    menu = PushButton(window_3,command=goto_main, text="Exit",width=8,height=4)
    text_3_1.repeat(10000,change_gal_acum_manual)
    text.repeat(10000, change_feet)
    text_2.repeat(10000,change_feet_acum)

#Window to input GPM (for systems without flowmeter)
def input_mode():
    global input_water
    app.hide()
    window_2.set_full_screen()
    window_2.show()
    input_text = Text(window_2,text="Enter your flow in GPM",size=32)
    input_water = TextBox(window_2,width="fill") #Input textbox
    buttons = Box(window_2,layout='grid') #Box for "Enter" and "Clear" buttons
    button_input = PushButton(buttons,text="Enter",command=change_mode_manual,grid=[0,0],width=8,height=4) #Enter the input and go to manual mode window
    Clear_app = PushButton(buttons, Clearapp, text="Clear",grid=[1,0],width=8,height=4) #Clear input
    keypad = Box(window_2,layout='grid') #Box for KeyPad
    #Keypad
    Keypad_1 = PushButton(keypad, Keypad__1, text="1",grid=[0,0],width=8,height=4)
    Keypad_2 = PushButton(keypad, Keypad__2, text="2",grid=[1,0],width=8,height=4)
    Keypad_3 = PushButton(keypad, Keypad__3, text="3",grid=[2,0],width=8,height=4)
    Keypad_4 = PushButton(keypad, Keypad__4, text="4",grid=[0,1],width=8,height=4)
    Keypad_5 = PushButton(keypad, Keypad__5, text="5",grid=[1,1],width=8,height=4)
    Keypad_6 = PushButton(keypad, Keypad__6, text="6",grid=[2,1],width=8,height=4)
    Keypad_7 = PushButton(keypad, Keypad__7, text="7",grid=[0,2],width=8,height=4)
    Keypad_8 = PushButton(keypad, Keypad__8, text="8",grid=[1,2],width=8,height=4)
    Keypad_9 = PushButton(keypad, Keypad__9, text="9",grid=[2,2],width=8,height=4)
    Keypad_0 = PushButton(keypad, Keypad__0, text="0",grid=[1,3],width=8,height=4)
    ####
    menu = PushButton(window_2,command=goto_main, text="Exit",width=8,height=4) #Exit button

#Main loop
if __name__ =='__main__':
    app = App(title="Flow",width=1024,height=600) #Main app, to select the mode
    app.set_full_screen()
    window_1 = Window(app,title="Flow",width=1024,height=600) #Window for auto mode
    window_1.hide()
    window_2 = Window(app,title="Flow",width=1024,height=600) #Window for input
    window_2.hide()
    window_3 = Window(app,title="Flow",width=1024,height=600) #Window for manual mode
    window_3.hide()
    button = PushButton(app, command=change_mode_auto,text="Auto mode",align="top",width="fill",height="fill") #Go to Auto mode
    button.text_size=50
    button_2 = PushButton(app,command=input_mode,text="Manual mode",align="bottom",width="fill",height="fill") #Go to Manual mode
    button_2.text_size=50
    app.display()
