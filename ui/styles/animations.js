/**
 * Professional Animations for Doubt Tutor
 * Smooth, performant, and accessible animations
 */

// Animation configurations
const ANIMATION_CONFIG = {
    duration: {
        fast: 150,
        base: 300,
        slow: 500
    },
    easing: {
        easeIn: 'cubic-bezier(0.4, 0, 1, 1)',
        easeOut: 'cubic-bezier(0, 0, 0.2, 1)',
        easeInOut: 'cubic-bezier(0.4, 0, 0.2, 1)',
        spring: 'cubic-bezier(0.68, -0.55, 0.265, 1.55)'
    }
};

// Check if user prefers reduced motion
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

/**
 * Initialize animations when DOM is loaded
 */
document.addEventListener('DOMContentLoaded', () => {
    if (!prefersReducedMotion) {
        initScrollAnimations();
        initHoverEffects();
        initMessageAnimations();
        initButtonAnimations();
    }
});

/**
 * Scroll-based animations
 */
function initScrollAnimations() {
    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate-in');
                    observer.unobserve(entry.target);
                }
            });
        },
        {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        }
    );

    // Observe elements with animation class
    document.querySelectorAll('.animate-on-scroll').forEach(el => {
        observer.observe(el);
    });
}

/**
 * Enhanced hover effects
 */
function initHoverEffects() {
    const cards = document.querySelectorAll('.feature-card, .card');
    
    cards.forEach(card => {
        card.addEventListener('mouseenter', function(e) {
            this.style.transform = 'translateY(-8px)';
            this.style.transition = `transform ${ANIMATION_CONFIG.duration.base}ms ${ANIMATION_CONFIG.easing.easeOut}`;
        });
        
        card.addEventListener('mouseleave', function(e) {
            this.style.transform = 'translateY(0)';
        });
    });
}

/**
 * Message bubble animations
 */
function initMessageAnimations() {
    const messages = document.querySelectorAll('.message-wrapper');
    
    messages.forEach((msg, index) => {
        msg.style.animation = `slideUp ${ANIMATION_CONFIG.duration.base}ms ${ANIMATION_CONFIG.easing.easeOut} ${index * 50}ms both`;
    });
}

/**
 * Button ripple effect
 */
function initButtonAnimations() {
    const buttons = document.querySelectorAll('.stButton > button');
    
    buttons.forEach(button => {
        button.addEventListener('click', function(e) {
            const ripple = document.createElement('span');
            const rect = this.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            const x = e.clientX - rect.left - size / 2;
            const y = e.clientY - rect.top - size / 2;
            
            ripple.style.width = ripple.style.height = size + 'px';
            ripple.style.left = x + 'px';
            ripple.style.top = y + 'px';
            ripple.classList.add('ripple');
            
            this.appendChild(ripple);
            
            setTimeout(() => {
                ripple.remove();
            }, 600);
        });
    });
}

/**
 * Smooth scroll to element
 */
function smoothScrollTo(targetId, offset = 0) {
    const target = document.getElementById(targetId);
    if (!target) return;
    
    const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - offset;
    
    window.scrollTo({
        top: targetPosition,
        behavior: 'smooth'
    });
}

/**
 * Fade in animation
 */
function fadeIn(element, duration = ANIMATION_CONFIG.duration.base) {
    element.style.opacity = '0';
    element.style.display = 'block';
    
    let start = null;
    
    function animate(timestamp) {
        if (!start) start = timestamp;
        const progress = timestamp - start;
        const opacity = Math.min(progress / duration, 1);
        
        element.style.opacity = opacity;
        
        if (progress < duration) {
            requestAnimationFrame(animate);
        }
    }
    
    requestAnimationFrame(animate);
}

/**
 * Fade out animation
 */
function fadeOut(element, duration = ANIMATION_CONFIG.duration.base) {
    let start = null;
    const initialOpacity = parseFloat(window.getComputedStyle(element).opacity);
    
    function animate(timestamp) {
        if (!start) start = timestamp;
        const progress = timestamp - start;
        const opacity = initialOpacity * (1 - Math.min(progress / duration, 1));
        
        element.style.opacity = opacity;
        
        if (progress < duration) {
            requestAnimationFrame(animate);
        } else {
            element.style.display = 'none';
        }
    }
    
    requestAnimationFrame(animate);
}

/**
 * Slide in from direction
 */
function slideIn(element, direction = 'up', duration = ANIMATION_CONFIG.duration.base) {
    const translations = {
        up: 'translateY(20px)',
        down: 'translateY(-20px)',
        left: 'translateX(20px)',
        right: 'translateX(-20px)'
    };
    
    element.style.opacity = '0';
    element.style.transform = translations[direction];
    element.style.display = 'block';
    
    setTimeout(() => {
        element.style.transition = `opacity ${duration}ms ${ANIMATION_CONFIG.easing.easeOut}, transform ${duration}ms ${ANIMATION_CONFIG.easing.easeOut}`;
        element.style.opacity = '1';
        element.style.transform = 'translate(0, 0)';
    }, 10);
}

