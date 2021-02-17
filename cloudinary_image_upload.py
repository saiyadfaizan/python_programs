import cloudinary
import cloudinary.uploader
import cloudinary.api
import requests

cloudinary.config( 
  cloud_name = "saiyadfaizan", 
  api_key = "358128463149668", 
  api_secret = "9vLFVeETw4WlfKhqbqbhaeBlfeQ" 
)


#Successful= cloudinary.api.create_folder("product/test2")
#print(Successful)

response = cloudinary.uploader.upload('https://homepages.cae.wisc.edu/~ece533/images/airplane.png', folder = "shivam/", public_id = "airplane")

#result = cloudinary.uploader.add_tag('fly', ['airplane'])

print(response)
public_id=response['public_id']
print(public_id)



link = cloudinary.utils.cloudinary_url(public_id)
print(link)

print('@'*100)
asset_id=response['asset_id']
version_id=response['version_id']

#url = cloudinary.utils.download_backedup_asset(asset_id, version_id)
url = cloudinary.utils.download_zip_url(public_id)
print(url)




 
