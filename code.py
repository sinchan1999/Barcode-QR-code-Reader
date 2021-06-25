import cv2
from pyzbar import pyzbar

# Function to read and write the info.
def read_Barcode(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y, w, h = barcode.rect
        barcode_info = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 1)

        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, barcode_info, (x + 8, y - 8),
                    font, 1.0, (252, 194, 0), 1)

        # Opening & writing the Barcode/QR-code info.
        with open("barcode_result.txt", mode='w') as file:
            file.write("Recognized Barcode:" + barcode_info)
    return frame

# Capturing the video from primary camera (webcam).
def main():
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    while ret:
        ret, frame = camera.read()
        frame = read_Barcode(frame)
        cv2.imshow('Barcode/QR code reader', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    camera.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
