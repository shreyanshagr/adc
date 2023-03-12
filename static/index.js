console.log("Check");

// switches to SignUP Page
let signUpPg=document.getElementById("signup-page");
let loginInPg=document.getElementById("login-page");
let signUpbtn=document.getElementById("SPbtn");
signUpbtn.addEventListener("click",function(){
    passwordSuggest();
    loginInPg.classList.add("hide");
    signUpPg.classList.remove("hide");
});


// switches to Login Page
let loginbtn=document.getElementById("login_btn");
loginbtn.addEventListener("click",function(){
    checkingPassword();
    loginInPg.classList.remove("hide");
    signUpPg.classList.add("hide");
});

// Checking login Page
function checkingPassword(){
    bar.classList.remove("invalid");
    msg.style.display="none";
}
let loginPassword=document.getElementById("login_password");
let bar=document.getElementById("login_password_box");
let msg=document.getElementById("invalid-msg");
loginPassword.addEventListener("click",checkingPassword);
loginPassword.addEventListener("blur",()=>{
    let pss=loginPassword.value;
    if(pss.length<8){
        bar.classList.add("invalid");
        msg.style.display="inline-block";
    }

});

// Checking SignUP Page
function passwordSuggest(){
    signupPasswordBar.classList.remove("invalid");
        passwordSugg.style.display="none";
        signupInvalid.style.display="none";
}
let signupPassword=document.getElementById("password");
let signupPasswordBar=document.getElementById("signup_password_box");
let passwordSugg=document.getElementById("password_suggestion");
let signupInvalid=document.getElementById("signup-invalid");

signupPassword.addEventListener("click",passwordSuggest);

signupPassword.addEventListener("blur",function(){
    let regex=/(?=.*[~!@#$%&])(?=.*[a-zA-Z])(?=.*[0-9])[a-zA-Z0-9!@#$%]{8,}/gm;
    if(!regex.test(signupPassword.value)){
        signupPasswordBar.classList.add("invalid");
        passwordSugg.style.display="block";
        signupInvalid.style.display="inline-block";
    }
});

// confirm Password check
let confirmPassword=document.getElementById("confirm_password");
let confirmPasswordBar=document.getElementById("confirm_password_box");
let errmsg=document.getElementById("err_msg");

function confirmPasswordError(){
    confirmPasswordBar.classList.remove("invalid");
    errmsg.style.display="none";
}
confirmPassword.addEventListener("click",confirmPasswordError);
confirmPassword.addEventListener("blur",function(){
    let pass=document.getElementById("password");
    if(pass.value !== confirmPassword.value){
        confirmPasswordBar.classList.add("invalid");
        errmsg.style.display="inline-block";
    }
    else{
        confirmPasswordBar.classList.remove("invalid");
        errmsg.style.display="none";
    }
});

let remover=document.querySelectorAll(".effect-remover");
remover.forEach((e,i)=>{
    e.addEventListener("click",function(){
        let PH=e.placeholder;
        remover[i].placeholder="";
        console.log(remover[i].placeholder);
        e.addEventListener("blur",function(){
            e.placeholder=PH;
        });
    })
})