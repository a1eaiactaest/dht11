function FetchAPI(endpoint){
  const url = "http://localhost:1337"+endpoint;
  const error=false;
  const data=null;

  fetch(url)
    .then(res => res.json())
    .then((res) => {
      data = res;
    })
    .catch(error => {
      console.log("Couldn't fetch from " + url);
      error = true;
    })

  if (error){
    return null;
  } else{
    return data;
  }
}

export { FetchAPI };