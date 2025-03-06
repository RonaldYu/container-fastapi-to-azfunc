import azure.functions as func
import datetime
import json
import logging
from fastapi_task1 import app as fast_app_1
from fastapi_task2 import app as fast_app_2
app = func.FunctionApp()

@app.function_name("Micro-Task1")
@app.route(route="task1/{*route}", auth_level=func.AuthLevel.ANONYMOUS)
async def backend_api(req: func.HttpRequest) -> func.HttpResponse:
    return await func.AsgiMiddleware(fast_app_1).handle_async(req)



@app.function_name("Micro-Task2")
@app.route(route="task2/{*route}", auth_level=func.AuthLevel.ANONYMOUS)
async def backend_api(req: func.HttpRequest) -> func.HttpResponse:
    return await func.AsgiMiddleware(fast_app_2).handle_async(req)


@app.route(route="HttpOcrFunc", auth_level=func.AuthLevel.ANONYMOUS)
def HttpOcrFunc(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )