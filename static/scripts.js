let menu1 = document.querySelector("#menu-icon");
let navlist1 = document.querySelector(".navlist");
let header1 = document.querySelector("header");

window.addEventListener("scroll", () => {
  let value = window.scrollY;

  if (value > 870) {
    header1.style.background = "#93DFD5";
  } else {
    header1.style.background = "transparent";
  }
});

menu1.onclick = () => {
  menu1.classList.toggle("bx-x");
  navlist1.classList.toggle("open");
};