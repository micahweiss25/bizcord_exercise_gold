window.getAvatarURL = num => `https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava${(num % 5) + 1}-bg.webp`;

window.Fetch = async function Fetch(...args) {
	let err = null;
	const response = await fetch(...args).then(r => r.json()).catch(e => {
		err = e;
		return null;
	});

	if(!response) {
		console.error(err);
		throw new Error(`Failed to access ${args[0]} route.`);
		return;
	}

	if(response.error) {
		return alert('Error: ' + response.error);
	}

	return response;
}