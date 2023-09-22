const wrapper =document.querySelector('.wrapper');
const signupLink=document.querySelector('.signup-link');
const signinLink=document.querySelector('.signin-link');

signupLink.addEventListener('click',()=>{
    wrapper.classList.add('animate-signIn');
    wrapper.classList.remove('animate-signUp');
});
signinLink.addEventListener('click',()=>{
    wrapper.classList.add('animate-signUp');
    wrapper.classList.remove('animate-signIn');
});