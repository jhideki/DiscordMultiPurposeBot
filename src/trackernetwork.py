import requests

def getApexStats(username):
    url = f"https://public-api.tracker.gg/v2/apex/standard/profile/origin/{username}"
    headers = {
        "TRN-Api-Key": "be4918dc-7331-4a1a-8fd2-6c39fd067785",
        "Accept": "application/json",
        "Accept-Encoding": "gzip"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error: {response.status_code}")

def getFortStats(username):
    url = f"https://api.fortnitetracker.com/v1/powerrankings/pc/NAW/{username}"
    headers = {
        "TRN-Api-Key": "be4918dc-7331-4a1a-8fd2-6c39fd067785",
        "Accept": "application/json",
        "Accept-Encoding": "gzip"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error: {response.status_code}")