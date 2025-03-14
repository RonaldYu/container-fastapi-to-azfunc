#%%
import requests
#%%
response = requests.get(
    f"https://ry-funcapp.azurewebsites.net/api/task1/items/{1}",
    headers={"x-functions-key": ""},
)

print(response.status_code, response.content)

# %%
