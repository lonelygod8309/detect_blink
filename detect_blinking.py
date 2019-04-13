import pyautogui
import tkinter.messagebox
import tkinter
from tkinter import *
from scipy.spatial import distance as dist
from imutils.video import VideoStream
from imutils.video import FPS
from imutils import face_utils
import argparse
import imutils
import time
import dlib
import sys
import cv2
import pyautogui
from win32 import win32api
from win32 import win32con
import threading


class calculator(threading.Thread):

    def __init__(self):
        frame = tkinter.Tk()
        frm_top = Frame()
        frm_top.pack(side=TOP, fill=Y, expand=YES, padx=15, pady=20)
        frm_left = Frame()
        frm_left.pack(side=LEFT, fill=BOTH)
        frm_number_1 = Frame()
        frm_number_1.pack(side=LEFT, fill=BOTH, padx=5)
        frm_number_2 = Frame()
        frm_number_2.pack(side=LEFT, fill=BOTH, padx=5)
        frm_number_3 = Frame()
        frm_number_3.pack(side=LEFT, fill=BOTH, padx=5)
        frm_right = Frame()
        frm_right.pack(side=LEFT)
        img_1 = tkinter.PhotoImage(file="./img/1.png")
        img_2 = tkinter.PhotoImage(file="./img/2.png")
        img_3 = tkinter.PhotoImage(file="./img/3.png")
        img_4 = tkinter.PhotoImage(file="./img/4.png")
        img_5 = tkinter.PhotoImage(file="./img/5.png")
        img_6 = tkinter.PhotoImage(file="./img/6.png")
        img_7 = tkinter.PhotoImage(file="./img/7.png")
        img_8 = tkinter.PhotoImage(file="./img/8.png")
        img_9 = tkinter.PhotoImage(file="./img/9.png")
        img_0 = tkinter.PhotoImage(file="./img/0.png")
        img_add = tkinter.PhotoImage(file="./img/+.png")
        img_sub = tkinter.PhotoImage(file="./img/-.png")
        img_mul = tkinter.PhotoImage(file="./img/mult.png")
        img_dev = tkinter.PhotoImage(file="./img/div.png")
        img_CE = tkinter.PhotoImage(file="./img/CE.png")
        img_equal = tkinter.PhotoImage(file="./img/equal.png")
        self.result = tkinter.StringVar()
        self.data = self.result.get()
        self.result.set(0)
        frame.geometry('1320x960')
        frame.title('Eyecontrol')

        self.lab = tkinter.Label(frm_top, bd=3, bg='white', font=('宋体', 50), anchor='e', textvariable=self.result)

        '''按钮'''

        self.btn_1 = tkinter.Button(frm_number_1, image=img_1, width=150, height=150,
                                    command=lambda: self.pressnum('1'))
        self.btn_2 = tkinter.Button(frm_number_2, image=img_2, width=150, height=150,
                                    command=lambda: self.pressnum('2'))
        self.btn_3 = tkinter.Button(frm_number_3, image=img_3, width=150, height=150,
                                    command=lambda: self.pressnum('3'))
        self.btn_4 = tkinter.Button(frm_number_1, image=img_4, width=150, height=150,
                                    command=lambda: self.pressnum('4'))
        self.btn_5 = tkinter.Button(frm_number_2,  image=img_5, width=150, height=150,
                                    command=lambda: self.pressnum('5'))
        self.btn_6 = tkinter.Button(frm_number_3,  image=img_6, width=150, height=150,
                                    command=lambda: self.pressnum('6'))
        self.btn_7 = tkinter.Button(frm_number_1,  image=img_7, width=150, height=150,
                                    command=lambda: self.pressnum('7'))
        self.btn_8 = tkinter.Button(frm_number_2,  image=img_8, width=150, height=150,
                                    command=lambda: self.pressnum('8'))
        self.btn_0 = tkinter.Button(frm_number_2,  image=img_0, width=150, height=150,
                                    command=lambda: self.pressnum('0'))
        self.btn_9 = tkinter.Button(frm_number_3,image=img_9, width=150, height=150,
                                    command=lambda: self.pressnum('9'))

        self.btn_add = tkinter.Button(frm_right, relief='groove', image=img_add, width=150, height=150,
                                      command=lambda: self.pressCompute('+'))
        self.btn_sub = tkinter.Button(frm_right, relief='groove', image=img_sub, width=150, height=150,
                                      command=lambda: self.pressCompute('-'))
        self.btn_mul = tkinter.Button(frm_right, relief='groove', image=img_mul, width=150, height=150,
                                      command=lambda: self.pressCompute('*'))
        self.btn_dev = tkinter.Button(frm_right, relief='groove', image=img_dev, width=150, height=150,
                                      command=lambda: self.pressCompute('/'))
        self.btn_CE = tkinter.Button(frm_number_3, relief='groove', image=img_CE, width=150, height=150,
                                     command=lambda: self.pressCompute('AC'))
        self.btnequal = tkinter.Button(frm_number_1, text='save', relief='groove', image=img_equal,
                                      font=('黑体', 45), command=lambda: self.pressEqual())
        self.lab.pack(ipadx=150, ipady=15)
        a = 80
        b = 20

        self.btn_1.pack(ipadx=a, ipady=b)
        self.btn_2.pack(ipadx=a, ipady=b)
        self.btn_3.pack(ipadx=a, ipady=b)
        self.btn_4.pack(ipadx=a, ipady=b)
        self.btn_5.pack(ipadx=a, ipady=b)
        self.btn_6.pack(ipadx=a, ipady=b)
        self.btn_7.pack(ipadx=a, ipady=b)
        self.btn_8.pack(ipadx=a, ipady=b)
        self.btn_9.pack(ipadx=a, ipady=b)
        self.btn_0.pack(ipadx=a, ipady=b)
        self.btn_add.pack(ipadx=a, ipady=b)
        self.btn_sub.pack(ipadx=a, ipady=b)
        self.btn_mul.pack(ipadx=a, ipady=b)
        self.btn_dev.pack(ipadx=a, ipady=b)
        self.btn_CE.pack(ipadx=a, ipady=b)
        self.btnequal.pack()

        self.lists = []
        self.isPressSign = False
        self.isPressNum = False
        tkinter.mainloop()


        # 计算器主界面摆

    def pressnum(self, num):
            if self.isPressSign == False:
                pass
            else:  # 重新将运算符号状态设置为否
                self.result.set(0)
                self.isPressSign = False
            oldnum = self.result.get()  # 第一步
            if oldnum == '0':  # 如过界面上数字为0 则获取按下的数字
                self.result.set(num)
            else:  # 如果界面上的而数字不是0  则链接上新按下的数字
                newnum = oldnum + num
                self.result.set(newnum)  # 将按下的数字写到面板中

    def pressCompute(self, sign):
        num = self.result.get()  # 获取界面数字
        self.lists.append(num)  # 保存界面获取的数字到列表中

        self.lists.append(sign)  # 讲按下的运算符号保存到列表中
        self.isPressSign = True

        if sign == 'AC':  # 如果按下的是'AC'按键，则清空列表内容，讲屏幕上的数字键设置为默认数字0
            self.lists.clear()
            self.result.set(0)

    def pressEqual(self):

        curnum = self.result.get()  # 设置当前数字变量，并获取添加到列表
        self.lists.append(curnum)

        computrStr = ''.join(self.lists)  # 讲列表内容用join命令将字符串链接起来
        endNum = eval(computrStr)  # 用eval命令运算字符串中的内容
        self.result.set(endNum)  # 讲运算结果显示到屏幕1
        self.lists.clear()


