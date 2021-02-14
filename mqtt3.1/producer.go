package main

import (
	"fmt"
	"math/rand"

	mqtt "github.com/eclipse/paho.mqtt.golang"
)

func randomString(l int) string {
	bytes := make([]byte, l)
	for i := 0; i < l; i++ {
		bytes[i] = byte(randInt(65, 90))
	}
	return string(bytes)
}

func randInt(min int, max int) int {
	return min + rand.Intn(max-min)
}
func main() {
	ops := mqtt.NewClientOptions().SetClientID(randomString(16)).AddBroker("tcp://mqtt:1883")
	client := mqtt.NewClient(ops)
	if token := client.Connect(); token.Wait() && token.Error() != nil {
		panic(token.Error())
	}
	if token := client.Publish("test/topic", 0, false, "Example Payload"); token.Wait() && token.Error() != nil {
		panic(token.Error())
	}
	fmt.Println("send msg")
}
