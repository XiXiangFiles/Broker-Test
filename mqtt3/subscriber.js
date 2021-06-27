const mqtt = require('mqtt')
const fs = require('fs')
const opt = {
  protocolId: 'MQIsdp',
  protocolVersion: 3
}

let finish = 0
let numberMessage = 0
const filename = process.env.FILENAME
const res = {}
let isStart = false
let tmp = 0
let percent = 0
let i = 0

const client = mqtt.connect('mqtt://mqtt-server', opt)
client.on('connect', function () {
  client.subscribe('subscriber', function (err) {
    if (err) {
      console.error(err)
    }
  })
})
try {
  fs.mkdirSync(`result/${process.env.PUBLISHER_NUM}`)
} catch (err) {}

client.on('message', function (topic, message) {
  topic = topic.toString('utf8')
  message = message.toString('utf8')
  if (!isStart) {
    isStart = true
    res.start = Date.now()
  }
  console.log(message)
  percent = (++i / parseInt(process.env.TIMES)).toFixed(2)
  if (tmp < percent) {
    tmp = percent
    console.log(`${tmp}%`)
  }
  numberMessage++
  if (message === 'finish') {
    finish++
  }
  if (finish === parseInt(process.env.PUBLISHER_NUM)) {
    res.end = Date.now()
    res.numbers = numberMessage
    fs.writeFileSync(`result/${process.env.PUBLISHER_NUM}/${filename}.txt`, `${JSON.stringify(res)}\n`)
    process.exit()
  }
})

client.on('error', function (err) {
  console.log(err)
  process.exit()
})
