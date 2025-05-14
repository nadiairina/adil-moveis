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

// Close menu when clicking outside
document.addEventListener('click', function(event) {
  // Check if menu is open (not hidden)
  if (!menuOverlay.classList.contains('hidden')) {
    // Check if the click is outside the menu AND not on the menu button itself
    if (!menuOverlay.contains(event.target) && event.target !== menuButton && !menuButton.contains(event.target)) {
      // Close the menu
      menuOverlay.classList.add('hidden');
    }
  }
});
