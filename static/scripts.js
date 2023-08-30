let menu = document.querySelector("#menu-icon");
let navlist = document.querySelector(".navlist");
let header = document.querySelector("header");

window.addEventListener("scroll", () => {
  let value = window.scrollY;

  if (value > 870) {
    header.style.background = "#93DFD5";
  } else {
    header.style.background = "transparent";
  }
});

menu.onclick = () => {
  menu.classList.toggle("bx-x");
  navlist.classList.toggle("open");
};