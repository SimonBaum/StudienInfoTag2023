import os
import shutil
import random

# For saving purposes only
counter = random.randint(1000, 9999)

# Reverses the edited picture back to its original size
os.system(r"magick C:\Users\K017-Labor\Desktop\SetupFolder\Edited_Pics\A.png -resize 200% C:\Users\K017-Labor\Desktop\SetupFolder\Edited_Pics\A.png")

# Adding the QR-Code on the top left of the picture
os.system(r"magick composite -gravity NorthWest C:\Users\K017-Labor\Desktop\SetupFolder\Edited_Pics\qrTestVerySmall.png C:\Users\K017-Labor\Desktop\SetupFolder\Edited_Pics\A.png C:\Users\K017-Labor\Desktop\Final.png")


#source = "C:\\Users\\K017-Labor\\Desktop\\Final.png"
#new_file_name = "image_" + str(counter) + ".png"
#destination = "C:\\Users\\K017-Labor\\Desktop\\SetupFolder\\SavedPics\\" + new_file_name

# Copies the finished picture on desktop for printing
#shutil.copy2(source, destination)

os.system("echo Your picture is ready to print now!")

# does not work due to printer resetting print settings every single time >:]
#os.system(r"print C:\Users\K017-Labor\Desktop\SetupFolder\Edited_Pics\A.png")
