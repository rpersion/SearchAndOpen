import os, sys
import time
import datetime
#from PIL import Image

#FILE EXTENSIONS TO LAUNCH
exts = ["jpg","jpeg","png","gif","tiff","bmp"]

#START MESSAGE
print("##### ROSTISLAV PERSION - IMAGE WATCH/LOADER 1.00 #####")
print("MONITORING LOCAL FOLDER...")

#INITIALIZE FILE LIST
myfiles_new = os.listdir()

#MAIN LOOP
while True:

    #PAUSE FOR A FEW SECONDS
    time.sleep(5)

    #SAVE OLD FILE LIST, LOAD NEW FILE LIST
    myfiles_old = myfiles_new.copy()
    myfiles_new = os.listdir()

    #FIND DIFFERENCE BETWEEN NEW FILE LIST AND OLD FILE LIST
    myfiles_dif = list(set(myfiles_new) - set(myfiles_old))

    #TRAVERSE NEW FILES
    for myfiles_dir in myfiles_dif:

        #FIND FILE EXTANSION FOR FILE
        myfile_ext = myfiles_dir.split(".")[-1]
        
        #CHECK IF FILE EXTANSION EXISTS IN FILE EXTENSION LIST
        if myfile_ext.lower() in exts:
            
            #SHOW IMAGE FILE
            os.system(myfiles_dir)

            #img = Image.open(myfiles_dir)
            #img.show()
            
            #GENERATE TIMESTAMP
            now1 = datetime.datetime.now()
            now2 = now1.strftime("%d/%m/%Y %H:%M:%S")
            
            #OUTPUT NEW FILE FOUND
            print(now2 + " - NEW FILE FOUND: " + myfiles_dir)




