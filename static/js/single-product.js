/*jshint -W033 */
let swiperImages = new Swiper('.image__container', {
  cssMode: true,
  loop: true,
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
  pagination: {
    el: '.swiper-pagination',
    clickable:true,
  },
  scrollbar: {
    e1: 'swiper-scrollbar',
  },
  mousewheel: true,
  keyboard: true
});
