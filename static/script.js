document.addEventListener("DOMContentLoaded", function() {
  const members = document.querySelectorAll(".member");
  let delay = 0;

  members.forEach((member, index) => {
    setTimeout(() => {
      member.style.transitionDelay = `${index * 0.3}s`;
      member.style.opacity = 1;
      member.style.transform = "translateY(0)";
    }, delay * 1000);
    
    delay += 0.2;
  });
});

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
