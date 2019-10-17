import pyautogui, sys
print("""
      Bu program mouse koordinatlarını bulmanızı sağlayacaktır.
      X ve Y düzlemlerini her iki tıklama işlemi için not edip config dosyasına uygun şekilde ekleyiniz.
      Programı kapatmak için Ctrl-C tuşlarına basınız.
      
      """)
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n') 