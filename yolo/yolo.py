import cv2
import numpy as np

# Pastikan path file YOLO benar
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
layer_names = net.getLayerNames()

# Perbaikan untuk mengakses output layers
output_layers_indices = net.getUnconnectedOutLayers()
output_layers = [layer_names[i - 1] for i in output_layers_indices]

# Load class labels
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Open video
# video = cv2.VideoCapture("highway.mp4")  # Ganti dengan sumber video Anda
video = cv2.VideoCapture(0)  # Gunakan kamera laptop (indeks 0)
if not video.isOpened():
    print("Error: Gagal membuka video.")
    exit()

# Define line for counting
line_y = 300  # Posisi garis virtual
count = 0

while True:
    ret, frame = video.read()
    if not ret:
        print("Error: Gagal membaca frame dari video.")
        break

    height, width, channels = frame.shape

    # Deteksi objek menggunakan YOLO
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    # Parsing hasil deteksi
    class_ids = []
    boxes = []
    confidences = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5 and classes[class_id] == "car":  # Hanya deteksi mobil
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Koordinat kotak pembatas
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # Non-max suppression untuk menghapus duplikat
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    # Gambar kotak pembatas dan hitung mobil yang melewati garis
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # Cek apakah mobil melewati garis
            if y < line_y < y + h:
                count += 1

    # Gambar garis virtual
    cv2.line(frame, (0, line_y), (width, line_y), (0, 0, 255), 2)
    cv2.putText(frame, f"Count: {count}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Tampilkan frame
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()