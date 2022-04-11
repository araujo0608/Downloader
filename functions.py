from pytube import YouTube
from tkinter import *

save_path_video = "/home/eduardo/Videos" # Change this
save_path_audio = "/home/eduardo/Musica" # Change this

def spamMessage(message):
	top = Toplevel()
	
	top.geometry("350x150+420+400")
	top.resizable(True, True)

	lblMsg = Label(top, text=str(message), font='bold')
	lblMsg.config(font=40)
	lblMsg.pack()

def successMessageVideo():
	top = Toplevel()
	
	top.geometry("350x150+420+400")
	top.resizable(True, True)

	lblMsg = Label(top, text='Video Downloaded!\n Saved in ' + save_path_video, font='bold')
	lblMsg.config(font=40)
	lblMsg.pack()

def successMessageAudio():
	top = Toplevel()
	
	top.geometry("350x150+420+400")
	top.resizable(True, True)

	lblMsg = Label(top, text='Audio Downloaded!\n Saved in ' + save_path_audio, font='bold')
	lblMsg.config(font=40)
	lblMsg.pack()

def download(option, link):
	
	if option == 1:
		#Trying create an object
		try:
			yt = YouTube(link)
		except:
			spamMessage('Error: not able to find your link')

		video = yt.streams.filter(progressive=True).get_highest_resolution().itag

		try:
			# Downloading video
			yt.streams.get_by_itag(video).download(save_path_video)
		except:
			spamMessage("Error in downloading the video!")

		successMessageVideo()

	else:
		
		#Trying create an object
		try:
			yt = YouTube(link)
		except:
			spamMessage("Error: not able to find your link")


		audio = yt.streams.filter(only_audio=True).get_audio_only().itag

		try:
			# Downloading audio
			yt.streams.get_by_itag(audio).download(save_path_audio)
		except:
			spamMessage('Error in downloading the audio!')

		successMessageAudio()