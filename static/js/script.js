function register() {
    alert("Register button clicked!");
}

document.addEventListener("DOMContentLoaded", function() {
    const images = ["mimage/image1.jpg", "mimage/image2.jpg", "mimage/image3.jpg"];
    let index = 0;

    function changeImage() {
        const headerImages = document.querySelectorAll('.header-image');
        const welcomeMessages = document.querySelectorAll('.welcome-message');

        headerImages.forEach((image, i) => {
            image.src = images[(index + i) % images.length];
        });

        index = (index + 1) % images.length;
    }

    setInterval(changeImage, 3000); // Change image every 3 seconds
});

