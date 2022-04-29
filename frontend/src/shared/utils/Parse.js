function parseEpoch(epoch){
  let date = new Date(epoch*1000)
  let year = date.getFullYear()
  let month = date.getMonth()
  let day = date.getDate()
  let hour = date.getHours()
  let minutes = date.getMinutes()
  let seconds = date.getSeconds()

  let time = `${year}-${month}-${day} ${hour}:${minutes}:${seconds.length == 1 ? seconds : "0"+seconds}`
  return time
}

export { parseEpoch };