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

// Add this to your existing menu JavaScript
document.addEventListener('click', function(event) {
  // Check if menu is open
  if (!menuOverlay.classList.contains('hidden') && !menuOverlay.classList.contains('active')) {
    // Check if the click is outside the menu
    if (!menuOverlay.contains(event.target) && event.target !== menuButton) {
      // Close the menu
      menuOverlay.classList.remove('active');
      setTimeout(function() {
        menuOverlay.classList.add('hidden');
      }, 300);
    }
  }
});

