import requests
import json

# ---------------------
API_KEY = "eU0q1YYy9TF_PtpCJPXZ8A"
TARGET_USERNAME = "roses_are_rosie"
# ---------------------

BASE_URL = "https://v1.rocketapi.io/instagram/user"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Token {API_KEY}"
}

def get_user_id(username):
    """step 1: get the numeric User ID from the username."""
    url = f"{BASE_URL}/get_web_profile_info"
    payload = {"username": username}
    
    print(f"1. Fetching profile for: {username}...")
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        # navigate the JSON response to find the ID
        # response -> body -> data -> user -> id
        user_data = data.get("response", {}).get("body", {}).get("data", {}).get("user", {})
        user_id = user_data.get("id")
        
        if user_id:
            print(f"   success! found User ID: {user_id}")
            return user_id
        else:
            print("   error: could not find User ID in the response.")
            print("   debug Response:", json.dumps(data, indent=2))
            return None

    except requests.exceptions.RequestException as e:
        print(f"   Network/API Error: {e}")
        return None

def get_similar_accounts(user_id):
    """step 2: get similar accounts using the numeric User ID."""
    url = f"{BASE_URL}/get_similar_accounts"
    payload = {"id": int(user_id)} # Ensure ID is an integer
    
    print(f"\n2. Fetching similar accounts for ID: {user_id}...")
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        # navigate the JSON to find the list of similar users
        # response -> body -> data -> user -> edge_related_profiles
        return data

    except requests.exceptions.RequestException as e:
        print(f"   Network/API Error: {e}")
        return None

# --- MAIN EXECUTION FLOW ---
if __name__ == "__main__":
    # step 1: get the ID
    target_id = get_user_id(TARGET_USERNAME)
    
    # step 2: if we got an ID, get the similar accounts
    if target_id:
        similar_accounts_data = get_similar_accounts(target_id)
        
        if similar_accounts_data:
            print("\n--- RESULTS ---")
            # print the raw JSON or a summary
            # dump it to a string so it's readable in the console
            print(json.dumps(similar_accounts_data, indent=2))
        else:
            print("failed to retrieve similar accounts.")
    else:
        print("stopping because User ID could not be found.")
