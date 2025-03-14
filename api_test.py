import requests

# Define the API endpoint
url = "https://jsonplaceholder.typicode.com/todos/1"

try:
	# Send GET request
	response = requests.get(url)
	response.raise_for_status() # Raise an error for bad status codes (4xx, 5xx)

	# Parse JSON response
	data  = response.json()

	# Print formatted JSON response
	print("Response Data:")
	print(f"ID: {data['id']}")
	print(f"Title: {data['title']}")
	print(f"Completed: {data['completed']}")

except requests.exceptions.RequestExceptions as e:
	print(f"Error: {e}")
