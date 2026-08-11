document.addEventListener('DOMContentLoaded', () => {
    const thumbs = document.querySelectorAll('.thumbs img');
    if (thumbs.length > 0) {
        // Set first thumb as active by default
        thumbs[0].classList.add('active');
        
        thumbs.forEach(img => {
            img.addEventListener('click', () => {
                const layout = img.closest('.product-layout');
                const main = layout.querySelector('.main-product-img');
                if (main) {
                    main.src = img.src;
                    // Update active state
                    thumbs.forEach(t => t.classList.remove('active'));
                    img.classList.add('active');
                }
            });
        });
    }
});
