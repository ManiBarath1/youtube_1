let menuIcon=document.querySelector('.menu-icon')
let sidebar=document.querySelector('.sidebar')
let container=document.querySelector('.container')

menuIcon.onclick=function(){
    sidebar.classList.toggle('small-sidebar')
    container.classList.toogle('large-container')
}
console.log(sidebar)