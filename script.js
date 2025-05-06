// Menu toggle functionality
const menuButton = document.getElementById('menuButton');
const closeMenuButton = document.getElementById('closeMenuButton');
const menuOverlay = document.getElementById('menuOverlay');

menuButton.addEventListener('click', () => {
  menuOverlay.classList.remove('hidden');
});

closeMenuButton.addEventListener('click', () => {
  menuOverlay.classList.add('hidden');
});
<!-- At the end of your body tag, add this script -->
