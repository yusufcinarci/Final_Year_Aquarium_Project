# Final Year Aquarium Project

Raspberry Pi 3b, bu akvaryum izleme sistemindeki sensörleri ve aktüatörleri izlemek ve kontrol etmek için ana kontrolör olarak kullanılmıştır. Pi'nin kontrol etmesi gereken yaklaşık dört sensör ve altı aktüatör bulunmaktadır. 

## Akvaryum Monitör Sisteminin Genel Blok Diyagramı

<p align="center">
<img src="https://github.com/yusufcinarci/Final_Year_Aquarium_Project/assets/77057546/549f1286-f7bf-460a-9abb-732cdabcf232" width="80%">
</p>

## Sistemin Çalışma Prensibi ve Akış Şeması

Bu akvaryum izleme sistemi, biri manuel mod ve diğeri otomatik mod olmak üzere iki moddan oluşur. Manuel mod, kullanıcı müdahalelerine ihtiyaç duyar. Örneğin, balığı beslemek için kullanıcının akvaryum kontrol sistem uygulamasını kullanarak Pi'ye manuel olarak komut göndermesi gerekir. Otomatik modda ise Pi, sensöre dayalı akıllı kararlar verebilir. Örneğin, saat 21:00 ise balığı besleyin, çok kirliyse suyu değiştirin, bulanıklık sensör değerini alın vb. Yani yukarıda bahsedilen her şeyi yapmak için bir algoritmaya ihtiyaç vardır. Aşağıda bu sistemde kullanılan ana algoritma akış şeması gösterilmektedir.
<p align="center">
<img src="https://github.com/yusufcinarci/Final_Year_Aquarium_Project/assets/77057546/1a971d24-5c15-4604-927f-1892aad778a8" width="50%">
</p>

## Akvaryum Kontrol Sistemi Kullanıcı Arayüzü (GUI)

Aşağıda verilen görselde kullanıcı arayüzü şeması gösterilmiştir. Python Tkinter arayüz tasarlama kütüphanesi kullanılarak hazırlanan bu arayüz oldukça sade ve anlaşılır bir şekilde tasarlanmıştır. Kullanıcının sistem üzerinde bulunan tüm sensörleri, ışıkları, aktüatörleri ve diğer modları uzaktan kontrol edebileceği bir arayüz tasarlanmıştır.
<p align="center">
<img src="https://github.com/yusufcinarci/Final_Year_Aquarium_Project/assets/77057546/93f8d4e1-8c93-44fc-bb77-71f3e6bca690" width="80%">
</p>

Kullanıcının bu akvaryum izleme sistemini kontrol etmesinin ve izlemesinin iki yolu vardır; biri Pi'de manuel mod diğeri ise yine Pi üzerinde çalışacak otomatik moddur. 
Verilen arayüz kısaca tanımlanacak olursa; Otomatik mod butonu, kullanıcıdan dakika bilgisi alacak olan girdi kutusu, RGB Led kontrol butonları, yemleme butonu, kameraya bağlanma ve ekran görüntüsü alma butonu, sıcaklık durumu, su seviyesi, su sızıntı durumu gibi sensör butonları, beyaz led, soğutucu fan ve su pompa butonları ile sistemdeki bilgileri kaydetme, temizleme ve sistemi kapatma butonu yer almaktadır. Kullanıcı arayüzü ile sistemin genel blok şeması aşağıda verilmiştir.

<p align="center">
<img src="https://github.com/yusufcinarci/Final_Year_Aquarium_Project/assets/77057546/cb76b07c-6ca6-473e-991b-5cbbc265ec96" width="80%">
</p>

## Donanım ve Yazılım Bileşenleri

Akvaryum Kontrol Sisteminin oluşturulmasında kullanılan donanım bileşenlerinin ve yazılımların genel görünümünü göstermektedir.

Donanım Bileşenleri  | Yazılım Bileşenleri
------------- | -------------
Raspberry Pi 3b  | Python 
MCP3008 Dönüştürücü | Python Tkinter GUI
HC-SR04 Ultrasonik Mesafe Sensörü | UV4L Streaming Server 
Bulanıklık Sensörü | -----------
DS18B20 Su Sıcaklık Sensörü | -----------
28BYJ48 Step Motor ve ULN2003 Sürücü Kartı | -----------
SRD-05VDC-SL-C 4 Kanal 5V Röle | -----------
DS3231 Clock Modülü | -----------
Beyaz Şerit Led  | -----------
3528 RGB Led | -----------
3.5V~12V DC Fırçasız Su Pompası | -----------
2xSoğutucu Fan | -----------
Logitech webcam | -----------

## Sistemin Son Hali

<p align="center">
<img src="https://github.com/yusufcinarci/Final_Year_Aquarium_Project/assets/77057546/6187a952-d151-443f-a5e9-06b9a2021dc8" alt="alt text" width="200" height="400">
<img src="https://github.com/yusufcinarci/Final_Year_Aquarium_Project/assets/77057546/52fcd612-2734-400c-9698-358766fea605" alt="alt text" width="200" height="400">
<img src="https://github.com/yusufcinarci/Final_Year_Aquarium_Project/assets/77057546/2f20fa02-2a32-4f3b-a4af-637dc57e88be" alt="alt text" width="200" height="400">
<img src="https://github.com/yusufcinarci/Final_Year_Aquarium_Project/assets/77057546/f80bd00f-b866-4a39-9950-1108c2c0c59a" alt="alt text" width="200" height="400">
</p>









### Video

[<img src="https://r.resimlink.com/wJksN.jpg" width="50%" >](https://drive.google.com/file/d/1Of7dxlSQWjCBufpUw2A0cSVWcjmrgNWb/view?usp=sharing)

