import requests
# Make a GET request to fetch posts from JSONPlaceholder
response = requests.get("https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc")
# Check if the request was successful
if response.status_code == 200:
    posts = response.json()
    # Display the titles of the first 5 posts
    for post in posts[:5]: 
        print(f"post Title: {title}\n") 
else: 
    print("Failed to fetch data")


    # wrong
