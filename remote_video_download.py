import requests
 
file_url = 'https://www.learningcontainer.com/wp-content/uploads/2020/05/sample-mp4-file.mp4'
filename = file_url.split("/")[-1]
 
file_object = requests.get(file_url)
 
with open(filename, 'wb') as local_file:
    local_file.write(file_object.content)

print("Status code: "+str(file_object.status_code))
print(filename)
print(file_object.headers)
print('Success')

