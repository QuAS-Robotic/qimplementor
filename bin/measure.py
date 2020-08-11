from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import os

import imutils
import cv2
def run(picture,width = 30,hint= "TREE"):
        global window_flag
        window_flag = False
        if hint == "CCOMP":
                method = cv2.RETR_CCOMP
                method2 = cv2.CHAIN_APPROX_NONE
        elif hint == "TREE":
                method = cv2.RETR_TREE
                method2 = cv2.CHAIN_APPROX_SIMPLE
        else :
                method = cv2.RETR_TREE
                method2 = cv2.CHAIN_APPROX_SIMPLE

        image = picture
        results = []
        def midpoint(ptA, ptB):  # orta noktayı bulmayı sağlıyor
                return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)

        # görüntüyü yükleyin, gri tonlamaya dönüştürün ve biraz bulanıklaştırın

        # kenar haritasında konturlar bul
        try:
                cnts, hierarchy = cv2.findContours(image.copy(),method, method2)
        except:
                image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
                cnts, hierarchy = cv2.findContours(image.copy(), method, method2)

        # cnts = imutils.grab_contours(cnts)

        # sort the contours from left-to-right and initialize the
        # 'pixels per metric' calibration variable
        (cnts, _) = contours.sort_contours(cnts)
        hierarchy = hierarchy[0]
        global pixelsPerMetric
        pixelsPerMetric = None
        # loop over the contours individually

        # for c in cnts:
        mask = np.zeros(image.shape[:2], dtype=image.dtype)
        def show(c):
                global window_flag
                # if the contour is not sufficiently large, ignore it
                if cv2.contourArea(c) < 100:
                        return

                # compute the rotated bounding box of the contour
                global pixelsPerMetric
                orig = image.copy()
                box = cv2.minAreaRect(c)
                box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
                box = np.array(box, dtype="int")

                # order the points in the contour such that they appear
                # in top-left, top-right, bottom-right, and bottom-left
                # order, then draw the outline of the rotated bounding
                # box
                box = perspective.order_points(box)
                cv2.drawContours(orig, [box.astype("int")], -1, (0, 255, 0), 2)

                # loop over the original points and draw them
                # cv2.circle daire çizer----cv2.circle(image, center_coordinates, radius, color, thickness)---
                for (x, y) in box:
                        cv2.circle(orig, (int(x), int(y)), 5, (0, 0, 255), -1)

                # unpack the ordered bounding box, then compute the midpoint
                # between the top-left and top-right coordinates, followed by
                # the midpoint between bottom-left and bottom-right coordinates
                # çizilen kutunun alt ve üst kenarlarının orta noktalarını buldu
                (tl, tr, br, bl) = box
                (tltrX, tltrY) = midpoint(tl, tr)
                (blbrX, blbrY) = midpoint(bl, br)

                # compute the midpoint between the top-left and top-right points,
                # followed by the midpoint between the top-righ and bottom-right
                # orta noktaların arasını hesapladı
                (tlblX, tlblY) = midpoint(tl, bl)
                (trbrX, trbrY) = midpoint(tr, br)

                # draw the midpoints on the image
                cv2.circle(orig, (int(tltrX), int(tltrY)), 5, (255, 0, 0), -1)
                cv2.circle(orig, (int(blbrX), int(blbrY)), 5, (255, 0, 0), -1)
                cv2.circle(orig, (int(tlblX), int(tlblY)), 5, (255, 0, 0), -1)
                cv2.circle(orig, (int(trbrX), int(trbrY)), 5, (255, 0, 0), -1)

                # draw lines between the midpoints
                cv2.line(orig, (int(tltrX), int(tltrY)), (int(blbrX), int(blbrY)), (255, 0, 255), 2)
                cv2.line(orig, (int(tlblX), int(tlblY)), (int(trbrX), int(trbrY)), (255, 0, 255), 2)

                # compute the Euclidean distance between the midpoints
                dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))
                dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))

                # if the pixels per metric has not been initialized, then
                # compute it as the ratio of pixels to supplied metric
                # (in this case, inches)
                if pixelsPerMetric is None:
                        pixelsPerMetric = dB / width
                # compute the size of the object

                dimA = dA / pixelsPerMetric

                dimB = dB / pixelsPerMetric
                if dimA < width/5 or dimB < width/5:
                        return
                # draw the object sizes on the image
                cv2.putText(orig, "{:.2f}mm".format(dimA),
                            (int(tltrX - 15), int(tltrY - 10)), cv2.FONT_HERSHEY_SIMPLEX,
                            0.65, (255, 255, 255), 2)
                cv2.putText(orig, "{:.2f}mm".format(dimB),
                            (int(trbrX + 10), int(trbrY)), cv2.FONT_HERSHEY_SIMPLEX,
                            0.65, (255, 255, 255), 2)

                # show the output image
                if window_flag != True:
                        cv2.namedWindow("Sonuc Ekrani",cv2.WINDOW_NORMAL)
                        window_flag = True
                #cv2.resizeWindow("Ölçüm Resmi")
                cv2.imshow("Sonuc Ekrani", orig)

                cv2.waitKey(0)
                return (round(dimA,2),round(dimB,2))

        for component in zip(cnts, hierarchy):
                currentContour = component[0]
                currentHierarchy = component[1]


                if currentHierarchy[2] < 0:
                        results.append(show(currentContour))
                elif currentHierarchy[3] < 0:
                        results.append(show(currentContour))
                if results[-1] == None:
                        results.pop()
        window_flag = False
        return results
