import os
import shutil
import random

# For saving purposes only
#counter = random.randint(1000, 9999)

# Reverses the edited picture back to its original size
os.system(r"magick C:\Users\K017-Labor\Desktop\SetupFolder\Edited_Pics\index.png -resize 200% C:\Users\K017-Labor\Desktop\SetupFolder\Edited_Pics\index.png")

# Adding the QR-Code on the top left of the picture
os.system(r"magick composite -gravity NorthWest -geometry +20+5 C:\Users\K017-Labor\Desktop\SetupFolder\QR-Codes\qrTBS.png C:\Users\K017-Labor\Desktop\SetupFolder\Edited_Pics\index.png C:\Users\K017-Labor\Desktop\Final.png")


#source = "C:\\Users\\K017-Labor\\Desktop\\Final.png"
#new_file_name = "image_" + str(counter) + ".png"
#destination = "C:\\Users\\K017-Labor\\Desktop\\SetupFolder\\SavedPics\\"

# Copies the finished picture on desktop for printing

#shutil.copy2(source, destination, new_file_name)

os.system("echo Your picture is ready to print now!")

 #   result_name = filename2
  #  print result_name
   # i = 0

    # Check if file exists
    #if arcpy.Exists(draftloc + "\\" + result_name):
        # If it does, increment i by 1
     #   i+=1
        # While each successive filename (including i) does not exists, then save the next filename
       # while not arcpy.Exists(draftloc + "\\" + shortname + "_" + str(i) + extension):                
      #      mxd.saveACopy(draftloc + "\\" + shortname + "_" + str(i) + extension)            
    # else if the original file didn't satisfy the if, the save it.
    #else:           
     #   mxd.saveACopy(draftloc + "\\" + result_name)

