from fastapi import APIRouter
from fastapi.responses import JSONResponse
import requests
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
kv_client = SecretClient(
    vault_url = f"https://pru-ai-pil-test-kv.vault.azure.net",
    credential = DefaultAzureCredential()
)


FUNCTION_KEY = kv_client.get_secret("pru-aipil-test-dp-micsrv-funckey").value

router = APIRouter()

@router.get("/items/{item_id}")
async def read_item(item_id: int):
    response = requests.get(
        f'https://data-pipeline-microservice.azurewebsites.net/task2/items/{item_id}',
        headers={
            'x-functions-key': FUNCTION_KEY
        }
    )
    res = None
    if response.status_code == 200:
        res = response.json()
    else:
        res = str(response.content)
    return JSONResponse(content={"item_id": f"task-2-{str(item_id)}", 'microservice': res})

