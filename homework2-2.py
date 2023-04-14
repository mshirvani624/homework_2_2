import vlc
import cv2
import numpy as np
import time

class MyMediaPlayer():
	def __init__(self, name1):
		self.detector_face=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
		self.detector_eye=cv2.CascadeClassifier("haarcascade_eye.xml")
		self.cap=cv2.VideoCapture(0)

	def play_music(self,target_dir):
		music=vlc.MediaPlayer(target_dir)
		music.play()
		time.sleep(15)

	def show_film_demo(self,target_dir):
		img=cv2.imread(target_dir)
		img=cv2.resize(img,None,fx=1.5,fy=1.5)
		cv2.imshow("film_demo",img)
		cv2.waitKey(0)
		cv2.destroyAllWindows()

	def type_book_name(self,book_name):
		print(book_name)

	def stream_webcam(self):
		while True:
			ret, frame= self.cap.read()
			
			if ret:

				frame=cv2.flip(frame,1)
				gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
				results_face=self.detector_face.detectMultiScale(gray)
				
				for (x,y,w,h) in results_face:	
					cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
				
				gray_face=gray[x:x+w,y:y+h]
				results_eye=self.detector_eye.detectMultiScale(gray_face)
				for (a,b,c,d) in results_eye:
					cv2.rectangle(frame,(x+a,y+b),(x+a+c,y+b+d),(255,0,0),2)
				
				cv2.imshow("webcamasdfasdf",frame)
				
				q=cv2.waitKey(1)
				if q==ord('q'):
					break	
			else:
				break
		self.cap.release()
		cv2.destroyAllWindows()				

mp=MyMediaPlayer("Mohammad")
mp.stream_webcam()
while True:
	print("please select one number : :\n     1-music \n     2-movie\n     3-book\n")
	choise= input()
	if choise=="1":
		mp.play_music("music.mp3")
	elif choise=="2":
		mp.show_film_demo("It's a wonderful life.jpg")
	elif choise=="3":
		mp.type_book_name("Karamazof brothers")
	else:
		break

		
