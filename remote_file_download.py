import cloudinary
import cloudinary.uploader
import cloudinary.api
import requests

cloudinary.config( 
  cloud_name = "saiyadfaizan", 
  api_key = "358128463149668", 
  api_secret = "9vLFVeETw4WlfKhqbqbhaeBlfeQ" 
)

response = cloudinary.uploader.upload('https://homepages.cae.wisc.edu/~ece533/images/airplane.png', folder = "shivam/", public_id = "airplane")

print(response)

url=response['url']
print(url)
 
 
file_object = requests.get(url)
filename = url.split("/")[-1]
 
with open(filename, 'wb') as local_file:
    local_file.write(file_object.content)

print('Success')
