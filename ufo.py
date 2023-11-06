import tkinter as tk
from tkinter import ttk
import os
import shutil

def again():
    frame.pack_forget()
    f.pack()

def pathinfo():
    path=e.get()
    os.chdir(path)
    os.mkdir('Audio_files_byufo')
    os.mkdir('compressed_files_byufo')
    os.mkdir('Disc_and_media_files_byufo')
    os.mkdir('Database_files_byufo')
    os.mkdir('E-mail_files_byufo')
    os.mkdir('Programming_files_byufo')
    os.mkdir('Image_files_byufo')
    os.mkdir('Presentation_files_byufo')
    os.mkdir('Spreadsheet_files_byufo')
    os.mkdir('System_files_byufo')
    os.mkdir('Video_files_byufo')
    os.mkdir('text_files_byufo')
    files=os.listdir(path)
    for i in files:
        _,ext=os.path.splitext(i)
        if ext in ('.aif','.cda','.mid' ,'.midi' ,'.mp3','.mpa','.ogg' ,'.wav' ,'.wma' ,'.wpl'): 
            shutil.move(i,'Audio_files_byufo')
        elif ext in ('.7z','.arj' ,'.deb','.pkg' ,'.rar' ,'.rpm' ,'.tar.gz','.z' ,'.zip'):
            shutil.move(i,'compressed_files_byufo')
        elif ext in ('.bin','.dmg','.iso','.toast','.vcd'): 
            shutil.move(i,'Disc_and_media_files_byufo')
        elif ext in ('.csv','.dat' ,'.db' ,'.dbf' ,'.log','.mdb','.sav','.sql' ,'.tar'): 
            shutil.move(i,'Database_files_byufo')
        elif ext in ('.email' ,'.eml','.emlx','.msg','.oft','.ost ','.pst ','.vcf '): 
            shutil.move(i,'E-mail_files_byufo')
        elif ext in ('.c','.class','.cpp' ,'.cs' ,'.h' ,'.java','.pl','.sh','.swift','.vb' ,'.apk' ,'.bat','.bin' ,'.cgi' ,'.pl' ,'.com' ,'.exe' ,'.gadget ','.jar','.msi','.py'): 
            shutil.move(i,'Programming_files_byufo')
        elif ext in ('.ai','.bmp','.gif' ,'.ico' ,'.jpeg' ,'.jpg' ,'.png' ,'.ps' ,'.psd','.svg'): 
            shutil.move(i,'Image_files_byufo')
        elif ext in ('.key','.odp','.pps','.ppt','.pptx' ,'.tif ','.tiff' ,'.wsf','.pptm'): 
            shutil.move(i,'Presentation_files_byufo')
        elif ext in ('.ods','.xls','.xlsm','.xlsx'): 
            shutil.move(i,'Spreadsheet_files_byufo')
        elif ext in ('.bak','.cab' ,'.cfg','.cpl','.cur' ,'.dll','.dmp' ,'.drv' ,'.icns' ,'.ico' ,'.ini' ,'.lnk' ,'.msi','.sys' ,'.tmp' ): 
            shutil.move(i,'System_files_byufo')
        elif ext in ('.3g2','.3gp','.avi' ,'.flv','.h264','.m4v' ,'.mkv ','.mov' ,'.mp4' ,'.mpg' ,'.mpeg' ,'.rm' ,'.swf' ,'.vob' ): 
            shutil.move(i,'Video_files_byufo')
        elif ext in ('.doc','.docx','.odte','.pdf','.rtf' ,'.tex','.txt' ,'.wpd' ,'.wmv' ): 
            shutil.move(i,'text_files_byufo')
        else:
            pass
    if len(os.listdir(path+'\Audio_files_byufo')) == 0:
        os.rmdir('Audio_files_byufo')
    if len(os.listdir(path+'\compressed_files_byufo')) == 0:
        os.rmdir('compressed_files_byufo')
    if len(os.listdir(path+'\Disc_and_media_files_byufo')) == 0:
        os.rmdir('Disc_and_media_files_byufo')
    if len(os.listdir(path+'\Database_files_byufo')) == 0:
        os.rmdir('Database_files_byufo')
    if len(os.listdir(path+'\E-mail_files_byufo')) == 0:
        os.rmdir('E-mail_files_byufo')
    if len(os.listdir(path+'\Programming_files_byufo')) == 0:
        os.rmdir('Programming_files_byufo')
    if len(os.listdir(path+'\Image_files_byufo')) == 0:
        os.rmdir('Image_files_byufo')
    if len(os.listdir(path+'\Presentation_files_byufo')) == 0:
        os.rmdir('Presentation_files_byufo')
    if len(os.listdir(path+'\Spreadsheet_files_byufo')) == 0:
        os.rmdir('Spreadsheet_files_byufo')
    if len(os.listdir(path+'\System_files_byufo')) == 0:
        os.rmdir('System_files_byufo')
    if len(os.listdir(path+'\Video_files_byufo')) == 0:
        os.rmdir('Video_files_byufo')
    if len(os.listdir(path+r'\text_files_byufo')) == 0:
        os.rmdir('text_files_byufo')
    
    f.pack_forget()
    frame.pack()
    return 0
   
            


root=tk.Tk()
w=root.winfo_screenwidth()
h=root.winfo_screenheight()
root.geometry(f"{w}x{h-50}+0+0")
root.title("UFO(Unique File Organizer)")
f=ttk.Frame(root)
ttk.Label(f,text="WELCOME TO U.F.O ( Unique File Organizer ) !!!",font="Andalus 24 bold").pack(side="top",anchor="center",pady=20)
ttk.Label(f,text="Please enter the path of the location",font='Andalus 16 bold').pack(side="top",anchor="center",pady=20)
e=ttk.Entry(f,width=80)
e.pack(side='top',anchor="center",ipady=8)
button=ttk.Button(f,text="Decorate !",command=pathinfo)
button.pack(side='top',anchor='center',pady=15)
f.pack()

frame=ttk.Frame(root)
ttk.Label(frame,text="WELCOME TO U.F.O ( Unique File Organizer ) !!!",font="Andalus 24 bold").pack(side="top",anchor="center",pady=20)
ttk.Label(frame,text="FILE ORGANIZING PROCESS HAS BEEN COMPLETED !\nPLEASE LOOK AT THE GIVEN LOCATION",font='Andalus 16 bold').pack(side="top",anchor="center",pady=20)
ttk.Button(frame,text="Decorate another location!",command=again).pack(side='top',anchor='center',pady=20)
# frame.pack()
root.mainloop()