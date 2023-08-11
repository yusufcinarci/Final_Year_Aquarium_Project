import tkinter as tk
from tkinter import messagebox
import webbrowser
import cv2
import numpy as np
import pigpio
from tkinter import *
#import pytesseract
import datetime
from time import sleep
import RPi.GPIO as GPIO
import time
import os
import glob
from PigpioStepperMotor import StepperMotor


pi = pigpio.pi()



TRIG = 23
ECHO = 24
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

A = 5
B = 6
C = 13
D = 19


GPIO.setup(14,GPIO.OUT) #Relay IN4 for Ligth
GPIO.setup(15,GPIO.OUT) #Relay IN3 for Pump_1
GPIO.setup(7,GPIO.OUT)  #Relay IN2 for Pump_2
GPIO.setup(25,GPIO.OUT)  #Relay IN1 for Cooler_Fan
GPIO.setup(26,GPIO.IN)  #For water leak

#To read Aquarium WAter Level
#-------------------------------------------------------
#def read_AquaWaterLevel():

GPIO.output(14,GPIO.HIGH)
GPIO.output(15,GPIO.HIGH)
GPIO.output(7,GPIO.HIGH)
GPIO.output(25,GPIO.HIGH)

GPIO.setup(A, GPIO.OUT) #
GPIO.setup(B, GPIO.OUT) #For Stepper Motor
GPIO.setup(C, GPIO.OUT) #
GPIO.setup(D, GPIO.OUT) #


def GPIO_SETUP(a,b,c,d):
        GPIO.output(A, a)
        GPIO.output(B, b)
        GPIO.output(C, c)
        GPIO.output(D, d)
        time.sleep(0.001)
        
def Fish_Feeder_RTURN(deg):

        full_circle = 510.0
        degree = full_circle/360*deg
        GPIO_SETUP(0,0,0,0)
        
        
        while degree > 0.0:
            GPIO_SETUP(1,0,0,0)
            GPIO_SETUP(1,1,0,0)
            GPIO_SETUP(0,1,0,0)
            GPIO_SETUP(0,1,1,0)
            GPIO_SETUP(0,0,1,0)
            GPIO_SETUP(0,0,1,1)
            GPIO_SETUP(0,0,0,1)
            GPIO_SETUP(1,0,0,1)
            degree -= 1
        GPIO_SETUP(0,0,0,0)
        
def Fish_Feeder_LTURN(deg):

        full_circle = 510.0
        degree = full_circle/360*deg
        GPIO_SETUP(0,0,0,0)

        while degree > 0.0:
            GPIO_SETUP(1,0,0,1)
            GPIO_SETUP(0,0,0,1)
            GPIO_SETUP(0,0,1,1)
            GPIO_SETUP(0,0,1,0)
            GPIO_SETUP(0,1,1,0)
            GPIO_SETUP(0,1,0,0)
            GPIO_SETUP(1,1,0,0)
            GPIO_SETUP(1,0,0,0)
            degree -= 1
        GPIO_SETUP(0,0,0,0)
#motor = StepperMotor(29,31,33,35)

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28-3c8af648382f')[0] #serial number of my sensor
device_file = device_folder + '/w1_slave'

pi.set_PWM_dutycycle(17, 255)
pi.set_PWM_dutycycle(22, 255)


pencere = tk.Tk()

img = PhotoImage(file="/home/fortytwo/Desktop/image3")
fotograf = Label(pencere,image=img)
fotograf.place(x=0, y=0)

entry = tk.Entry(state='disabled',bd=5,disabledbackground="white",disabledforeground="black",width=27,font="bold")
entry.place(x=280, y=366)

entry2 = tk.Entry(state='disabled',bd=5,disabledbackground="white",disabledforeground="black",width=27,font="bold")
entry2.place(x=280, y=416)

entry3 = tk.Entry(state='disabled',bd=5,disabledbackground="white",disabledforeground="black",width=27,font="bold")
entry3.place(x=280, y=460)

entry4 = tk.Entry(bd=5,disabledbackground="white",disabledforeground="black",width=8,font="bold")
entry4.place(x=200, y=110)
###########################################

