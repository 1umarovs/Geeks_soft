const mobileMenu = document.querySelector(".list"),
  burgerBtn = document.querySelector(".burger"),
  navLinks = document.querySelectorAll(".list-link"),
  closeBtn = document.querySelector(".close-btn"),
  body = document.body;

burgerBtn.addEventListener("click", () => {
  mobileMenu.classList.toggle("active_navbar");
  burgerBtn.classList.toggle("active_burger");
  body.classList.toggle("active-scroll");
});

navLinks.forEach((link) =>
  link.addEventListener("click", () => {
    navLinks.forEach((l) => l.classList.remove("active"));
    link.classList.add("active");
    closeMenu();
  })
);

function closeMenu() {
  mobileMenu.classList.remove("active_navbar");
  burgerBtn.classList.remove("active_burger");
  body.classList.remove("active-scroll");
}

const modal = document.getElementById("imageModal");
const modalImg = document.getElementById("modalImg");
const closeModal = document.querySelector(".modal .close");
const viewBtns = document.querySelectorAll(".show-btn");

viewBtns.forEach((btn) => {
  btn.addEventListener("click", function (e) {
    e.preventDefault();

    const parentSlide = btn.closest(".portfolio-slide");
    const imgTag = parentSlide?.querySelector("img");
    const imgSrc = imgTag?.getAttribute("src");

    if (!imgSrc) return;

    modalImg.src = imgSrc;
    modal.style.display = "flex";
    body.classList.add("active-scroll");
  });
});

closeModal.addEventListener("click", function () {
  closeImageModal();
});

modal.addEventListener("click", function (e) {
  if (e.target === modal) {
    closeImageModal();
  }
});

window.addEventListener("load", () => {
  closeImageModal();
});

function closeImageModal() {
  modal.style.display = "none";
  modalImg.src = "";
  body.classList.remove("active-scroll");
}

const mapWrapperElement = document.querySelector(".map-wrapper");

document.addEventListener("click", (e) => {
  mapWrapperElement.classList.toggle(
    "is-active",
    e.target === mapWrapperElement
  );
});

const allDetails = document.querySelectorAll(".accordion details");
allDetails.forEach((details) => {
  const btn = details.querySelector(".toggleBtn");
  btn.addEventListener("click", () => {
    details.open = !details.open;
    btn.textContent = details.open ? "−" : "+";
  });
  details.addEventListener("toggle", () => {
    btn.textContent = details.open ? "−" : "+";
  });
});


