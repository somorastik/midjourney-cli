import requests
#https://api.imgbb.com
def post_to_api(api_key, image):
    url = "https://api.imgbb.com/1/upload"
    parameters = {
        "expiration": 600,
        "key": api_key
    }
    files = {
        "image": image
    }
    response = requests.post(url, data=parameters, files=files)
    if response.status_code == 200:
        return response.json()
    else:
        return None

api_key = "api key here"
image = "R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"

result = post_to_api(api_key, image)
if result:
    print(result)
else:
    print("Request failed")
