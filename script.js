document.getElementById('loginForm').addEventListener('submit',function(e){
e.preventDefault();
const u=document.getElementById('username').value.trim();
const p=document.getElementById('password').value.trim();
const m=document.getElementById('message');
if(!u||!p){m.style.color='red';m.innerHTML='Please fill in all fields.';return;}
if(u==='admin'&&p==='password123'){
m.style.color='green';
m.innerHTML='Login Successful!';
}else{
m.style.color='red';
m.innerHTML='Invalid Username or Password.';
}
});