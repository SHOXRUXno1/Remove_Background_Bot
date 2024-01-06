import requests

url = "https://background-removal.p.rapidapi.com/remove"

# payload = { "image_url": "https://objectcut.com/assets/img/raven.jpg" }
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "a034eee326msh391acfe23fba9fcp1bda1ejsnd0f64603a28d",
	"X-RapidAPI-Host": "background-removal.p.rapidapi.com"
}

# response = requests.post(url, data=payload, headers=headers)

# print(response.json())
async def remove_background(img_url):
	payload = f"image_url={img_url}"
	response = requests.request("POST", url, data=payload, headers=headers)
	return response.json()["response"]["image_url"]