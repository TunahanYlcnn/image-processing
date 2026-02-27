import cv2
import numpy as np
from pyzbar.pyzbar import decode

# Kamera başlat
cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

qr_detector = cv2.QRCodeDetector()

def perspective_correction(image, points):
    rect = np.zeros((4, 2), dtype="float32")
    s = points.sum(axis=1)
    rect[0] = points[np.argmin(s)]
    rect[2] = points[np.argmax(s)]

    diff = np.diff(points, axis=1)
    rect[1] = points[np.argmin(diff)]
    rect[3] = points[np.argmax(diff)]

    (tl, tr, br, bl) = rect
    widthA = np.linalg.norm(br - bl)
    widthB = np.linalg.norm(tr - tl)
    heightA = np.linalg.norm(tr - br)
    heightB = np.linalg.norm(tl - bl)

    maxWidth = int(max(widthA, widthB))
    maxHeight = int(max(heightA, heightB))

    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype="float32")

    M = cv2.getPerspectiveTransform(rect, dst)
    warp = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
    return warp

while True:
    ret, frame = cap.read()
    if not ret:
        break

    found = False  # Bulundu mu işareti

    # ✅ 1. Tüm görüntüyü doğrudan tarayarak başla
    retval, decoded_info, points, _ = qr_detector.detectAndDecodeMulti(frame)
    if retval:
        for data, pt in zip(decoded_info, points):
            if data:
                pt = pt.astype(int)
                cv2.polylines(frame, [pt], True, (0, 255, 0), 2)
                cv2.putText(frame, data, (pt[0][0], pt[0][1] - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
                print("✅ Multi QR:", data)
                found = True
        if found:
            cv2.imshow("Gelişmiş QR Okuyucu", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            continue

    # ✅ 2. Kontur tabanlı perspektif düzeltme başlat
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.adaptiveThreshold(blurred, 255,
                                   cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY_INV, 21, 9)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    contours, _ = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.03 * cv2.arcLength(cnt, True), True)

        # 🔒 reshape hatasına karşı sadece 4 köşe ile devam et
        if len(approx) == 4 and cv2.contourArea(cnt) > 10000:
            pts = approx.reshape((4, 2))
            warped = perspective_correction(frame, pts)

            # ✅ Önce OpenCV QR çözümlemesi
            data, _, _ = qr_detector.detectAndDecode(warped)

            # ✅ Eğer başarısızsa pyzbar ile dene
            if not data:
                decoded = decode(warped)
                if decoded:
                    data = decoded[0].data.decode("utf-8")

            if data:
                print("✅ Perspektif QR:", data)
                cv2.putText(frame, data, (pts[0][0], pts[0][1] - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
                cv2.drawContours(frame, [approx], -1, (0, 255, 0), 3)
                found = True
                break

    if not found:
        cv2.putText(frame, "QR bulunamadi", (30, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    cv2.imshow("Gelişmiş QR Okuyucu", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
