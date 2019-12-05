import dropbox

import glob
import os

list_of_files = glob.glob('/home/avishek/Documents/pre/dropboxupload/project/*') # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)
folder, filename = os.path.split(latest_file)
print(latest_file)



f= open(filename)
dbx = dropbox.Dropbox('Your App Key Here')
with open(str(folder)+"/"+ str(filename), "rb") as f:
    print("UPLOADING FILE "+ str(filename))
    dbx.files_upload(f.read(), '/'+str(filename), mute = True)
    print("UPLOAD DONE")

f.close()



# f= open("demo.txt")
# dbx = dropbox.Dropbox('Your App Key Here')
# with open("/home/avishek/Documents/pre/dropboxupload/project/dem.txt", "rb") as f:
#     dbx.files_upload(f.read(), '/dem.txt', mute = True)
#     print("UPLOAD DONE")

# f.close()

