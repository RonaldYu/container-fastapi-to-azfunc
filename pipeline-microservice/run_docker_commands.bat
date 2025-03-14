@echo off
docker build -t pru-aipil-data-pipeline-microservice:latest .
if %errorlevel% neq 0 exit /b %errorlevel%

docker tag pru-aipil-data-pipeline-microservice:latest rycntrgy.azurecr.io/pru-aipil-data-pipeline-microservice:v0
if %errorlevel% neq 0 exit /b %errorlevel%

docker push rycntrgy.azurecr.io/pru-aipil-data-pipeline-microservice:v0
if %errorlevel% neq 0 exit /b %errorlevel%

docker tag pru-aipil-data-pipeline-microservice:latest rycntrgy.azurecr.io/pru-aipil-data-pipeline-microservice:latest
if %errorlevel% neq 0 exit /b %errorlevel%

docker push rycntrgy.azurecr.io/pru-aipil-data-pipeline-microservice:latest
if %errorlevel% neq 0 exit /b %errorlevel%


@REM docker run --rm -it --expose=80 -e PORT=80 pru-aipil-data-pipeline-microservice:latest
@REM docker run --rm -p 80:80 -it pru-aipil-data-pipeline-microservice:latest
@REM docker run --rm -it mcr.microsoft.com/azure-cli:latest