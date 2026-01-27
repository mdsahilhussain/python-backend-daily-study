import requests

def fetch_random_users():
    url ='https://api.freeapi.app/api/v1/public/randomusers/user/random'
    response = requests.get(url)
    users = response.json()
    if users['success'] and 'data' in users:
        username = users['data']['login']['username']
        country = users['data']['location']['country']
        return username, country
    else:
        raise Exception("Failed to fetch user data")


def main():
    try:
        username, country = fetch_random_users()
        print(f"Username: {username}, \nCountry: {country}")
    except Exception as e:
        print(f"Error: {e}")
    

if __name__ == "__main__":
    main()
