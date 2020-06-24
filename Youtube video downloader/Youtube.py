from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import os
from pytube import YouTube ,Stream,streams,StreamQuery

folderpath = ""
filesizeinbytes = 0
maxfilesize = 0
def clear():
    loading.config(text="")
    entryurl.delete(0,END)


def browse():
    global folderpath
    folderpath = filedialog.askdirectory()
    if len(folderpath) > 1:
        entrypath.delete(0,END)
        entrypath.insert(0,folderpath)
    else:
        entrypath.delete(0, END)
        entrypath.insert(0, "Please specify path")


def download():
    loading.config(text = "")
    global filesizeinbytes,maxfilesize,folderpath
    choice = ytbchoices.get()
    video = entryurl.get()
    if len(video)>1:
        yt = YouTube(video , on_progress_callback =  progress)
        print("Video title is : ",yt.title)
        if choice == choices[0]:
            print("720p downloading...")
            selectedvideo = yt.streams.filter(progressive=True,res = "720p").first()

        elif choice == choices[1]:
            print("360p downloading...")
            selectedvideo = yt.streams.filter(progressive=True, res="360p").first()

        elif choice == choices[2]:
            print("144p downloading...")
            selectedvideo = yt.streams.filter(progressive=True).last()


        elif choice == choices[3]:
            print("mp3 song downloading...")
            selectedvideo = yt.streams.filter(only_audio= True).first()


        if selectedvideo == None:
            loading.config(text="Please choose another format")
        else:
            filesizeinbytes = selectedvideo.filesize
            maxfilesize = filesizeinbytes/1024000
            mb = str(maxfilesize) + "MB"
            print("File size is : {:00.00f} MB".format(maxfilesize))

            selectedvideo.download(folderpath)
            print("Downloaded at {}".format(folderpath))
            complete()

    else:
        entryurl.delete(0,END)
        entryurl.insert(0,"Please Enter Youtube Link")


def progress(chunk = None, file_handler = None,bytes_remaining = None):
    percent = (100*(filesizeinbytes - bytes_remaining)/filesizeinbytes)
    print("{:00.0f}% downloaded ".format(percent))

def complete():
    loading.config(text = "Download Complete!")

root = Tk()
root.title("Youtube video Downloader")
root.geometry("700x500")
root.wm_iconbitmap('ytb.ico')
root.config(bg = "#EAECF0")
ytbeurl = StringVar()
head = Label(text = "Download any youtube video you like" , font = 'Times 30 bold' ,bg = "#EAECF0" , fg = "#061833")
head.grid(row = 1,column = 0,pady = 15)
#enter url here
entryurl = Entry(root,textvariable = ytbeurl , bg = "#DDDDDD" , fg ="#061833", font = 'Courier 10 italic',width = 40 )
entryurl.insert(0, 'Paste link here')
entryurl.grid(row = 3, column = 0, ipady = 8)

#enter path
entrypath = Entry(root, bg = "#DDDDDD" , fg ="#061833", font = 'Courier 10 italic',width = 40)
entrypath.insert(0,'Enter path where you want to download.')

entrypath.grid(ipady = 8,pady = 25)


#browse button
browsebutton = Button(root,text = "Browse",bg= "#32383E",fg = "#CCD8E3",command = browse ,width ="15",height = "2")
browsebutton.place(x = 480,y = 140)

clearbutton = Button(root,text = "Clear",bg= "#32383E",fg = "#CCD8E3",command = clear,width  = "15",height  = "2")
clearbutton.place(x = 480,y = 80)
#label coose
chooselabel = Label(root, text ="Choose what to download" , bg= "#EAECF0",fg ="#061833",font ="Times 15 italic")
chooselabel.place(x = 150,y =200)
choices = ["Mp4 720p" , "Mp4 360p" ,"Mp4 144p" , "song mp3"]
ytbchoices = ttk.Combobox(root, value = choices,width= "50")
ytbchoices.place(x = 150,y = 230)

#download button
dldbutton = Button(root,text ="Download" , command = download, bg ="#3A4FA8" , fg = "#CCD8E3", width = "20",height = "2" , activebackground = "#2B4ACC")
dldbutton.place(x = 250, y = 280)

loading = Label(root,text="",bg= "#EAECF0",fg ="#061833",font ="Times 15 italic")
loading.place(x = 230, y = 330)
#about
aboutlabel = Label(root,text="With Love By Ritika Goyal" , font = 'Times 10 bold' ,bg = "#EAECF0" , fg = "#061833")
aboutlabel.place(x = 530, y = 450)
root.mainloop()