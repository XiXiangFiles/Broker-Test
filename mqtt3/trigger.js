const mqtt = require('mqtt')
const opt = {
  protocolId: 'MQIsdp',
  protocolVersion: 3
}
const client = mqtt.connect('mqtt://127.0.0.1', opt)
client.on('connect', function () {
  client.publish('publisher', 'start')
  client.end()
})
