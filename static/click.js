document.addEventListener('DOMContentLoaded', function () {
    const navLinks = document.querySelectorAll('.nav-link');

    navLinks.forEach(item => {
        item.addEventListener('click', function () {
            navLinks.forEach(navLink => navLink.classList.remove('active'));
            this.classList.add('active');
            });

        });
    });