import geocoder

# Get location based on IP
g = geocoder.ip('me')  # 'me' refers to your own IP address
print(f"IP Address: {g.ip}")
print(f"City: {g.city}")
print(f"Region: {g.state}")
print(f"Country: {g.country}")
print(f"Latitude: {g.latlng[0]}")
print(f"Longitude: {g.latlng[1]}")