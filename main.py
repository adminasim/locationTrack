import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import folium

# Replace with your actual API Key
API_KEY = "your_api_key"

# Get phone number input
number = input("Please enter your phone number with country code (e.g., +1234567890): ")

# Parse phone number
try:
    new_number = phonenumbers.parse(number)
    
    # Get location
    location = geocoder.description_for_number(new_number, "en")
    print(f"Location: {location}")

    # Get carrier name
    service_name = carrier.name_for_number(new_number, "en")
    print(f"Carrier: {service_name}")

    # Initialize OpenCage Geocoder
    oc_geocoder = OpenCageGeocode(API_KEY)
    
    # Get coordinates
    result = oc_geocoder.geocode(location)
    
    if result and len(result) > 0:
        lat = result[0]['geometry']['lat']
        lng = result[0]['geometry']['lng']
        print(f"Coordinates: {lat}, {lng}")

        # Create map
        my_map = folium.Map(location=[lat, lng], zoom_start=9)
        folium.Marker([lat, lng], popup=location).add_to(my_map)

        # Save map
        my_map.save("location.html")
        print("Location tracking completed. Open 'location.html' to view the map.")

    else:
        print("Could not find location coordinates.")

except Exception as e:
    print(f"Error: {e}")
