import cv2
import requests
import numpy as np
import imutils
from pyzbar import pyzbar


def read_Barcode(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y, w, h = barcode.rect
        barcode_info = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 1)

        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, barcode_info, (x + 8, y - 8),
                    font, 1.0, (255, 255, 255), 1)
        with open("barcode_result.txt", mode='w') as file:
            file.write("Recognized Barcode:" + barcode_info)
    return frame


def main():
    # Capturing the video from Ip hosted camera.
    IP_Url = "<Enter your Ip address where video is hosted>/shot.jpg"

    while True:
        img_resp = requests.get(IP_Url)
        img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
        img = cv2.imdecode(img_arr, -1)
        img = imutils.resize(img, width=400, height=800) # Adjust dimensions according to your video orientation
        frame = img
        frame = read_Barcode(frame)
        cv2.imshow('Barcode/QR code reader', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
