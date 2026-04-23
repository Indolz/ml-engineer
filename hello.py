import requests
response = requests.get("https://api.github.com/users/Indolz")
data = response.json()

print(f"GitHub user: {data['login']}")
print(f"Public repos: {data['public_repos']}")
print(f"Account created: {data['created_at'][:10]}")