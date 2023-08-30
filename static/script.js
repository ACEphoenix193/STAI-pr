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