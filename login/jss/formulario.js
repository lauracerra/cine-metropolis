$(document).ready(function(){

	//Avatar
	const avatar = document.getElementById("avatarIcon");
	const loginSignup = document.getElementById("loginSignupMenu");

	avatar.addEventListener('mouseover', () => { loginSignup.style.display = 'block' })
	avatar.addEventListener('mouseleave', () => { loginSignup.style.display = 'none' })

})
