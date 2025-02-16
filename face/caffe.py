import cv2
import numpy as np

# Load model Caffe untuk deteksi wajah
model_file = "res10_300x300_ssd_iter_140000.caffemodel"
config_file = "deploy.prototxt"
net = cv2.dnn.readNetFromCaffe(config_file, model_file)

# Buka video dari CCTV atau kamera
video = cv2.VideoCapture(0)  # Ganti dengan URL CCTV atau file video
if not video.isOpened():
    print("Error: Gagal membuka video.")
    exit()

while True:
    ret, frame = video.read()
    if not ret:
        print("Error: Gagal membaca frame.")
        break

    height, width = frame.shape[:2]

    # Preprocessing frame untuk model
    blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), (104.0, 177.0, 123.0))
    net.setInput(blob)
    detections = net.forward()

    # Proses deteksi
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:  # Ambil deteksi dengan confidence > 50%
            box = detections[0, 0, i, 3:7] * np.array([width, height, width, height])
            (x, y, x2, y2) = box.astype("int")
            cv2.rectangle(frame, (x, y), (x2, y2), (0, 255, 0), 2)

    # Tampilkan jumlah wajah yang terdeteksi
    cv2.putText(frame, f"Jumlah Wajah: {detections.shape[2]}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Tampilkan frame
    cv2.imshow("Deteksi Wajah", frame)

    # Tekan 'q' untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()