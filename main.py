import os
import httpx
import pandas as pd

response = httpx.get("https://jsonplaceholder.typicode.com/users")

if response.status_code == 200:
    users_data = response.json()
    df = pd.DataFrame(users_data)

    if not os.path.exists("users"):
        os.makedirs("users")

    for index, user in df.iterrows():
        username = user['username']
        user.to_csv(f"users/{username}.csv", index=False)
else:
    print("Failed to fetch data")
