import dropbox

dbx = dropbox.Dropbox('JJj8AtXc4EkAAAAAAAAAAcHXf1sunymAJbolm3Shqzm1-LvGkgSBWLL3pV6qKfwg')
#folder creation

dropboxBaseDir = '/sample8'
#dropboxNewSubDir = '/new'

res = dbx.files_create_folder_v2(dropboxBaseDir) 
print(res)


#local file upload
file_from = 'airplane.png'  

file_to = '/test/new/airplane.png' 
    
def upload_file(file_from, file_to):
    dbx = dropbox.Dropbox('JJj8AtXc4EkAAAAAAAAAAcHXf1sunymAJbolm3Shqzm1-LvGkgSBWLL3pV6qKfwg')
    f = open(file_from, 'rb')
    dbx.files_upload(f.read(), file_to)

response= upload_file(file_from,file_to)
print(response)

