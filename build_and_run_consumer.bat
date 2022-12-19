docker build -t codvl/consumer -f CI/consumer.Dockerfile .
docker run  --name consumer --net elastic -it codvl/consumer:latest