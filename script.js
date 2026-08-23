document.addEventListener('DOMContentLoaded', () => {
    console.log("EngiNotes platform initialized.");

    // Navbar scroll effect
    const navbar = document.getElementById('navbar');

    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // Simple smooth scrolling for future sections
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;

            const target = document.querySelector(targetId);
            if (target) {
                e.preventDefault();
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // The lucide icons are initialized directly in the HTML via <script> tag 
    // to ensure they render as quickly as possible.

    
    // Mobile Menu Toggle
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const navLinks = document.querySelector('.nav-links');
    if (mobileMenuBtn && navLinks) {
        mobileMenuBtn.addEventListener('click', () => {
            navLinks.classList.toggle('mobile-active');
        });
    }

    // Auth Page Logic
    const tabSignIn = document.getElementById('tab-signin');
    const tabSignUp = document.getElementById('tab-signup');
    const formSignIn = document.getElementById('form-signin');
    const formSignUp = document.getElementById('form-signup');

    if (tabSignIn && tabSignUp && formSignIn && formSignUp) {
        tabSignIn.addEventListener('click', () => {
            tabSignIn.classList.add('active');
            tabSignUp.classList.remove('active');
            formSignIn.classList.add('active');
            formSignUp.classList.remove('active');
        });

        tabSignUp.addEventListener('click', () => {
            tabSignUp.classList.add('active');
            tabSignIn.classList.remove('active');
            formSignUp.classList.add('active');
            formSignIn.classList.remove('active');
        });

    }

    // Dynamic PPS Notes Rendering
    const ppsNotes = [
        {
            title: "PPS Unit 1",
            description: "Programming for Problem Solving — Unit 1 Crash Course Notes",
            file: "assets/pdf/PPS_Unit_1_Slides.pdf",
            icon: "monitor-play",
            colorClass: "var(--accent-blue)",
            bgClass: "rgba(59, 130, 246, 0.1)"
        },
        {
            title: "PPS Unit 3",
            description: "Programming for Problem Solving — Unit 3 Crash Course Notes",
            file: "assets/pdf/PPS_Unit_3_Slides.pdf",
            icon: "monitor-play",
            colorClass: "var(--accent-green)",
            bgClass: "rgba(16, 185, 129, 0.1)"
        },
        {
            title: "PPS Unit 4: Functions & Searching",
            description: "Complete one-shot slides covering Functions, Arrays with Functions, Linear Search, Binary Search, and Sorting algorithms.",
            file: "assets/pdf/PPS_Unit_4_Slides.pdf",
            icon: "code",
            colorClass: "var(--accent-purple)",
            bgClass: "rgba(139, 92, 246, 0.1)"
        },
        {
            title: "PPS Unit 5: Pointers & Files",
            description: "Comprehensive slides covering Pointers, Dynamic Memory Allocation, File Handling, and Preprocessor Macros.",
            file: "assets/pdf/PPS_Unit_5_Slides.pdf",
            icon: "cpu",
            colorClass: "var(--accent-cyan)",
            bgClass: "rgba(6, 182, 212, 0.1)"
        }
    ];

    const ppsGrid = document.getElementById('pps-notes-grid');
    if (ppsGrid) {
        ppsGrid.innerHTML = '';
        ppsNotes.forEach(note => {
            const cardHTML = `
                <div class="resource-card">
                    <div class="resource-icon" style="color: ${note.colorClass}; background: ${note.bgClass};">
                        <i data-lucide="${note.icon}"></i>
                    </div>
                    <h3>${note.title}</h3>
                    <p>${note.description}</p>
                    <div class="action-buttons">
                        <a href="${note.file}" target="_blank" class="secondary-btn"><i data-lucide="eye"></i> View</a>
                        <a href="${note.file}" download class="primary-btn glow-btn"><i data-lucide="download"></i> Download</a>
                    </div>
                </div>
            `;
            ppsGrid.innerHTML += cardHTML;
document.addEventListener('DOMContentLoaded', () => {
    console.log("EngiNotes platform initialized.");

    // Navbar scroll effect
    const navbar = document.getElementById('navbar');

    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // Simple smooth scrolling for future sections
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;

            const target = document.querySelector(targetId);
            if (target) {
                e.preventDefault();
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // The lucide icons are initialized directly in the HTML via <script> tag 
    // to ensure they render as quickly as possible.

    
    // Mobile Menu Toggle
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const navLinks = document.querySelector('.nav-links');
    if (mobileMenuBtn && navLinks) {
        mobileMenuBtn.addEventListener('click', () => {
            navLinks.classList.toggle('mobile-active');
        });
    }

    // Auth Page Logic
    const tabSignIn = document.getElementById('tab-signin');
    const tabSignUp = document.getElementById('tab-signup');
    const formSignIn = document.getElementById('form-signin');
    const formSignUp = document.getElementById('form-signup');

    if (tabSignIn && tabSignUp && formSignIn && formSignUp) {
        tabSignIn.addEventListener('click', () => {
            tabSignIn.classList.add('active');
            tabSignUp.classList.remove('active');
            formSignIn.classList.add('active');
            formSignUp.classList.remove('active');
        });

        tabSignUp.addEventListener('click', () => {
            tabSignUp.classList.add('active');
            tabSignIn.classList.remove('active');
            formSignUp.classList.add('active');
            formSignIn.classList.remove('active');
        });

    }

    // Dynamic PPS Notes Rendering
    const ppsNotes = [
        {
            title: "PPS Unit 1",
            description: "Programming for Problem Solving — Unit 1 Crash Course Notes",
            file: "assets/pdf/PPS_Unit_1_Slides.pdf",
            icon: "monitor-play",
            colorClass: "var(--accent-blue)",
            bgClass: "rgba(59, 130, 246, 0.1)"
        },
        {
            title: "PPS Unit 3",
            description: "Programming for Problem Solving — Unit 3 Crash Course Notes",
            file: "assets/pdf/PPS_Unit_3_Slides.pdf",
            icon: "monitor-play",
            colorClass: "var(--accent-green)",
            bgClass: "rgba(16, 185, 129, 0.1)"
        },
        {
            title: "PPS Unit 4: Functions & Searching",
            description: "Complete one-shot slides covering Functions, Arrays with Functions, Linear Search, Binary Search, and Sorting algorithms.",
            file: "assets/pdf/PPS_Unit_4_Slides.pdf",
            icon: "code",
            colorClass: "var(--accent-purple)",
            bgClass: "rgba(139, 92, 246, 0.1)"
        },
        {
            title: "PPS Unit 5: Pointers & Files",
            description: "Comprehensive slides covering Pointers, Dynamic Memory Allocation, File Handling, and Preprocessor Macros.",
            file: "assets/pdf/PPS_Unit_5_Slides.pdf",
            icon: "cpu",
            colorClass: "var(--accent-cyan)",
            bgClass: "rgba(6, 182, 212, 0.1)"
        }
    ];

    const ppsGrid = document.getElementById('pps-notes-grid');
    if (ppsGrid) {
        ppsGrid.innerHTML = '';
        ppsNotes.forEach(note => {
            const cardHTML = `
                <div class="resource-card">
                    <div class="resource-icon" style="color: ${note.colorClass}; background: ${note.bgClass};">
                        <i data-lucide="${note.icon}"></i>
                    </div>
                    <h3>${note.title}</h3>
                    <p>${note.description}</p>
                    <div class="action-buttons">
                        <a href="${note.file}" target="_blank" class="secondary-btn"><i data-lucide="eye"></i> View</a>
                        <a href="${note.file}" download class="primary-btn glow-btn"><i data-lucide="download"></i> Download</a>
                    </div>
                </div>
            `;
            ppsGrid.innerHTML += cardHTML;
        });

        if (typeof lucide !== 'undefined') {
            lucide.createIcons();
        }
    }
});
