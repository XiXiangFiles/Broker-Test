const mqtt = require('mqtt')
const uuid = require('uuid')
const options = { qos: 2 }
const opt = {
  protocolVersion: 5
}
const client = mqtt.connect('mqtt://127.0.0.1', opt)
const times = parseInt(process.env.TIMES)
let count = 0

const result = {
    flag: true
}

client.on('connect', function () {
  client.subscribe('publisher', options)
})



client.on('message', function (topic, message) {
  count++
  if (result.flag){
    result.start = Date.now()
    result.flag = false
  }
  result.end = Date.now()
})
setInterval(function(){
  if (result.end && (Date.now() - result.end > 1000)){
    result.count = count
    result.tps = (count / (result.end - result.start)) * 1000
    result.qos = (count / times) * 100
    console.log(JSON.stringify(result))
    process.exit()
  }
},1000)