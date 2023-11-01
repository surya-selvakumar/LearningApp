const login_toogle_btn = document.getElementById("login-toogle-btn");

const signup_toogle_btn = document.getElementById("signup-toogle-btn");

const signup_form = document.getElementById("signup-form");
const login_form = document.getElementById("login-form");

signup_form.style.display = "none";
login_toogle_btn.style.borderBottom = "3px solid #503E9D";



login_toogle_btn.addEventListener("click", () => {
  signup_form.style.display = "none";
  login_form.style.display = "flex";
  login_toogle_btn.style.borderBottom = "3px solid #503E9D";
  signup_toogle_btn.style.borderBottom = "2px solid black";
});

signup_toogle_btn.addEventListener("click", () => {
  login_form.style.display = "none";
  signup_form.style.display = "flex";
  signup_toogle_btn.style.borderBottom = "3px solid #503E9D";
  login_toogle_btn.style.borderBottom = "2px solid black";
});



// // Select the form and the input field  
// const form = document.getElementById("login-form");
// const login_email = document.getElementById("login-email");
// const logi_password = document.getElementById("login-password");




// console.log("sddsds");


// // Add an event listener to the form to handle form submission
// form.addEventListener("submit", function (event) {
//     event.preventDefault(); // Prevent the default form submission behavior
//     const login_data = {
//       email : login_email.value,
//       password : logi_password.value
//     }
//     console.log(login_data);
// });


// const login_btn = document.getElementById("login-btn");

// login_btn.addEventListener("click" , ()=>{
//   const email = document.getElementById("login-email").value;
//   const password = document.getElementById("login-password").value;
 

//   const formData = {
//       email: email,
//       password: password,
    
//   };

//   console.log(formData);
// })


// const signup_btn = document.getElementById("signup-btn");

// signup_btn.addEventListener("click" , ()=>{
//   const email = document.getElementById("signup-email").value;
//   const password = document.getElementById("signup-password").value;
//   const password2 = document.getElementById("signup-password2").value;

//   const formData = {
//       email: email,
//       password: password,
//       confirmPassword: password2,
    
//   };

//   console.log(formData);
// })





  
// document.addEventListener("DOMContentLoaded", function () {
//   const form = document.getElementById("login-form");

//   form.addEventListener("submit", function (event) {
//       event.preventDefault(); // Prevent the default form submission

//       const email = document.getElementById("login-email").value;
//       const password = document.getElementById("login-password").value;
      
    
//       const formData = {
//           email: email,
//           password: password,
        
//       };

//       console.log(formData);
//   });
// });
     