def go (picture):
        image = cv2.imread(picture)
        #r = cv2.selectROI(image)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (13, 13), 0)
        #kes =gray[r[1]:r[1]+r[3], r[0]:r[0]+r[2]]

        # kenar algılar ardından dilatasyon + erozyon uygulayıp
        # nesne kenarları arasındaki boşlukları kapatır
        image = cv2.Canny(gray, 50, 150)
        #gray[r[1]:r[1]+r[3], r[0]:r[0]+r[2]] = cimage
        #cv2.imshow("im",gray)
        #cv2.waitKey(0)

        image = cv2.dilate(image, None, iterations=1)
        image = cv2.erode(image, None, iterations=1)
        run(picture=image, width=80)
#go(picture="imm.png")

def selection (img =cv2.imread("temp.png")):
        global drawing,mode
        drawing = False
        def interactive_drawing(event, x, y, flags, param):
                global mouse_x, mouse_y, drawing, draw_x,draw_y,rad,img2,ix,iy,center_x,center_y
                if event == cv2.EVENT_LBUTTONDOWN:
                        rad = 0
                        drawing = True
                        center_x, center_y = x, y
                        img2 = np.zeros((512, 512, 3), np.uint8)
                        cv2.imshow('begueradj',img2)
                elif event == cv2.EVENT_MOUSEMOVE:

                        if drawing == True:
                                img2 = np.zeros((512, 512, 3), np.uint8)
                                print("x :", x, "ix : ", ix, "rad :", rad)
                                if x > ix or y > iy:
                                        rad += 1
                                        ix = x
                                elif x < ix or y<iy and rad > 1:
                                        ix = x
                                        rad -= 1
                                print("center : ",center_x,center_y)
                                cv2.circle(img2, (center_x, center_y), rad, (0, 0, 255), 3)
                                img = img2
                                cv2.imshow('begueradj', img2)
                elif event == cv2.EVENT_LBUTTONUP:
                        drawing = False
                        img2 = np.zeros((512, 512, 3), np.uint8)
                        cv2.circle(img2, (center_x, center_y), rad, (0, 0, 255), 3)

                        cv2.imshow('begueradj', img2)
                        img = img2
                        # print x,y
                        # cv2.line(img,(x,y),(x,y),(0,0,255),10)
                return x, y

        img = np.zeros((512, 512, 3), np.uint8)
        global img2
        img2 = np.zeros((512, 512, 3), np.uint8)
        static = img2.copy()
        cv2.namedWindow('begueradj')
        cv2.setMouseCallback('begueradj', interactive_drawing)
        global rad,ix,iy
        ix = 0
        iy = 0
        rad = 0
        while (1):
                cv2.imshow('begueradj', img2)

                k = cv2.waitKey(1) & 0xFF
                if k == 27:
                        combined = img2[:, :, 0] + img2[:, :, 1] + img2[:, :, 2]
                        rows, cols = np.where(combined > 0)
                        print(rows,cols)
                        break
        cv2.destroyAllWindows()
if __name__ == "__main__":
        run(picture=cv2.imread("./temp/Canny.JPG"),width = 30)
        #selection()