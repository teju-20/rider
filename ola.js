document.addEventListener("DOMContentLoaded", function() {
    // Elements
    const homeButton = document.getElementById('homeButton');
    const homeDropdown = document.getElementById('homeDropdown');
    const rideForm = document.getElementById('rideForm');
    const rideDetails = document.getElementById('rideDetails');
    const contactUsButton = document.getElementById('contactUsButton');
    const contactSection = document.getElementById('contact');

    // Toggle Home Dropdown Menu
    homeButton.addEventListener('mouseenter', () => {
        clearTimeout(timeoutId);
        homeDropdown.classList.add('show');
    });
    homeButton.addEventListener('mouseleave', () =>{
        timeoutId = setTimeout(() => {
            homeDropdown.classList.remove('show');
        }, 1000);
    });

    // Toggle Contact Us Section
    contactUsButton.addEventListener('click', function(event) {
        event.preventDefault();
        contactSection.classList.add('visible');
    });

    // Show Ride Form after 10 seconds
    setTimeout(() => {
        rideForm.classList.add('visible');
    }, 10000); // 10000 milliseconds = 10 seconds

    // Handle Form Submission
    rideForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission



        // Hide the form and show details
        rideForm.classList.add('visible');
        rideDetails.classList.remove('hidden');

    });
});