import pywhatkit 
import time
import os
from datetime import datetime
import pyautogui as pg #Importe pyautogui para suprir algumas falhas da biblioteca pywhatkit


agora = datetime.now()
hora = agora.hour
minuto = agora.minute

send = "mensagem"
num = "" #Digite o númedo com o código de país e ddd


def send_wpp() : 
    try: 
      pywhatkit.sendwhatmsg(num,  
                            send,  
                         hora, minuto) 
      print("Successfully Sent!") 
      time.sleep(1)
      pg.press('enter')
      time.sleep(1)
      pg.hotkey('alt', 'f4')
    except:  
      print("An Unexpected Error!")
      return send_wpp()

send_wpp()





