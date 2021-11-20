export function are_equal(a,b){
  /* 

  Takes two arrays as parameters (a,b).
  Returns true only if arrays are exactly the same.

  a = [1, 2, 3]
  b = [1, 2, 3]
  console.log(areEqual(a,b));

    true

  a = ["1", 2, 3]
  b = [1, 2, 3]
  console.log(areEqual(a,b));
    
    false

  */
  return Array.isArray(a) &&
    Array.isArray(a) && 
    a.length === b.length &&
    a.every((val, index) => val === b[index]);
}

export function parse_unix_time(unix_seconds){
  /*

  Takes unix seconds as parameter and returns formatted date:
 
      YYYY-MM-DD HH:mm:SS 

  */

  var date = new Date(unix_seconds * 1000);
  var year = date.getFullYear();
  var month = date.getMonth();
  var day = date.getDate();
  var hour = date.getHours();
  var minutes = "0" + date.getMinutes();
  var seconds = "0" + date.getSeconds();
  var formatted_time = year + "-" + month + "-" + day + " " + hour + ":" + minutes.substr(-2) + ":" + seconds.substr(-2);

  return formatted_time
}
