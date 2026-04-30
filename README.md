# 📌 Praktikum Pengolahan Citra - Pertemuan 8

## 👩‍💻 Deskripsi

Program ini merupakan implementasi pengolahan citra digital menggunakan Python dengan library OpenCV dan Matplotlib. Pengolahan citra dilakukan melalui beberapa tahapan yaitu pembacaan citra, konversi warna, segmentasi citra menggunakan berbagai metode thresholding, serta deteksi tepi objek.

---

## 🎯 Tujuan

* Memahami proses dasar pengolahan citra digital
* Mengubah citra RGB menjadi grayscale
* Menerapkan metode thresholding untuk segmentasi citra
* Membandingkan hasil beberapa metode thresholding
* Mendeteksi tepi objek menggunakan metode Canny

---

## ⚙️ Tools & Library

* Python
* OpenCV (`cv2`)
* Matplotlib (`pyplot`)

---

## 🔄 Tahapan Program & Penjelasan Kode

### 1. Membaca Gambar

```python
img = cv2.imread('gambar.jpg')
```

Penjelasan:

* Fungsi `cv2.imread()` digunakan untuk membaca file gambar
* Jika gambar tidak ditemukan, program akan dihentikan

---

### 2. Konversi Warna (BGR → RGB)

```python
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
```

Penjelasan:

* OpenCV membaca gambar dalam format BGR
* Matplotlib menggunakan format RGB
* Oleh karena itu perlu dikonversi agar warna tampil dengan benar

---

### 3. Konversi ke Grayscale

```python
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
```

Penjelasan:

* Mengubah citra menjadi satu channel intensitas (abu-abu)
* Mempermudah proses pengolahan citra selanjutnya

---

### 4. Threshold Biasa

```python
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
```

Penjelasan:

* Menggunakan nilai ambang tetap (127)
* Piksel < 127 → hitam (0)
* Piksel ≥ 127 → putih (255)

---

### 5. Adaptive Threshold

```python
adaptive = cv2.adaptiveThreshold(
    gray,
    255,
    cv2.ADAPTIVE_THRESH_MEAN_C,
    cv2.THRESH_BINARY,
    11,
    2
)
```

Penjelasan:

* Threshold ditentukan berdasarkan area sekitar piksel
* Cocok untuk citra dengan pencahayaan tidak merata

---

### 6. Otsu Threshold

```python
ret2, otsu = cv2.threshold(
    gray,
    0,
    255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)
```

Penjelasan:

* Menentukan threshold secara otomatis
* Berdasarkan distribusi intensitas piksel (histogram)

---

### 7. Edge Detection (Canny)

```python
edges = cv2.Canny(gray, 100, 200)
```

Penjelasan:

* Digunakan untuk mendeteksi tepi objek
* Parameter:

  * 100 → threshold bawah
  * 200 → threshold atas

---

## 🔁 Perkembangan Program (Step by Step)

### 🔹 Tahap 1

![Menampilkan gambar asli](https://github.com/ramzi121006/uts_citra/blob/83c92140fd6f9ff9acdc1b636d79ea443b2b14bf/ss_uts_citra/ss1.png)

### 🔹 Tahap 2

Menambahkan konversi grayscale

![foto](https://github.com/ramzi121006/uts_citra/blob/900e7b2b175a78e1ee2723dee654066ed07be48f/ss_uts_citra/ss2.png)

### 🔹 Tahap 3

Menambahkan thresholding (biner)

![foto](https://github.com/ramzi121006/uts_citra/blob/90e954542589129087fa7d273111a42ea07d3fb1/ss_uts_citra/ss3.png)

### 🔹 Tahap 4

Menambahkan:

* Adaptive Threshold
* Otsu 

![foto](https://github.com/ramzi121006/uts_citra/blob/56f69e085eb371bb242d312e7ef4ce93f3db048b/ss_uts_citra/ss4.png)

### 🔹 Tahap 5 (Final)

Menambahkan:

* Edge Detection (Canny)

![foto](https://github.com/ramzi121006/uts_citra/blob/30ba9f886091637038fac4f06537de725859091f/ss_uts_citra/ss5.png)

---

## 📸 Dokumentasi Tambahan

### 📌 Source Code

![Code](hasil/hasil2.png)

---

### 📌 Struktur Folder

📍 Letakkan di:

```
hasil/hasil3.png
```

![Struktur](hasil/hasil3.png)

---

## 🧠 Analisis Hasil

* Threshold biasa kurang optimal jika pencahayaan tidak merata
* Adaptive threshold lebih fleksibel karena menyesuaikan area lokal
* Otsu memberikan hasil optimal secara otomatis
* Edge detection membantu memperjelas batas objek

---

## 🧾 Kesimpulan

Pengolahan citra dilakukan melalui beberapa tahap penting yaitu konversi citra, segmentasi, dan deteksi tepi. Metode thresholding yang lebih adaptif seperti Otsu dan Adaptive menghasilkan segmentasi yang lebih baik dibandingkan metode threshold biasa.

---

## 🚀 Cara Menjalankan

1. Install library:

```
pip install opencv-python matplotlib
```

2. Jalankan:

```
python main.py
```

---

## 👤 Author

Nama: (Isi Nama Kamu)
NIM: (Isi NIM Kamu)