#############################################
#Kamera


new = 1
url = "http://10.106.1.216:8090/stream"
def openweb():
    webbrowser.open(url, new=new)
    
    
####################################################
url2 = "http://10.106.1.216:8090/stream/snapshot.jpeg?delay_s=0"
new = 2
def ekran_goruntusu():
    webbrowser.open(url2, new=new)
    
    


######################################################
#YEMLEME SİSTEMİ
def yem_at():
    """
    GPIO.setup(A, GPIO.OUT) #
    GPIO.setup(B, GPIO.OUT) #For Stepper Motor
    GPIO.setup(C, GPIO.OUT) #
    GPIO.setup(D, GPIO.OUT) #


    def GPIO_SETUP(a,b,c,d):
        GPIO.output(A, a)
        GPIO.output(B, b)
        GPIO.output(C, c)
        GPIO.output(D, d)
        time.sleep(0.001)
        
    def Fish_Feeder_RTURN(deg):

        full_circle = 510.0
        degree = full_circle/360*deg
        GPIO_SETUP(0,0,0,0)
        
        
        while degree > 0.0:
            GPIO_SETUP(1,0,0,0)
            GPIO_SETUP(1,1,0,0)
            GPIO_SETUP(0,1,0,0)
            GPIO_SETUP(0,1,1,0)
            GPIO_SETUP(0,0,1,0)
            GPIO_SETUP(0,0,1,1)
            GPIO_SETUP(0,0,0,1)
            GPIO_SETUP(1,0,0,1)
            degree -= 1
        GPIO_SETUP(0,0,0,0)
        
    def Fish_Feeder_LTURN(deg):

        full_circle = 510.0
        degree = full_circle/360*deg
        GPIO_SETUP(0,0,0,0)

        while degree > 0.0:
            GPIO_SETUP(1,0,0,1)
            GPIO_SETUP(0,0,0,1)
            GPIO_SETUP(0,0,1,1)
            GPIO_SETUP(0,0,1,0)
            GPIO_SETUP(0,1,1,0)
            GPIO_SETUP(0,1,0,0)
            GPIO_SETUP(1,1,0,0)
            GPIO_SETUP(1,0,0,0)
            degree -= 1
        GPIO_SETUP(0,0,0,0)
    """    
    while True:
        print("---------------------------------------------------")
        print("YEM ATILIYOR...")
        print("---------------------------------------------------")
        Fish_Feeder_LTURN(90)
        time.sleep(0.1)
        print("YEM ATILDI...")
        print("---------------------------------------------------")
        Fish_Feeder_LTURN(0)
        time.sleep(0.1)      
        
        Fish_Feeder_RTURN(120)
        time.sleep(0.1)
        break
    
#############################################
def gir():
    b16['state']='normal'
############################################

#############################################
def otoMod():
    dakika_degeri=int(entry4.get())
    na = datetime.datetime.now()
    yeni = int(na.strftime("%M"))
    while 1:
        x = read_temp()
        an = datetime.datetime.now()
        saat = int(an.strftime("%M"))
        #print(type(an))
        #print(type(saat))
        print("--------------------------------------------")
        print("Saat: ",(an))
        print("Dakika: ",(saat))
        print("Sıcaklık: "+str(x)+" Derece")
        print("--------------------------------------------")
        time.sleep(2)       
        if(x > 30.0):
            print("Çok Sıcak.. Fan Açılıyor...")
            while True:
                GPIO.setup(25,GPIO.OUT) #Relay IN4 for Ligth
                
                
                print("--------------------------------------------")
                print("FAN AÇILDI")
                
                GPIO.output(25,GPIO.LOW)
                time.sleep(60)
                GPIO.output(25,GPIO.HIGH)
                print("FAN KAPANDI")
                print("--------------------------------------------")
                break
            break
        
        elif(saat == yeni + dakika_degeri):
            while True:
                print("---------------------------------------------------")
                print("YEM ATILIYOR...")
                print("---------------------------------------------------")
                Fish_Feeder_LTURN(90)
                time.sleep(0.1)
                print("YEM ATILDI...")
                print("---------------------------------------------------")
                Fish_Feeder_LTURN(0)
                time.sleep(0.1)      
                
                Fish_Feeder_RTURN(120)
                time.sleep(0.1)
                break
            messagebox.showinfo("Otomod","OTOMOD KAPATILDI")
            entry4['state']='normal'
            entry4.delete(0,tk.END)
            entry4['state']='disabled'
            b16['state']='disabled'
            break
    
