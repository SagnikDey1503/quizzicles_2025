document.addEventListener('DOMContentLoaded', () => {
  const toggle = document.querySelector('.menu-toggle');
  const navList = document.querySelector('nav ul');
  if (toggle) {
    toggle.addEventListener('click', () => {
      navList.classList.toggle('open');
    });
  }
});
