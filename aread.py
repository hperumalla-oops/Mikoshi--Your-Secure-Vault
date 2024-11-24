import cv2 as cv
import pytesseract as tess
##tess.pytesseract.tesseract_cmd = r'C:\\\\Users\\\\USER\\\\AppData\\\\Local\\\\tesseract-OCR\\\\tesseract.exe'
def ocr_core(img):
    text = tess.image_to_string(img)
    return text

def gray(img):
    return cv.cvtColor(img, cv.COLOR_BGR2GRAY)


def remove_noise(img):
    return cv.medianBlur(img, 1)  ### some random value
 
def THing(img):
    return cv.threshold(img, 0, 255, cv.THRESH_BINARY +cv.THRESH_OTSU)[1]


##"C:\Users\Dell\Desktop\mongo\h1.jpg"

img= cv.imread(r"C:\Users\Dell\Desktop\mongo\bhavanaone.jpg")
#print(img.shape)
img=cv.resize(img, (750, 713))
# #cv.imshow("resized",img)
# img= gray(img)
# #cv.imshow("gray",img1)

# img= THing(img)
# cv.imshow("Thresholding",img)

# # img3= remove_noise(img2)
# # cv.imshow("removing noise",img3)

print(ocr_core(img))

if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyAllWindows()