#############################################
# RGB LED

#Kırmızı

def kirmiziAc():
    #pi.set_PWM_dutycycle(27, 0) # Red kanalı 16
    #pi.set_PWM_dutycycle(22, 0)
    pi.set_PWM_dutycycle(17, 255)
    """
    while True:
        print("Red RGB is on")
        kirmiziAc()
        break
    """
#Yesil
def yesilAc():
    pi.set_PWM_dutycycle(27, 255) 
    #pi.set_PWM_dutycycle(22, 0) # Green Kanalı 20
    #pi.set_PWM_dutycycle(17, 0)
    """
    while True:
        print("Green RGB is on")
        yesilAc()
        break
    """
#Mavi
def maviAc():
    #pi.set_PWM_dutycycle(27, 0)
    pi.set_PWM_dutycycle(22, 255)
    #pi.set_PWM_dutycycle(17, 0) # Blue Kanalı 21
    """
    while True:
        print("Blue RGB is on")
        maviAc()
        break
    """
#Kırmızıkapat

def kirmiziKapat():
    #pi.set_PWM_dutycycle(27, 0)
    #pi.set_PWM_dutycycle(22, 0)
    pi.set_PWM_dutycycle(17, 0)
    """
    while True:
        print("Red RGB is off")
        kirmiziKapat()
        break
    """
#Yesilkapat

def yesilKapat():
    pi.set_PWM_dutycycle(27, 0)
    #pi.set_PWM_dutycycle(22, 0)
    #pi.set_PWM_dutycycle(17, 0)
    """
    while True:
        print("Green RGB is off")
        yesilKapat()
        break
    """
#Mavi

def maviKapat():
    #pi.set_PWM_dutycycle(27, 0)
    pi.set_PWM_dutycycle(22, 0)
    #pi.set_PWM_dutycycle(17, 0)
    """
    while True:
        print("Blue RGB is off")
        maviKapat()
        break
    """

#############################################

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        #time.def yem_at():sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        #temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c


#############################################
def sistemi_kapat():
    cevap=messagebox.askyesno("Çıkış","Programı Kapatmak İstediğinizden\n Eminmisiniz ?")
    if cevap==1:
        exit()
    else:
        pass

#############################################
def suSeviyesi():
    entry['state']='normal'
    entry.delete(0,tk.END)
    entry['state']='disabled'
    b9['state']='normal'
    while True:
        global pulse_duration
        global pulse_start
        global pulse_end
        GPIO.output(TRIG, False)
        #print "Waiting For Sensor To Settle"
        time.sleep(0.5)

        
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)


        
        while GPIO.input(ECHO)==0:
          pulse_start = time.time()

        while GPIO.input(ECHO)==1:
          pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150

        distance = round(distance, 2)
          

        print ("Su Seviyesi: ",distance,"cm")
        #return distance
        entry['state']='normal'
        entry.insert(0,distance)
        entry.insert(tk.END," cm")
        entry['state']='disabled'
        break
    #-------------------------------------------------------
    
#############################################
#############################################
def sicaklikDurumu():
    entry2['state']='normal'
    entry2.delete(0,tk.END)
    entry2['state']='disabled'
    b9['state']='normal'
    while True:
        #print(type(read_temp()))
        print(str(read_temp())+" Derece")
        x = read_temp()
        time.sleep(1)
        entry2['state']='normal'
        entry2.insert(0,x)
        entry2.insert(tk.END," Derece")
        entry2['state']='disabled'
        break
    #-------------------------------------------------------
    
