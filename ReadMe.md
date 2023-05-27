
# Auxilium GPT Fallback service

Service used as fallback version for OpenAI API when API goes out of nothing.
    Service was written for IT-Hacaton 2023 by AssertionBit (Mark Soroking).
    MIT License.

## Deploy

Application contains Docker-Compose which will be enough for launching 
    application as fallback service. For own purpose You may use Dockefile for
    building image and deploying to your clusters and Docker-Compose's.
    All steps are automated and You not required in special items beside that.

* `docker-compose -f Docker-Compose.yaml up -d`

Or

* `docker -f Dockerfile up -d`

