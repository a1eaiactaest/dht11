function fetchAPI(endpoint) {
	const url = "http://localhost:1337" + endpoint;

	fetch(url)
		.then((res) => res.json())
		.then((res) => {
			return res;
		})
		.catch((error) => {
			console.log("Couldn't fetch from " + url, error);
		});
}

export { fetchAPI };
