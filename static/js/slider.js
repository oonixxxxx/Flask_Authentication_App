document.addEventListener('DOMContentLoaded', function() {
    const slider = document.querySelector('.testimonials-slider');
    let isScrolling = false;
    
    setInterval(() => {
        if (!isScrolling) {
            slider.scrollLeft += slider.offsetWidth;
            if (slider.scrollLeft >= slider.scrollWidth - slider.offsetWidth) {
                slider.scrollLeft = 0;
            }
        }
    }, 3000);

    slider.addEventListener('scroll', () => {
        isScrolling = true;
        setTimeout(() => {
            isScrolling = false;
        }, 150);
    });
}); 