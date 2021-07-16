for i in {1..15}
do
   ./scripts/start_publish.sh &
   ./scripts/subscriber.sh 
   sleep 1
done