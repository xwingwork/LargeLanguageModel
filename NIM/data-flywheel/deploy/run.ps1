$workPath = split-path -Parent $MyInvocation.MyCommand.Definition

# Get-Content -Path "$workPath\.key" | docker login -u '$oauthtoken' nvcr.io --password-stdin


docker compose -f $workPath\docker-compose.yaml down 
docker compose -f $workPath\docker-compose.yaml up -d --build --no-attach mongodb