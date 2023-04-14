import requests

# First, get the user's own IP address
ip_response = requests.get('https://api.ipify.org?format=json')
ip_address = ip_response.json()['ip']

# Next, make a request to the ipstack.com API with the user's IP address
API_KEY = 'YOUR_API_KEY' 
url = f'http://api.ipstack.com/{ip_address}?access_key={API_KEY}'
response = requests.get(url)
data = response.json()

# Extract the relevant information from the response
ip = data['ip']
continent = data['continent_name']
country = data['country_name']
region = data['region_name']
city = data['city']

# Print the information to the user
print(f'IP Address: {ip}')
print(f'Location: {continent}, {country}, {region}, {city}')