document.querySelector(".primary").addEventListener("click", () => {
    alert("Thank you! Our team will contact you shortly.");
});

document.querySelector(".whatsapp").addEventListener("click", () => {
    window.open("https://wa.me/91XXXXXXXXXX", "_blank");
});

document.querySelector(".view-work").addEventListener("click", () => {
    alert('');
});


const toggle = document.getElementById("menuToggle");
const nav = document.getElementById("navMenu");



document.querySelectorAll('a[href^="#"]').forEach(link => {
    link.addEventListener("click", () => {
        nav.style.display = "none";
    });
});



const animatedElements = document.querySelectorAll(".animate");

const observer = new IntersectionObserver(
    (entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("show");
            }
        });
    },
    {
        threshold: 0.2
    }
);

animatedElements.forEach(el => observer.observe(el));