#############################################
    
    
    
    
def isikKapat():
    while True:
        #GPIO.setup(14,GPIO.OUT) #Relay IN4 for Ligth
        
        
        print("--------------------------------------------")
        
        print("IŞIK KAPANDI")
        GPIO.output(14,GPIO.LOW)
        time.sleep(1)
       
        print("--------------------------------------------")
        break

def isikAc():
    while True:
        #GPIO.setup(14,GPIO.OUT) #Relay IN4 for Ligth
        
        
        print("--------------------------------------------")
        print("IŞIK AÇILDI")
        
        GPIO.output(14,GPIO.HIGH)
        time.sleep(1)
       
        print("--------------------------------------------")
        break
    
    
#############################################

def faniAc():
    while True:
        GPIO.setup(25,GPIO.OUT) #Relay IN4 for Ligth
        
        
        print("--------------------------------------------")
        print("FAN AÇILDI")
        
        GPIO.output(25,GPIO.LOW)
        time.sleep(1)
       
        print("--------------------------------------------")
        break
    
    
#############################################
#############################################

def faniKapat():
    while True:
        GPIO.setup(25,GPIO.OUT) #Relay IN4 for Ligth
        
        
        print("--------------------------------------------")
        print("FAN KAPATILDI")
        
        GPIO.output(25,GPIO.HIGH)
        time.sleep(1)
       
        print("--------------------------------------------")
        break
    
    
#############################################
#############################################

def pompa1Ac():
    
    temizle_cevap=messagebox.askyesno("Su Boşalt","Su Boşaltmak\nİstediğinizden Eminmisiniz ?")
    if temizle_cevap==1:
        while True:
            #GPIO.setup(7,GPIO.OUT) #Relay IN4 for Ligth
            
            
            print("--------------------------------------------")
            print("POMPA 1 AÇILDI")
            
            GPIO.output(7,GPIO.LOW)
            time.sleep(1)
           
            print("--------------------------------------------")
            messagebox.showinfo("Su Boşalt","SU BOŞALTILIYOR.")
            break
    else:
        pass
    
    
#############################################
#############################################

def pompa1Kapat():
    
    temizle_cevap=messagebox.askyesno("Su Boşalt","Pompa 1'yi Kapatmak\nİstediğinizden Eminmisiniz ?")
    if temizle_cevap==1:
        while True:
            #GPIO.setup(7,GPIO.OUT) #Relay IN4 for Ligth
            
            
            print("--------------------------------------------")
            print("POMPA 1 KAPATILDI")
            
            GPIO.output(7,GPIO.HIGH)
            time.sleep(1)
           
            print("--------------------------------------------")
            messagebox.showinfo("Su Boşalt","POMPA KAPATILDI.")
            break
    else:
        pass
    
    
#############################################
#############################################

def pompa2Ac():
    
    temizle_cevap=messagebox.askyesno("Su Doldur","Su Doldurmak\nİstediğinizden Eminmisiniz ?")
    if temizle_cevap==1:
        while True:
            GPIO.setup(15,GPIO.OUT) #Relay IN4 for Ligth
            
            
            print("--------------------------------------------")
            print("POMPA 2 AÇILDI")
            
            GPIO.output(15,GPIO.LOW)
            time.sleep(1)
           
            print("--------------------------------------------")
            messagebox.showinfo("Su Doldur","SU DOLDURULUYOR.")
            break
            
    else:
        pass
    
    
#############################################
#############################################

def pompa2Kapat():
    
    temizle_cevap=messagebox.askyesno("Su Doldur","Pompa 2'yi Kapatmak\nİstediğinizden Eminmisiniz ?")
    if temizle_cevap==1:
        while True:
            GPIO.setup(15,GPIO.OUT) #Relay IN4 for Ligth
            
            
            print("--------------------------------------------")
            print("POMPA 2 KAPATILDI")
            
            GPIO.output(15,GPIO.HIGH)
            time.sleep(1)
           
            print("--------------------------------------------")
            messagebox.showinfo("Su Boşalt","POMPA 2 KAPATILDI.")
            break
    else:
        pass
    
#############################################

