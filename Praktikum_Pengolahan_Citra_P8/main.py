import cv2
import matplotlib.pyplot as plt

# ======================
# 1. BACA GAMBAR
# ======================
img = cv2.imread('gambar.jpg')

# Cek kalau gambar gagal dibaca
if img is None:
    print("Gambar tidak ditemukan!")
    exit()

# ======================
# 2. KONVERSI
# ======================
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# ======================
# 3. THRESHOLD BIASA
# ======================
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# ======================
# 4. ADAPTIVE THRESHOLD
# ======================
adaptive = cv2.adaptiveThreshold(
    gray,
    255,
    cv2.ADAPTIVE_THRESH_MEAN_C,
    cv2.THRESH_BINARY,
    11,
    2
)

# ======================
# 5. OTSU THRESHOLD
# ======================
ret2, otsu = cv2.threshold(
    gray,
    0,
    255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

# ======================
# 6. EDGE DETECTION (CANNY)
# ======================
edges = cv2.Canny(gray, 100, 200)

# ======================
# 7. TAMPILKAN SEMUA
# ======================
plt.figure(figsize=(15,10))

plt.subplot(2,3,1)
plt.imshow(img_rgb)
plt.title('Gambar Asli')
plt.axis('off')

plt.subplot(2,3,2)
plt.imshow(gray, cmap='gray')
plt.title('Grayscale')
plt.axis('off')

plt.subplot(2,3,3)
plt.imshow(thresh, cmap='gray')
plt.title('Threshold Biasa')
plt.axis('off')

plt.subplot(2,3,4)
plt.imshow(adaptive, cmap='gray')
plt.title('Adaptive Threshold')
plt.axis('off')

plt.subplot(2,3,5)
plt.imshow(otsu, cmap='gray')
plt.title('Otsu Threshold')
plt.axis('off')

plt.subplot(2,3,6)
plt.imshow(edges, cmap='gray')
plt.title('Edge Detection (Canny)')
plt.axis('off')

plt.tight_layout()
plt.show()