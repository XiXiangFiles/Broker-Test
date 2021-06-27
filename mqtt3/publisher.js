const mqtt = require('mqtt')
const uuid = require('uuid')
const shajs = require('sha.js')
const opt = {
  protocolId: 'MQIsdp',
  protocolVersion: 3
}
const client = mqtt.connect('mqtt://mqtt-server', opt)
const options = { qos: 2 }
const promise1 = new Promise((resolve, reject) => {
  client.on('connect', function () {
    client.subscribe('publisher', function (err) {
      if (err) {
        console.error(err)
      }
    })
  })
  client.on('message', function (topic, message) {
    topic = topic.toString('utf8')
    message = message.toString('utf8')
    resolve(message)
  })
})

promise1.then((value) => {
  console.log(value)
  const promise2 = new Promise((resolve, reject) => {
    for (let i = 0; i < parseInt(process.env.TIMES); i++) {
      client.publish('subscriber', shajs('sha512').update(uuid.v4().toString()).digest('hex'), options)
      if (i === parseInt(process.env.TIMES) - 1) {
        client.publish('subscriber', 'finish', options)
        console.log('done')
        resolve()
      }
    }
  })
  promise2.then(function (val) {})
})

client.on('error', function (err) {
  console.log(err)
})
