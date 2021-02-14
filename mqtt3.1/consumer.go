package main

import (
	"fmt"
	"math/rand"
	"os"

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
	c := make(chan os.Signal, 1)
	ops := mqtt.NewClientOptions().AddBroker("tcp://mqtt:1883")
	client := mqtt.NewClient(ops)
	if token := client.Connect(); token.Wait() && token.Error() != nil {
		panic(token.Error())
	}
	client.Subscribe("test/topic", 1, func(client mqtt.Client, msg mqtt.Message) {
		fmt.Printf("* [%s] %s\n", msg.Topic(), string(msg.Payload()))
	})
	<-c
}
