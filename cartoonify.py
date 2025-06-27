import cv2

def cartoonify(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.adaptiveThreshold(
        cv2.medianBlur(gray, 5), 255, cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY, 9, 9
    )
    color = cv2.bilateralFilter(img, 9, 300, 300)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    
    cv2.imshow("Cartoonified", cartoon)
    cv2.imwrite("cartoonified.jpg", cartoon)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

cartoonify("sample_image.jpg")
