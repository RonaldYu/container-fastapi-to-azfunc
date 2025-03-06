#%%
import requests

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

kv_client = SecretClient(
    vault_url = f"https://pru-ai-pil-test-kv.vault.azure.net",
    credential = DefaultAzureCredential()
)


FUNCTION_KEY = kv_client.get_secret("pru-aipil-test-dp-micsrv-funckey").value


headers = {
    'x-functions-key': FUNCTION_KEY
}

ls_urls = [
    'https://data-pipeline-microservice.azurewebsites.net/task1/',
    'https://data-pipeline-microservice.azurewebsites.net/task1/items/5',
    'https://data-pipeline-microservice.azurewebsites.net/task2/',
    'https://data-pipeline-microservice.azurewebsites.net/task2/items/5',
]

for url in ls_urls:
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print('Success:', response.json())
    else:
        print('Failed:', response.status_code)
        print(response.content)
#%%
import requests

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

kv_client = SecretClient(
    vault_url = f"https://pru-ai-pil-test-kv.vault.azure.net",
    credential = DefaultAzureCredential()
)


FUNCTION_KEY = kv_client.get_secret("pru-aipil-test-dp-tasks-funckey").value


headers = {
    'x-functions-key': FUNCTION_KEY
}

ls_urls = [
    'https://data-pipeline-tasks.azurewebsites.net/task1/',
    'https://data-pipeline-tasks.azurewebsites.net/task1/items/5',
    'https://data-pipeline-tasks.azurewebsites.net/task2/',
    'https://data-pipeline-tasks.azurewebsites.net/task2/items/5',
]

for url in ls_urls:
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print('Success:', response.json())
    else:
        print('Failed:', response.status_code)
        print(response.content)
# %%
