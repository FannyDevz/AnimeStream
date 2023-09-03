# Run this for updating the anime.json
# change <end_num> for last pagination from gogoanime anime list page

import requests
import json
import time

url_template = "https://animoasa.glitch.me/animelist/{}"
start_num = 1
end_num = 91
animelist = []

try:
    for num in range(start_num, end_num + 1):
        url = url_template.format(num)
        print("Getting data for page", num)
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            animelist.extend(data)
        else:
            print(f"Failed to fetch data for page {num}. Status code: {response.status_code}")

    with open('anime.json', 'w') as f:
        json.dump(animelist, f)

    num_objects = len(animelist)

    print("Done! Saved as anime.json")
    print("Total Anime:", num_objects)
except Exception as e:
    print("An error occurred:", str(e))
finally:
    # Add a sleep to prevent the script from exiting immediately
    time.sleep(10)  # Sleep for 10 seconds (adjust as needed)
