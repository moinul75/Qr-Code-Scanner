import cv2
from pyzbar.pyzbar import decode,ZBarSymbol

cap = cv2.VideoCapture(0)
recieved_data = None

while True:
    success,frame = cap.read()
    
    decode_data = decode(frame,symbols=[ZBarSymbol.QRCODE]) 
    
    try:
        data = decode_data[0][0]
        if data !=recieved_data:
            recieved_data = data
            
        print(recieved_data)
        
    except:
        pass
    
    cv2.imshow('QR Code Scanner App',frame)
    key = cv2.waitKey(1)
    
    if key == ord('d'):
        break
    