#############################################

def suSizintiDurumu():
    entry3['state']='normal'
    entry3.delete(0,tk.END)
    entry3['state']='disabled'
    b9['state']='normal'
    while True:
        state = GPIO.input(26)
        if state == GPIO.HIGH:
            print("SIZINTI VAR")
            entry3['state']='normal'
            entry3.insert(0,"Sızıntı Var")
            entry3['state']='disabled'
            messagebox.showinfo("Sizinti","SIZINTI VAR")
            break
        else:
            print("SIZINTI YOK")
            entry3['state']='normal'
            entry3.insert(0,"Sızıntı Yok")
            entry3['state']='disabled'
            messagebox.showinfo("Sizinti","SIZINTI YOK")
            break
            
        time.sleep(1)
        print("--------------------------------")
    
    
############################################# 



def uyari():
    led_kirmizi.value =False
    buzzer.duty_cycle=0


############################################# 
def ent_temizle():
    temizle_cevap=messagebox.askyesno("Temizleme","Bütün Verileri Temizlemek İstediğinizden\n Eminmisiniz ?")
    if temizle_cevap==1:
        entry['state']='normal'
        entry.delete(0,tk.END)
        entry['state']='disabled'
    
        entry2['state']='normal'
        entry2.delete(0,tk.END)
        entry2['state']='disabled'
        
        entry3['state']='normal'
        entry3.delete(0,tk.END)
        entry3['state']='disabled'
        b9['state']='disabled'
        
        """
        entry4['state']='normal'
        entry4.delete(0,tk.END)
        entry4['state']='disabled'
        b16['state']='disabled'
        """
        
        #cv2.destroyAllWindows()
    else:
        pass
############################################# 
def veri_kaydet():
    
    y1=str(entry.get())
    y2=str(entry2.get())
    y3=str(entry3.get())
    
    an = datetime.datetime.now()
    st_an=datetime.datetime.strftime(an,'Tarih: %d.%m.%Y Saat %H.%M.%S')
    
    dosya_2 = open("akvaryum_bilgileri.txt", "a", encoding="utf-8")
    
    dosya_2.write("********************************************")
    dosya_2.write("\n")
    dosya_2.write(st_an)
    dosya_2.write("\n")
    dosya_2.write("Su Seviyesi: "+y1)
    dosya_2.write("\n")
    dosya_2.write("Sıcaklık Durumu: "+y2)
    dosya_2.write("\n")
    dosya_2.write("Sızıntı Durumu: "+y3)
    dosya_2.write("\n")
    dosya_2.write("********************************************")
    dosya_2.write("\n")
    
    
    dosya_2.close()
    messagebox.showinfo("Kayıt","BİLGİLER KAYIT EDİLDİ")
    
    
#############################################    


pencere.title("Akvaryum Kontrol Sistemi -Anasayfa")
pencere.geometry("700x550+0+0")

baslik=tk.Label(text="AKVARYUM KONTROL SİSTEMİ",font="Verdana 22 bold",bg="white")
baslik.place(x=80,y=10)

an = datetime.datetime.now()
saat_yazi=tk.Label(text="Saat : "+(an.strftime("%H:%M:%S")),fg="white",font="Verdana 15 bold",bg="grey")
saat_yazi.place(x=10,y=60)

girdi_yazi=tk.Label(text="Lütfen Dakika Giriniz!",fg="white",font="Verdana 15 bold",bg="red")
girdi_yazi.place(x=200,y=60)

#kam_yazi2=tk.Label(text="ÇIKIŞ için Klavyeden 'E' Tuşuna Basınız",font="Verdana 10 bold",bg="white")
#kam_yazi2.place(x=165,y=130)

b2=tk.Button(text="Su Seviyesi",bg="blue",fg="#FFFFFF",font="bold",command = suSeviyesi)
b2.place(x=10,y=190)

b3=tk.Button(text="IŞIĞI KAPAT" ,bg="red",fg="#FFFFFF",font="bold",command=isikKapat)
b3.place(x=10,y=300)

