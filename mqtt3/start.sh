export PUBLISHER_NUM=1
export TIMES=100000
docker rm -f $(docker ps -a -q)
docker-compose up -d