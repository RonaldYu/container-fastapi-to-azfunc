@echo off
docker build -t pru-aipil-data-pipeline-tasks:latest .
if %errorlevel% neq 0 exit /b %errorlevel%

docker tag pru-aipil-data-pipeline-tasks:latest pruaipiltestcntrgy.azurecr.io/pru-aipil-data-pipeline-tasks:v0
if %errorlevel% neq 0 exit /b %errorlevel%

docker push pruaipiltestcntrgy.azurecr.io/pru-aipil-data-pipeline-tasks:v0
if %errorlevel% neq 0 exit /b %errorlevel%

docker tag pru-aipil-data-pipeline-tasks:latest pruaipiltestcntrgy.azurecr.io/pru-aipil-data-pipeline-tasks:latest
if %errorlevel% neq 0 exit /b %errorlevel%

docker push pruaipiltestcntrgy.azurecr.io/pru-aipil-data-pipeline-tasks:latest
if %errorlevel% neq 0 exit /b %errorlevel%
