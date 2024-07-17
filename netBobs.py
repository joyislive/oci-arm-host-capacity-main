# pyinstaller --onefile  netBobs.py
import requests
import time
from datetime import datetime

def make_requests(url, delay=35):
    while True:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        try:
            response = requests.get(url)
            print(f"[{current_time}] Status Code: {response.status_code}")
            print(f"[{current_time}] Response Content: {response.text[:100]}")  # Print the first 100 characters of the response content
        except requests.exceptions.RequestException as e:
            print(f"[{current_time}] An error occurred: {e}")
        
        # Wait for the specified delay before making the next request
        time.sleep(delay)

if __name__ == "__main__":
    url = "http://localhost/oci-arm-host-capacity-main/"  # Replace with the URL you want to request
    make_requests(url)