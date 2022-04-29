function extractDictItems(dict, key){
  let ret = [];
  dict.forEach(subdict => {
    for (const [k,v] of Object.entries(subdict)){
      if (k ===key){
        ret.push(v);
      }
    }
  });
  return ret;
}

function extractAirTemp(dict){
  let ret = [];
  dict.forEach(subdict => {
    for (const [k,v] of Object.entries(subdict)){
      if (k === "air_temp"){
        ret.push(v.air_temp);
      }
    }
  });
  return ret;
}
export { extractDictItems, extractAirTemp };