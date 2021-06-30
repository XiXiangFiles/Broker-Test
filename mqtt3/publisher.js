const mqtt = require('mqtt')
const uuid = require('uuid')
const shajs = require('sha.js')
const opt = {
  protocolId: 'MQIsdp',
  protocolVersion: 3
}
const client = mqtt.connect('mqtt://mqtt-server', opt)
const options = { qos: 0 }
const times = parseInt(process.env.TIMES)
const result = {}
let numberMessage = 0

client.on('connect', function () {
  client.subscribe('publisher')
})
let amuntTimes = 0
async function send (topic, message, options) {
  client.publish(topic, message, options, function (err) {
    if (err) {
      console.log(err)
    } else {
      numberMessage++
    }
    amuntTimes++
  })
}
client.on('message', function (topic, message) {
  topic = topic.toString('utf8')
  message = message.toString('utf8')
  for (let i = 0; i < times; i++) {
    if (i === 0) {
      result.start = Date.now()
    }
    send('subscriber', shajs('sha512').update(uuid.v4().toString()).digest('hex'), options)
    if (i === times - 1) {
      send('subscriber', 'finish', options)
    }
  }
})
client.on('error', function (err) {
  console.log(err)
})
setInterval(() => {
  if (parseInt(amuntTimes) >= parseInt(times)) {
    result.end = Date.now()
    result.tps = (numberMessage / (result.end - result.start)) * 1000
    result.amountPkg = numberMessage
    console.log(result)
    process.exit()
  }
}, 1000)