class vedio(threading.Thread):
 def eye_aspect_ratio(eye):
    # compute the euclidean distances between the two sets of
    # vertical eye landmarks (x, y)-coordinates
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])

    # compute the euclidean distance between the horizontal
    # eye landmark (x, y)-coordinates
    C = dist.euclidean(eye[0], eye[3])

    # compute the eye aspect ratio
    ear = (A + B) / (2.0 * C)

    # return the eye aspect ratio
    return ear


# construct the argument parse and parse the arguments


 def run(self):
     ap = argparse.ArgumentParser()
     ap.add_argument("-p", "--shape-predictor", default='shape_predictor_68_face_landmarks.dat')
     args = vars(ap.parse_args())
     EYE_AR_THRESH = 0.2
     EYE_AR_CONSEC_FRAMES = 2
     COUNTER = 0
     TOTAL = 0

     print("[INFO] loading facial landmark predictor...")
     detector = dlib.get_frontal_face_detector()
     predictor = dlib.shape_predictor(args["shape_predictor"])

     (lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
     (rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]
     (uStart, dEnd) = face_utils.FACIAL_LANDMARKS_IDXS["nose"]

     vs = VideoStream(src=0).start()
# vs = VideoStream(usePiCamera=True).start()
     fileStream = False

     #fourcc = cv2.VideoWriter_fourcc(*'DIVX')
     #out = cv2.VideoWriter('output.avi', fourcc, 2.6, (1600, 1000))
     time.sleep(1.0)
     fps = FPS().start()
# loop over frames from the video stream
     while True:
         if fileStream and not vs.more():
             break

         frame = vs.read()
         frame = imutils.resize(frame, width=1800,height=850)
         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
         rects = detector(gray, 0)
         for rect in rects:
             shape = predictor(gray, rect)
             points = face_utils.shape_to_np(shape)
             leftEye = points[42:48]  # 取出左眼对应的特征点
             rightEye = points[36:42]  # 取出右眼对应的特征点
             leftEAR = self.eye_aspect_ratio(leftEye)
             rightEAR = self.eye_aspect_ratio(rightEye)
             ear = (leftEAR + rightEAR) / 2.0
             x = leftEye[0]
             x1 = 1800 - x[0]
             pyautogui.moveTo(x1, x[1])
             leftEyeHull = cv2.convexHull(leftEye)
             rightEyeHull = cv2.convexHull(rightEye)
             cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
             cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)
             if ear < EYE_AR_THRESH:
                 COUNTER += 1
                 win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                 win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

             if COUNTER >= EYE_AR_CONSEC_FRAMES:
                 TOTAL += 1
                 COUNTER = 0

             cv2.putText(frame, "Blinks: {}".format(TOTAL), (10, 30),
                         cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
             cv2.putText(frame, "EAR: {:.2f}".format(ear), (300, 30),
                         cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
             #frame1 = cv2.resize(frame, (1600, 1000))
             #out.write(frame1)
         cv2.imshow("Frame", frame)
         key = cv2.waitKey(1) & 0xFF

         if key == ord("q"):
             break

     fps.stop()
     print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
     print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
     vs.stream.release()
     #out.release()
     cv2.destroyAllWindows()


# do a bit of cleanup
thread_1 = threading.Thread(target=calculator)  # 实例化一个线程对象，使线程执行这个函数
thread_1.start()
thread_2 = threading.Thread(target=vedio.run(vedio))





