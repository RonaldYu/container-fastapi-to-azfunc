import azure.functions as func
import datetime
import json
import logging
from fastapi_task1 import app as fast_app_1
from fastapi_task2 import app as fast_app_2
app = func.FunctionApp()

@app.function_name("Pipeline-Task1")
@app.route(route="task1/{*route}", auth_level=func.AuthLevel.FUNCTION)
async def backend_api(req: func.HttpRequest) -> func.HttpResponse:
    return await func.AsgiMiddleware(fast_app_1).handle_async(req)



@app.function_name("Pipeline-Task2")
@app.route(route="task2/{*route}", auth_level=func.AuthLevel.FUNCTION)
async def backend_api(req: func.HttpRequest) -> func.HttpResponse:
    return await func.AsgiMiddleware(fast_app_2).handle_async(req)