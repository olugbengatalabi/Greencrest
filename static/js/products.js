// /*=============== SHOW MENU ===============*/
// const catMenu = document.getElementById('categories-menu'),
//       catToggle = document.getElementById('categories-toggle'),
//       catClose = document.getElementById('categories-close')

// /*===== MENU SHOW =====*/
// /* Validate if constant exists */
// if(catToggle){
//   catToggle.addEventListener('click', () =>{
//       catMenu.classList.add('show-menu')
//     })
// }

// /*===== MENU HIDDEN =====*/
// /* Validate if constant exists */
// if(catClose){
//     navClose.addEventListener('click', () =>{
//       catMenu.classList.remove('show-menu')
//     })
// }

// /*=============== REMOVE MENU MOBILE ===============*/
// const navLink = document.querySelectorAll('.nav__link')

// function linkAction(){
//     const catMenu = document.getElementById('nav-menu')
//     // When we click on each nav__link, we remove the show-menu class
//     catMenu.classList.remove('show-menu')
// }
// navLink.forEach(n => n.addEventListener('click', linkAction))

// document.getElementById("search").size = "50";


const clearIcon = document.querySelector(".clear-icon");
const searchBar = document.querySelector(".search");

searchBar.addEventListener("keyup", () => {
  if(searchBar.value && clearIcon.style.visibility != "visible"){
    clearIcon.style.visibility = "visible";
  } else if(!searchBar.value) {
    clearIcon.style.visibility = "hidden";
  }
});

clearIcon.addEventListener("click", () => {
  searchBar.value = "";
  clearIcon.style.visibility = "hidden";
})