/**
 * Scale animation
 */
function scaleIn(element, duration = ANIMATION_CONFIG.duration.base) {
    element.style.transform = 'scale(0.9)';
    element.style.opacity = '0';
    element.style.display = 'block';
    
    setTimeout(() => {
        element.style.transition = `transform ${duration}ms ${ANIMATION_CONFIG.easing.spring}, opacity ${duration}ms ${ANIMATION_CONFIG.easing.easeOut}`;
        element.style.transform = 'scale(1)';
        element.style.opacity = '1';
    }, 10);
}

/**
 * Typing indicator animation
 */
function createTypingIndicator() {
    const indicator = document.createElement('div');
    indicator.className = 'typing-indicator';
    indicator.innerHTML = '<span></span><span></span><span></span>';
    
    const style = document.createElement('style');
    style.textContent = `
        .typing-indicator {
            display: flex;
            gap: 4px;
            padding: 12px;
        }
        .typing-indicator span {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: rgba(99, 102, 241, 0.6);
            animation: typing 1.4s infinite;
        }
        .typing-indicator span:nth-child(2) {
            animation-delay: 0.2s;
        }
        .typing-indicator span:nth-child(3) {
            animation-delay: 0.4s;
        }
        @keyframes typing {
            0%, 60%, 100% { transform: translateY(0); opacity: 0.6; }
            30% { transform: translateY(-10px); opacity: 1; }
        }
    `;
    
    if (!document.querySelector('#typing-indicator-style')) {
        style.id = 'typing-indicator-style';
        document.head.appendChild(style);
    }
    
    return indicator;
}

/**
 * Progress bar animation
 */
function animateProgressBar(element, targetValue, duration = ANIMATION_CONFIG.duration.slow) {
    let start = null;
    const initialValue = parseFloat(element.style.width) || 0;
    
    function animate(timestamp) {
        if (!start) start = timestamp;
        const progress = timestamp - start;
        const value = initialValue + (targetValue - initialValue) * Math.min(progress / duration, 1);
        
        element.style.width = value + '%';
        
        if (progress < duration) {
            requestAnimationFrame(animate);
        }
    }
    
    requestAnimationFrame(animate);
}

/**
 * Shake animation (for errors)
 */
function shake(element) {
    element.style.animation = 'shake 0.5s';
    element.addEventListener('animationend', () => {
        element.style.animation = '';
    }, { once: true });
}

// Add shake keyframes
const shakeStyle = document.createElement('style');
shakeStyle.textContent = `
    @keyframes shake {
        0%, 100% { transform: translateX(0); }
        10%, 30%, 50%, 70%, 90% { transform: translateX(-5px); }
        20%, 40%, 60%, 80% { transform: translateX(5px); }
    }
`;
document.head.appendChild(shakeStyle);

/**
 * Pulse animation (for notifications)
 */
function pulse(element, duration = ANIMATION_CONFIG.duration.base) {
    element.style.animation = `pulse ${duration}ms ${ANIMATION_CONFIG.easing.easeInOut}`;
    element.addEventListener('animationend', () => {
        element.style.animation = '';
    }, { once: true });
}

// Add pulse keyframes
const pulseStyle = document.createElement('style');
pulseStyle.textContent = `
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
`;
document.head.appendChild(pulseStyle);

/**
 * Confetti animation (for celebrations)
 */
function createConfetti(count = 50) {
    const colors = ['#6366f1', '#8b5cf6', '#ec4899', '#10b981', '#f59e0b'];
    
    for (let i = 0; i < count; i++) {
        const confetti = document.createElement('div');
        confetti.className = 'confetti';
        confetti.style.left = Math.random() * 100 + '%';
        confetti.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
        confetti.style.animationDelay = Math.random() * 3 + 's';
        
        document.body.appendChild(confetti);
        
        setTimeout(() => confetti.remove(), 3000);
    }
}

// Add confetti styles
const confettiStyle = document.createElement('style');
confettiStyle.textContent = `
    .confetti {
        position: fixed;
        width: 10px;
        height: 10px;
        top: -10px;
        z-index: 9999;
        animation: confetti-fall 3s linear forwards;
    }
    @keyframes confetti-fall {
        to {
            transform: translateY(100vh) rotate(360deg);
            opacity: 0;
        }
    }
`;
document.head.appendChild(confettiStyle);

// Export functions for use in other scripts
window.DoubtTutorAnimations = {
    fadeIn,
    fadeOut,
    slideIn,
    scaleIn,
    shake,
    pulse,
    createTypingIndicator,
    createConfetti,
    animateProgressBar,
    smoothScrollTo
};
function scrollChat() {
    const box = document.querySelector('.chat');
    if (box) {
        box.scrollTop = box.scrollHeight;
    }
}
setInterval(scrollChat, 500);
