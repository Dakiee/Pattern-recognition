import cv2
import numpy as np

# Өнгөт зургаа унших
img1 = cv2.imread('flower.jpg')
img2 = cv2.imread('flower1.jpg')

# Зургийг саарал өнгөтэй болгож хувиргах
gray_image1 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
gray_image2 = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)

# Зургуудын дундажийг олохын тулд ижил хэмжээтэй болгох
gray_image1 = cv2.resize(gray_image1, [400, 500])
gray_image2 = cv2.resize(gray_image2, [400, 500])

# Зургуудын дундажийг олохын тулд ижил хэмжээтэй болгох
avg_img = gray_image1/2 + gray_image2/2

# Зураг 1 болон 2 ийн дундаж зурагнаас хэр ялгаатайг олж байна 
img1_sub = avg_img - gray_image1
img2_sub = avg_img - gray_image2

# Саарал өнгийн зургийг result дотор хадгалах
cv2.imwrite('result/flower_grayscale_1.jpg', img1_sub)
cv2.imwrite('result/flower_grayscale_2.jpg', img2_sub)
