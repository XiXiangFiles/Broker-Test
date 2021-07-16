rm -rf scripts/publisher.sh
echo "mosquitto_pub -h 127.0.0.1 -t publisher -V 31 -q 2 -l <<!" >> scripts/publisher.sh
for i in {1..70000}
do
   echo 6381864e-4e50-4b82-8950-95f0a4e1045b9080e9b5-a3b3-4bc5-8aef-3524a79f0bf72d831555-e34b-4dc3-9992-c8727eefc1bba260bf5e-fb9a-4262-a8fe-72cd5649df8b6e282de1-6aee-4eed-805d-efa085ec6e49272f2448-32ba-41c5-9128-fc407d4457a1 >> scripts/publisher.sh
done
chmod +x scripts/publisher.sh