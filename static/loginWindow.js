const ELEMENTS = {
	LOGIN_BUTTON: document.querySelector('#loginButton'),
	USERNAME_INPUT: document.querySelector('#usernameInput')
};

const loginEvent = new CustomEvent('login', {});

window.USER_SESSION = null;

getSession();

ELEMENTS.LOGIN_BUTTON.addEventListener('click', async event => {
	let username = ELEMENTS.USERNAME_INPUT.value;

	if(username.trim().length > 0) {
		const response = await window.Fetch('/login', {
			method: 'POST',
			body: new URLSearchParams(`username=${username}`)
		});

		await getSession();
	}
});

async function getSession() {
	const response = await window.Fetch('/get_session');

	if(response.user) {
		window.USER_SESSION = response.user;
		window.UI.switchWindows('app');

		document.dispatchEvent(loginEvent);
	} else {
		window.USER_SESSION = null;
		window.UI.switchWindows('login');
	}
}