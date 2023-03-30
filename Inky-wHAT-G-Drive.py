from inky.auto import auto
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from PIL import Image
from time import sleep

board = auto()
inkyphat.set_border(black)

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

ids = []

folder_id = 'Your_Google_Drive_Folder_ID'
# Specifies the folder within the drive
lister = drive.ListFile({'q': "'%s' in parents" % folder_id}).GetList()
for item in lister:
    file = drive.CreateFile({'id': item['id']})
    file.GetContentFile(item['id'] + ".jpg")
    Image.open(item['id'] + ".jpg").convert("L").save(item['id'] + ".jpg")
    ids.append(item['id'] + ".jpg")
    # Renames and converts images in the folder to a greyscale jpg and adds them to the list

While True
    for x in range (0, len(ids))
        inkyphat.set_image(ids[x])
        inkyphat.show()
        sleep(1800)
        # Loop through and display every edited image in the list in 30 minute intervals
