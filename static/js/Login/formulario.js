$(document).ready(function(){
	//Avatar
	const avatar = document.getElementById("avatarIcon");
	const loginSignup = document.getElementById("loginSignupMenu");

	avatar.addEventListener('mouseover', () => { loginSignup.style.display = 'flex' })
	avatar.addEventListener('mouseleave', () => { loginSignup.style.display = 'none' })
})

function validate() {
	let email = document.getElementById("correo").value
	let password = document.getElementById("pass").value

	if(email == 'admin@gmail.com' && password == 'admin'){
		// window.location.replace("/templates/Dashboard/dashboardOne.html")
		window.open("/templates/Dashboard/dashboardOne.html")
	}else{
		alert("Usuario inválido")
	}
}







