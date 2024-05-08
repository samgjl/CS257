import psycopg2 
import requests

#+ Database Functions +#
def getConnection() -> tuple[psycopg2.extensions.connection, psycopg2.extensions.cursor]:
    conn = psycopg2.connect(
        host = "localhost",
        port = 5432,
        database = "johnsonlacosss",
        user = "johnsonlacosss",
        password = "puppy288market"
    )
    if not conn:
        print("Oops, we don't have a connection!")
        exit(1)
        
    cur = conn.cursor()
    return conn, cur

def getKey() -> str:
    # I'm not 100% sure if we can share this, so let's keep this repo private:
    id = '52e9d591fd4e4733943394658da9dcf9'
    sec = '8e42f010bb154d2895b5954f38fee59d'
    # Request our key:
    auth = requests.post(
        "https://accounts.spotify.com/api/token",
        headers = {"Content-Type": "application/x-www-form-urlencoded"},
        data = { "grant_type": "client_credentials",
                 "client_id": id,
                 "client_secret": sec }
        ).json()
    # Ensure we got a proper response:
    if 'access_token' not in auth:
        print("Oops, we didn't get a key!")
        return None
    
    return auth['access_token']


if __name__ == "__main__":
    print("---\nAttempting to get connection...")
    key = getKey()
    print("key", key)
    print("Connection established!\n---" if key else "Connection failed!\n---")