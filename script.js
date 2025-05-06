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
<script>
  // Initialize feather icons
  feather.replace();
  
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
  
  // Slideshow functionality
  let slideIndex = 1;
  
  // Run once the DOM is fully loaded
  document.addEventListener("DOMContentLoaded", function() {
    showSlides(slideIndex);
    
    // Add event listeners to prev/next buttons
    const prevButton = document.querySelector('.prev');
    const nextButton = document.querySelector('.next');
    
    prevButton.addEventListener('click', function() {
      plusSlides(-1);
    });
    
    nextButton.addEventListener('click', function() {
      plusSlides(1);
    });
    
    // Add event listeners to dots
    const dots = document.querySelectorAll('.dot');
    dots.forEach(function(dot, index) {
      dot.addEventListener('click', function() {
        currentSlide(index + 1);
      });
    });
  });
  
  // Next/previous controls
  function plusSlides(n) {
    showSlides(slideIndex += n);
  }
  
  // Thumbnail image controls
  function currentSlide(n) {
    showSlides(slideIndex = n);
  }
  
  function showSlides(n) {
    let i;
    let slides = document.querySelectorAll(".mySlides");
    let dots = document.querySelectorAll(".dot");
    
    if (n > slides.length) {slideIndex = 1}
    if (n < 1) {slideIndex = slides.length}
    
    // Hide all slides
    for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
    }
    
    // Remove active class from all dots
    for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" bg-gray-800", " bg-gray-300");
    }
    
    // Show the current slide and activate the dot
    slides[slideIndex-1].style.display = "block";
    dots[slideIndex-1].className = dots[slideIndex-1].className.replace(" bg-gray-300", " bg-gray-800");
  }
</script>
