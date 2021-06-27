const mqtt = require('mqtt')
const uuid = require('uuid')
const shajs = require('sha.js')
const opt = {
  protocolId: 'MQIsdp',
  protocolVersion: 3
}
const client = mqtt.connect('mqtt://mqtt-server', opt)
const options = { qos: 2 }
const times = parseInt(process.env.TIMES)
client.on('connect', function () {
  client.subscribe('publisher')
})
function send (topic, message, options) {
  return new Promise(function (resolve, reject) {
    client.publish(topic, message, options, function (err) {
      if (err) {
        console.log(err)
      }
      resolve()
    })
  })
}
client.on('message', function (topic, message) {
  topic = topic.toString('utf8')
  message = message.toString('utf8')
  for (let i = 0; i < times; i++) {
    send('subscriber', shajs('sha512').update(uuid.v4().toString()).digest('hex'), options).then()
    if (i === times - 1) {
      send('subscriber', 'finish', options).then(function () {})
    }
  }
})
client.on('error', function (err) {
  console.log(err)
})
