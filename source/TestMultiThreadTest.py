import pytesseract
from PIL import Image
import threading
import time

pytesseract.pytesseract.tesseract_cmd = 'D:/PythonTestProjects/Blink/Tesseract-OCR/tesseract'

def SingleTest():
    image = Image.open('WinnerPreOCRStretched.png')
    text = pytesseract.image_to_string(image, lang='eng')
    print(text)


'''t1 = threading.Thread(target=SingleTest)
t2 = threading.Thread(target=SingleTest)
t3 = threading.Thread(target=SingleTest)
t4 = threading.Thread(target=SingleTest)
t5 = threading.Thread(target=SingleTest)
t6 = threading.Thread(target=SingleTest)
t7 = threading.Thread(target=SingleTest)
t8 = threading.Thread(target=SingleTest)
t9 = threading.Thread(target=SingleTest)
t10 = threading.Thread(target=SingleTest)
'''
startT = time.time()
'''
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
t9.join()
t10.join()
'''
SingleTest()
endT = time.time()
print(endT - startT)