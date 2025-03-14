import requests

# Define API endpoint
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&precision=0"

# API headers with key
headers = {
    "accept": "application/json",
    "x-cg-api-key": "CG-HsbXcp52odATVdAmsvJeS6qc"  # Replace with your actual key
}

try:
    # Send GET request
    response = requests.get(url, headers=headers, timeout=10)  # Timeout added for safety
    response.raise_for_status()  # Raise error if status code is not 2xx

    # Attempt to parse JSON
    data = response.json()

    # Check if expected data exists
    if "bitcoin" in data and "usd" in data["bitcoin"]:
        bitcoin_price = data["bitcoin"]["usd"]
        print(f"Bitcoin: ${bitcoin_price:,}")  # Comma formatting for thousands
    else:
        print("Error: Unexpected API response structure.")

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP Error: {http_err}")  # Handles 4xx and 5xx errors

except requests.exceptions.ConnectionError:
    print("Error: Unable to connect to CoinGecko API. Check your internet.")

except requests.exceptions.Timeout:
    print("Error: The request timed out. Try again later.")

except requests.exceptions.RequestException as req_err:
    print(f"API Request Error: {req_err}")  # Catches any other request-related errors

except ValueError:
    print("Error: Failed to parse JSON response.")
