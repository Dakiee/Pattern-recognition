import cv2
import glob

# Folder доторх бүх jpg өргөтөлтэй файлуудын нэрийг хүснэгт болгон авч байна
jpgFilenamesList = glob.glob('*.jpg')

# Нийт дундажийн хувьсагч
avg_img = 0

# Нийт зургийн дундажийн хувьсагч
total_img = len(jpgFilenamesList)

# Нийт зургийн хэмжээгээр давталт гүйлгэх
for i in range(len(jpgFilenamesList)):
    img = cv2.imread(f'{jpgFilenamesList[i]}')
    grayscale_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    resized_img = cv2.resize(grayscale_img, [400, 500])
    avg_img = avg_img + (resized_img/total_img)

for j in range(len(jpgFilenamesList)):
    img = cv2.imread(f'{jpgFilenamesList[j]}')
    grayscale_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    resized_img = cv2.resize(grayscale_img, [400, 500])
    img_sub = avg_img - resized_img
    cv2.imwrite(f'result2/img{j}.jpg', img_sub)
