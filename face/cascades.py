import cv2

# Load Haar Cascade untuk deteksi wajah
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Buka video dari CCTV atau kamera
video = cv2.VideoCapture(0)  # Ganti dengan URL CCTV atau file video
if not video.isOpened():
    print("Error: Gagal membuka video.")
    exit()

count = 0  # Hitungan wajah

while True:
    ret, frame = video.read()
    if not ret:
        print("Error: Gagal membaca frame.")
        break

    # Konversi ke grayscale (Haar Cascade bekerja lebih baik pada grayscale)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Deteksi wajah
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Gambar kotak di sekitar wajah dan hitung jumlahnya
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        count += 1

    # Tampilkan jumlah wajah yang terdeteksi
    cv2.putText(frame, f"Jumlah Wajah: {len(faces)}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Tampilkan frame
    cv2.imshow("Deteksi Wajah", frame)

    # Tekan 'q' untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()