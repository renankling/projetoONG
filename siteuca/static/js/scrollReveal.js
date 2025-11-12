document.addEventListener("DOMContentLoaded", function () {
  const cards = document.querySelectorAll(".noticia-card");

  function revealCards() {
    const windowHeight = window.innerHeight;
    const revealPoint = 100;

    cards.forEach((card, index) => {
      const cardTop = card.getBoundingClientRect().top;

      if (cardTop < windowHeight - revealPoint && !card.classList.contains("active")) {
        
        setTimeout(() => {
          card.classList.add("active");
        }, index * 200);
      }
    });
  }

  window.addEventListener("scroll", revealCards);
  revealCards();
});