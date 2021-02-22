import dropbox
dbx = dropbox.Dropbox('6Tx58pC9uPAAAAAAAAAAAUgacV78wWD6407ryrC23hwPKQeASqFYjiWhYsJSKpHE')

#url = 'http://www.africau.edu/images/default/sample.pdf'
url = 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3'
#url = 'https://homepages.cae.wisc.edu/~ece533/images/airplane.png'
filename = url.split("/")[-1]
print(filename)

path = '/test/new/{}'.format(filename)

response= dbx.files_save_url(path, url)

print(response)
print(dropbox.files.SaveUrlResult)


link = dbx.sharing_create_shared_link(path, short_url=False, pending_upload=None)
print("This is link")
print(link)

#responsee= dbx.files_get_preview_to_file(url, path, rev=None)
#print(responsee)
