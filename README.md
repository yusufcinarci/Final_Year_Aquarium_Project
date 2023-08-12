# Final Year Aquarium Project

Bu proje esas olarak Raspberry Pi adlı tek çip kullanan bilgisayar ile bir Akvaryum İzleme Sistemi oluşturmaya yöneliktir. Bu projenin temel amacı, kapalı akvaryumlarının bakımını yapmakta güçlük çekenlere, özellikle de sık sık dışarıda kalanlara bu nedenle akvaryumlarını sürekli izleyemeyenlere yardımcı olmaktır. Bu sistem sayesinde kullanıcılar, akvaryumlarını sade ve basit bir arayüzü üzerinden kontrol edebilir ve izleyebilirler. Bu sistemin ana rolü, kullanıcıların balıkları zamanında besleme, su sıcaklığını, su seviyesini kontrol etme gibi görevleri içeren bir dizi süreci kontrol etmektir. Suyu pompalar aracılığı ile uzaktan doldurup boşaltma gibi ana işlevler bu sistem sayesinde oldukça kolay hale getirilmiştir. Akvaryumda su sızıntısı veya akvaryumun su seviyesinin normal seviyelerin altına düşmesi gibi acil durumlar olduğunda, kullanıcının arayüz üzerinde uyarı alması sağlanır. Akvaryumun durumunu sürekli olarak kontrol etmek için, Raspberry Pi 3, sensörlerden veri toplamak ve ardından verileri kaydetmek, sensörleri ve aktüatörleri kontrol etmek gibi işlevleri yerine getiren ana karttır. Kullanıcı daha sonra akvaryumlarının durumunu kontrol etmek için Raspberry Pi tarafından barındırılan özel olarak tasarlanmış arayüzüne giriş yapacaktır. Bunun yanında su sıcaklık sensörü, sistemin en iyi şekilde çalıştığından emin olmak için su sızıntı sensörü ve su seviye sensörü de gereklidir. Bunun dışında su pompası, su filtresi ve balıkları beslemek için motorlar da gereklidir. Bu proje ile akvaryum otomasyonu gerçekleştirilmiş ve belli başlı sensörler yardımıyla uzaktan kolay ve sade bir arayüz yardımıyla akvaryum kontrolü gerçekleştirilebileceği gösterilmiştir.

## Akvaryum Monitör Sisteminin Genel Blok Diyagramı

<p align="center">
<img src="https://github.com/yusufcinarci/Final_Year_Aquarium_Project/assets/77057546/d0217d2f-e471-4c7f-bf3d-568c7086f9a9" width="80%">
</p>

## Sistemin Çalışma Prensibi ve Akış Şeması

Bu akvaryum izleme sistemi, biri manuel mod ve diğeri otomatik mod olmak üzere iki moddan oluşur. Manuel mod, kullanıcı müdahalelerine ihtiyaç duyar. Örneğin, balığı beslemek için kullanıcının akvaryum kontrol sistem uygulamasını kullanarak Pi'ye manuel olarak komut göndermesi gerekir. Otomatik modda ise Pi, sensöre dayalı akıllı kararlar verebilir. Örneğin, saat 21:00 ise balığı besleyin, çok kirliyse suyu değiştirin, bulanıklık sensör değerini alın vb. Yani yukarıda bahsedilen her şeyi yapmak için bir algoritmaya ihtiyaç vardır. Aşağıda bu sistemde kullanılan ana algoritma akış şeması gösterilmektedir.
<p align="center">
<img src="https://github.com/yusufcinarci/Final_Year_Aquarium_Project/assets/77057546/0d3aac95-16d2-4f43-baaf-8ce0eda14306" width="50%">
</p>

## Akvaryum Kontrol Sistemi Kullanıcı Arayüzü (GUI)

Aşağıda verilen görselde kullanıcı arayüzü şeması gösterilmiştir. Python Tkinter arayüz tasarlama kütüphanesi kullanılarak hazırlanan bu arayüz oldukça sade ve anlaşılır bir şekilde tasarlanmıştır. Kullanıcının sistem üzerinde bulunan tüm sensörleri, ışıkları, aktüatörleri ve diğer modları uzaktan kontrol edebileceği bir arayüz tasarlanmıştır.
<p align="center">
<img src="https://github.com/yusufcinarci/Final_Year_Aquarium_Project/assets/77057546/80e96767-c76a-4707-8163-a80448d05450" width="80%">
</p>

Kullanıcının bu akvaryum izleme sistemini kontrol etmesinin ve izlemesinin iki yolu vardır; biri Pi'de manuel mod diğeri ise yine Pi üzerinde çalışacak otomatik moddur. 
Verilen arayüz kısaca tanımlanacak olursa; Otomatik mod butonu, kullanıcıdan dakika bilgisi alacak olan girdi kutusu, RGB Led kontrol butonları, yemleme butonu, kameraya bağlanma ve ekran görüntüsü alma butonu, sıcaklık durumu, su seviyesi, su sızıntı durumu gibi sensör butonları, beyaz led, soğutucu fan ve su pompa butonları ile sistemdeki bilgileri kaydetme, temizleme ve sistemi kapatma butonu yer almaktadır. Kullanıcı arayüzü ile sistemin genel blok şeması aşağıda verilmiştir.

<p align="center">
<img src="https://github.com/yusufcinarci/Final_Year_Aquarium_Project/assets/77057546/efe17f7b-627c-4df0-a6e1-c1298d658eac" width="80%">
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
<img src="https://github.com/yusufcinarci/Final_Year_Aquarium_Project/assets/77057546/6924fb73-14bf-46e8-8227-34a5a77f33ac" alt="alt text" width="200" height="400">
<img src="https://github.com/yusufcinarci/Final_Year_Aquarium_Project/assets/77057546/d4a81938-96e2-4599-bcf6-62b0de371588" alt="alt text" width="200" height="400">
<img src="https://github.com/yusufcinarci/Final_Year_Aquarium_Project/assets/77057546/dd0c168a-558e-4b5b-b578-5b2dc2d66619" alt="alt text" width="200" height="400">
</p>

## SONUÇLAR

İnsanların günümüz dünyasında vakitlerini oldukça verimli kullanması önemlidir. Gün içerisinde birçok yoğun telaşın ve koşuşturmacanın arasında evlerinde hobi olarak besledikleri balıklarının bakımlarını kolaylaştırma amacıyla bu sistem geliştirilmiştir.Sistemin çalışma mantığı, ekran görüntüleri, test görüntüleri ve kullanıcı kontrol durumları yukarıda detaylı olarak verilmiştir. Bu sistemde birçok geliştirme yapılabilir ve sistem hem donanım hem yazılım olarak üst düzey bir görünüme kavuşabilir. 

Bu çalışma ile kullanıcıların akvaryumlarındaki sensörleri ve aktüatörleri uzaktan sade ve basit bir arayüzü aracılığı ile kontrol edebileceği gösterilmiştir. Kullanılan ana kart Raspberry pi model 3B bu çalışmada önemli bir rol oynamış ve sistemin sorunsuz bir şekilde çalışmasını sağlamıştır.








### Video

[<img src="https://r.resimlink.com/wJksN.jpg" width="50%" >](https://drive.google.com/file/d/1Of7dxlSQWjCBufpUw2A0cSVWcjmrgNWb/view?usp=sharing)

