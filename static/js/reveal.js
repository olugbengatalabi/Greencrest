/*=============== SCROLL REVEAL ANIMATION ===============*/
const sr = ScrollReveal({
  origin: 'top',
  distance: '60px',
  duration: 1500,
  // inital duration ws 2500.
  delay: 400,
  // reset: true
})

sr.reveal(`.home__data`)
sr.reveal(`.home__img, .allproducts__button`, {delay: 400})
sr.reveal(`.home__social`, {delay: 500})
sr.reveal(`.about__img, .contact__box`,{origin: 'left'})
sr.reveal(`.about__data, .contact__form`,{origin: 'right'})
sr.reveal(`.steps__card, .product__card, .questions__group, .footer`, { interval: 100 })
sr.reveal(`.description__container`,{delay:400});
sr.reveal(`.image_container`);
sr.reveal(`.cart__container`);
sr.reveal(`.search__form`, { delay: 400 });
sr.reveal(`.table`, { delay: 400 });




