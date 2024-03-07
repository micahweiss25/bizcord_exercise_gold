window.UI = {};

window.UI.switchWindows = (newWindow) => {
	const allWindows = document.querySelectorAll('.main-window');
	allWindows.forEach(e => e.hidden = true);

	if(newWindow === 'login') {
		document.querySelector('#loginWindow').hidden = false;
	} else if(newWindow === 'app') {
		document.querySelector('#appWindow').hidden = false;
	}
};