import pyautogui, sys, time
import configparser
config = configparser.ConfigParser()
config.read('ayar.txt', encoding='utf-8')
x1 = int(config.get('ilk_tik', 'x1'));
y1 = int(config.get('ilk_tik', 'y1'));
x2 = int(config.get('ikinci_tik', 'x2'));
y2 = int(config.get('ikinci_tik', 'y2'));
timer = float(config.get('ayar', 'timer'));
count = int(config.get('ayar', 'count'));
 
print("""
      Bu program ayar.txt dosyasında belirttiğiniz şekilde otomatik olarak tıklama işlemi yapacaktır.
      Aklınızda bulundurmanız gereken bilgiler;
      1) Inemps bildirim zilinin X ve Y Koordinatları,
      2) İlk bildirimin X ve Y Koordinatları,
      3) Tıklamalar arasında ne kadar milisaniye bekleyeceği,
      Unutmayın, bildirim sayısı çok fazla ise bekleme süresi uzun olsun yoksa site yetişemeyecektir tıklama hızına.
      Ayar dosyasında yaptığınız her değişiklik sonrası bu programı tekrar kapatıp açınız.
      
      Programı başlatmak ve kapatmak için Enter (Return) tuşuna basınız.
      
      """)
try:
    while (count > 0):
        pyautogui.click(x=x1, y=y1)
        time.sleep(timer)
        pyautogui.click(x=x2, y=y2)
        time.sleep(timer)
        count -=1;
except KeyboardInterrupt:
    print("Program durduruldu.") 