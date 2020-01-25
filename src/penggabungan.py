import numpy as np
import cv2
r = np.reshape(np.arange(256*256)%256,(256,256))  # 256x256 piksel array dengan gradien horizontal dari 0 hingga 255 untuk saluran warna merah
g = np.zeros_like(r)  # array dengan ukuran dan tipe yang sama dengan r tetapi diisi dengan 0s untuk saluran warna hijau
b = r.T # Transposisi r akan memberikan gradien vertikal untuk saluran warna biru
cv2.imwrite('gradients.png', np.dstack([b,g,r]))  # Gambar OpenCV ditafsirkan sebagai BGR, array kedalaman-ditumpuk akan ditulis ke file PNG 8bit RGB yang disebut 'gradients.png'
# Hasil
True