b5=tk.Button(text="IŞIĞI AÇ", bg="green",font="bold",fg="#FFFFFF",command=isikAc)
b5.place(x=10,y=255)

b7=tk.Button(text="Programı Kapat", command =sistemi_kapat)
b7.place(x=550,y=500)

b8=tk.Button(text="Temizle",command =ent_temizle)
b8.place(x=330,y=500)

b9=tk.Button(text="Sisteme Kaydet", state='disabled',command =veri_kaydet)
b9.place(x=415,y=500)

b10=tk.Button(text="Sıcaklık Durumu", bg="purple",font="bold",fg="#FFFFFF",command=sicaklikDurumu)
b10.place(x=10,y=150)

b11=tk.Button(text="FANI AÇ", bg="green",font="bold",fg="#FFFFFF",command=faniAc)
b11.place(x=150,y=255)

b12=tk.Button(text="FANI KAPAT", bg="red",font="bold",fg="#FFFFFF",command=faniKapat)
b12.place(x=150,y=300)

b11=tk.Button(text="SU BOŞALT", bg="green",font="bold",fg="#FFFFFF",command=pompa1Ac)
b11.place(x=300,y=255)

b12=tk.Button(text="1.POMPAYI KAPAT", bg="red",font="bold",fg="#FFFFFF",command=pompa1Kapat)
b12.place(x=300,y=300)

b13=tk.Button(text="SU DOLDUR", bg="green",font="bold",fg="#FFFFFF",command=pompa2Ac)
b13.place(x=490,y=255)

b14=tk.Button(text="2.POMPAYI KAPAT", bg="red",font="bold",fg="#FFFFFF",command=pompa2Kapat)
b14.place(x=490,y=300)

b15=tk.Button(text="Su Sızıntı Durumu",bg="blue",fg="#FFFFFF",font="bold",command = suSizintiDurumu)
b15.place(x=130,y=190)

b16=tk.Button(text="OTOMATİK MOD", state='disabled',bg="black",fg="#FFFFFF",font="bold",command = otoMod)
b16.place(x=10,y=110)

b17=tk.Button(text="RED",bg="red",fg="#FFFFFF",font="bold", command = kirmiziAc)
b17.place(x=300,y=150)

b18=tk.Button(text="GREEN",bg="green",fg="#FFFFFF",font="bold", command = yesilAc)
b18.place(x=360,y=150)

b19=tk.Button(text="BLUE",bg="blue",fg="#FFFFFF",font="bold", command = maviAc)
b19.place(x=440,y=150)

b20=tk.Button(text="RED",bg="black",fg="#FF0000",font="bold", command = kirmiziKapat)
b20.place(x=300,y=190)

b21=tk.Button(text="GREEN",bg="black",fg="#008000",font="bold", command = yesilKapat)
b21.place(x=360,y=190)

b22=tk.Button(text="BLUE",bg="black",fg="#0000FF",font="bold", command = maviKapat) 
b22.place(x=440,y=190)

b23=tk.Button(text="GİR",bg="white",fg="#0000FF",font="bold", command = gir)
b23.place(x=300,y=110)

b24=tk.Button(text="YEM AT",bg="orange",fg="white",font="bold", command = yem_at)
b24.place(x=520,y=190)

b25 = tk.Button(text = "Kameraya Bağlan",bg="#D42866",fg="white",command = openweb)
b25.place(x=520,y=110)

b26 = tk.Button(text = "Ekran görüntüsü al",bg="#8128D4",fg="white",command = ekran_goruntusu)
b26.place(x=520,y=150)

su_seviyesi = tk.Label(text=("SU SEVİYESİ"),bg="white" ,font="Verdana 15 bold")
su_seviyesi.place(x=10, y=370)

sicaklik_durumu  = tk.Label(text=('SICAKLIK DURUMU'), bg="white",font="Verdana 15 bold")
sicaklik_durumu.place(x=10, y=420)

sizinti_durumu  = tk.Label(text=('SIZINTI DURUMU'), bg="white",font="Verdana 15 bold")
sizinti_durumu.place(x=10, y=460)

pencere.mainloop()


