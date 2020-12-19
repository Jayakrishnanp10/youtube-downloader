from pytube import YouTube
from tkinter import *
from tkinter import filedialog
from tkinter import ttk


class youtube(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("YOUTUBE DOWNLOADER")
        self.master.geometry("500x200")
        self.master.configure(bg="#e85348")
        self.p1 = PhotoImage(file ="C:/Users/pjaya/Documents/appu/python/youtube/yt.png")
        self.master.iconphoto(False, self.p1)
        self.configure(bg="#e85348")
        self.style=ttk.Style()
        self.style.theme_use("clam")
        self.grid()
        self.label1=Label(self,text="YOUTUBE DOWNLOADER")
        self.label1.grid(row=0,column=1,columnspan=3)
        self.label1.configure(bg="#e85348",fg='white',font='Helvetica 18 bold')
        self.label2=Label(self,text="Url:",font='Helvetica 8 bold')
        self.label2.grid(row=1,column=0,columnspan=1)
        self.label2.configure(bg="#e85348",fg='white')
        self.url=StringVar()
        self.urlentry=ttk.Entry(self,textvariable=self.url,width=50)
        self.urlentry.grid(row=1,column=1,columnspan=5)
        self.label3=Label(self,text="Location:",font='Helvetica 8 bold')
        self.label3.grid(row=2,column=0,columnspan=1)
        self.label3.configure(bg="#e85348",fg='white')
        self.loc=StringVar()
        self.locentry=ttk.Entry(self,textvariable=self.loc,width=50)
        self.locentry.grid(row=2,column=1,columnspan=5)
        self.locb=ttk.Button(self,text="select folder",command=self.folselect)
        self.locb.grid(row=2,column=6,columnspan=3)
        self.label3=Label(self,text="Resolution:",font='Helvetica 8 bold')
        self.label3.grid(row=3,column=0,columnspan=1)
        self.label3.configure(bg="#e85348",fg='white')
        self.reso=StringVar()
        self.resselect=ttk.Combobox(self,textvariable=self.reso)
        self.resselect['values']=('144p','240p','360p','480p','720p','1080p','1440p','2160p')
        self.resselect.grid(row=3,column=1,columnspan=1)
        self.resselect.current(4)
        self.submit=ttk.Button(self,text="download",command=self.ydownload)
        self.submit.grid(row=3,column=3,columnspan=3)
        
        
        
    def ydownload(self):
        YouTube(self.url.get()).streams.get_by_resolution(self.reso.get()).download(self.loc.get())

    
    def folselect(self):
        self.folder=filedialog.askdirectory()
        self.loc.set(self.folder)
        




def main():
    youtube().mainloop()

main()

