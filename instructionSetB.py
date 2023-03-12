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
