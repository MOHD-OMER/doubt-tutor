/**
 * Enhanced Professional Animations for Doubt Tutor
 * Advanced, performant, accessible animations with GSAP-like effects
 * Supports reduced motion, dark/light mode, and custom easing
 */

class DoubtTutorAnimations {
    constructor() {
        this.config = {
            duration: {
                fast: 150,
                base: 300,
                slow: 500,
                epic: 800
            },
            easing: {
                easeIn: 'cubic-bezier(0.4, 0, 1, 1)',
                easeOut: 'cubic-bezier(0, 0, 0.2, 1)',
                easeInOut: 'cubic-bezier(0.4, 0, 0.2, 1)',
                spring: 'cubic-bezier(0.68, -0.55, 0.265, 1.55)',
                bounce: 'cubic-bezier(0.68, -0.6, 0.32, 1.6)'
            },
            thresholds: {
                scroll: 0.15,
                hover: 0.3
            }
        };
        
        this.reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
        this.isDarkMode = window.matchMedia('(prefers-color-scheme: dark)').matches;
        
        this.init();
    }
    
    init() {
        document.addEventListener('DOMContentLoaded', () => {
            if (!this.reducedMotion) {
                this.initScrollAnimations();
                this.initHoverEffects();
                this.initMessageAnimations();
                this.initButtonAnimations();
                this.initThemeTransitions();
                this.initAccessibilityFeatures();
            }
            this.initScrollToBottom();
            this.setupEventListeners();
        });
        
        // Listen for theme changes
        window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
            this.isDarkMode = e.matches;
            this.applyThemeAnimations();
        });
    }
    
    // Enhanced Scroll-based animations with stagger
    initScrollAnimations() {
        const observerOptions = {
            threshold: this.config.thresholds.scroll,
            rootMargin: '0px 0px -100px 0px'
        };
        
        const observer = new IntersectionObserver(
            (entries) => {
                entries.forEach((entry, index) => {
                    if (entry.isIntersecting) {
                        const delay = index * 100;
                        this.animateIn(entry.target, { delay });
                        observer.unobserve(entry.target);
                    }
                });
            },
            observerOptions
        );
        
        document.querySelectorAll('[data-animate="scroll"], .animate-on-scroll').forEach(el => {
            observer.observe(el);
        });
    }
    
    // Advanced hover effects with parallax and scale
    initHoverEffects() {
        const interactiveElements = document.querySelectorAll('.card, .feature-card, .btn, .message-bubble');
        
        interactiveElements.forEach((el, index) => {
            const handleMouseMove = (e) => {
                const rect = el.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;
                const centerX = rect.width / 2;
                const centerY = rect.height / 2;
                const rotateX = (y - centerY) / 10;
                const rotateY = (centerX - x) / 10;
                
                el.style.transform = `
                    perspective(1000px) 
                    rotateX(${rotateX}deg) 
                    rotateY(${rotateY}deg) 
                    scale(1.02)
                `;
                el.style.transition = 'none';
            };
            
            const handleMouseLeave = () => {
                el.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) scale(1)';
                el.style.transition = `transform ${this.config.duration.base}ms ${this.config.easing.spring}`;
            };
            
            el.addEventListener('mouseenter', handleMouseMove);
            el.addEventListener('mouseleave', handleMouseLeave);
            
            // Initial state
            el.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) scale(1)';
            el.style.transition = `transform ${this.config.duration.base}ms ${this.config.easing.spring}`;
        });
    }
    
    // Staggered message animations with typing effect simulation
    initMessageAnimations() {
        const messageWrappers = document.querySelectorAll('.message-wrapper');
        
        messageWrappers.forEach((wrapper, index) => {
            const messages = wrapper.querySelectorAll('.message-bubble');
            messages.forEach((msg, msgIndex) => {
                const totalDelay = index * 200 + msgIndex * 150;
                msg.style.opacity = '0';
                msg.style.transform = 'translateY(20px) scale(0.95)';
                
                setTimeout(() => {
                    this.animateIn(msg, {
                        duration: this.config.duration.base,
                        ease: this.config.easing.easeOut,
                        onComplete: () => this.addTypingEffect(msg)
                    });
                }, totalDelay);
            });
        });
    }
    
    // Enhanced button animations with ripple and micro-interactions
    initButtonAnimations() {
        const buttons = document.querySelectorAll('button, .btn, [role="button"]');
        
        buttons.forEach(button => {
            // Ripple effect
            button.addEventListener('click', (e) => {
                this.createRipple(button, e);
                this.pulse(button);
            });
            
            // Press effect
            button.addEventListener('mousedown', () => {
                button.style.transform = 'scale(0.98)';
            });
            
            button.addEventListener('mouseup', () => {
                button.style.transform = 'scale(1)';
            });
            
            // Hover glow
            button.addEventListener('mouseenter', () => {
                button.style.boxShadow = this.isDarkMode 
                    ? '0 0 20px rgba(99, 102, 241, 0.4)' 
                    : '0 0 20px rgba(99, 102, 241, 0.2)';
            });
            
            button.addEventListener('mouseleave', () => {
                button.style.boxShadow = '';
            });
        });
    }
    
    // Theme transition animations
    initThemeTransitions() {
        const themeElements = document.querySelectorAll('[data-theme-transition]');
        
        themeElements.forEach(el => {
            el.style.transition = `background-color ${this.config.duration.slow}ms ease, color ${this.config.duration.slow}ms ease, border-color ${this.config.duration.slow}ms ease`;
        });
    }
    
    // Accessibility features
    initAccessibilityFeatures() {
        // Skip to content
        const skipLink = document.createElement('a');
        skipLink.href = '#main-content';
        skipLink.textContent = 'Skip to main content';
        skipLink.className = 'skip-link';
        skipLink.style.cssText = `
            position: absolute;
            top: -40px;
            left: 6px;
            background: var(--primary);
            color: white;
            padding: 8px;
            text-decoration: none;
            z-index: 10000;
            border-radius: 4px;
            transition: top 0.3s;
        `;
        skipLink.addEventListener('focus', () => {
            skipLink.style.top = '8px';
        });
        skipLink.addEventListener('blur', () => {
            skipLink.style.top = '-40px';
        });
        document.body.prepend(skipLink);
        
        // Focus management
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Tab') {
                document.body.classList.add('keyboard-nav');
            }
        });
        
        document.addEventListener('mousedown', () => {
            document.body.classList.remove('keyboard-nav');
        });
    }
    
    // Auto-scroll to bottom for chat
    initScrollToBottom() {
        this.scrollChat();
        // Throttled scroll interval
        let scrollTimeout;
        const scrollInterval = 500;
        setInterval(() => {
            clearTimeout(scrollTimeout);
            scrollTimeout = setTimeout(() => this.scrollChat(), scrollInterval);
        }, scrollInterval);
    }
    
    scrollChat() {
        const chatContainer = document.querySelector('.chat, [data-chat-container]');
        if (chatContainer) {
            chatContainer.scrollTop = chatContainer.scrollHeight;
        }
    }
    
    // Generic animation utility
    animateIn(element, options = {}) {
        const defaults = {
            duration: this.config.duration.base,
            ease: this.config.easing.easeOut,
            from: { opacity: 0, transform: 'translateY(20px) scale(0.95)' },
            to: { opacity: 1, transform: 'translateY(0) scale(1)' },
            delay: 0,
            onComplete: null
        };
        
        const settings = { ...defaults, ...options };
        
        element.style.opacity = settings.from.opacity;
        element.style.transform = settings.from.transform;
        element.style.transition = `all ${settings.duration}ms ${settings.ease} ${settings.delay}ms`;
        
        setTimeout(() => {
            element.style.opacity = settings.to.opacity;
            element.style.transform = settings.to.transform;
            
            if (settings.onComplete) {
                setTimeout(settings.onComplete, settings.duration);
            }
        }, settings.delay);
    }
    
    // Enhanced ripple effect
    createRipple(element, event) {
        const ripple = document.createElement('span');
        const rect = element.getBoundingClientRect();
        const size = Math.max(rect.width, rect.height);
        const x = event.clientX - rect.left - size / 2;
        const y = event.clientY - rect.top - size / 2;
        
        ripple.style.cssText = `
            position: absolute;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.6);
            transform: scale(0);
            animation: ripple-effect 0.6s linear;
            width: ${size}px;
            height: ${size}px;
            left: ${x}px;
            top: ${y}px;
            pointer-events: none;
        `;
        
        element.style.position = 'relative';
        element.appendChild(ripple);
        
        setTimeout(() => {
            ripple.remove();
        }, 600);
    }
    
    // Pulse with customizable intensity
    pulse(element, intensity = 1.05, duration = this.config.duration.base) {
        const originalTransform = element.style.transform;
        element.style.transform = `scale(${intensity})`;
        element.style.transition = `transform ${duration}ms ${this.config.easing.easeInOut}`;
        
        setTimeout(() => {
            element.style.transform = originalTransform;
        }, duration);
    }
    
    // Typing effect for messages
    addTypingEffect(element) {
        const text = element.textContent;
        element.textContent = '';
        let i = 0;
        
        const typeWriter = () => {
            if (i < text.length) {
                element.textContent += text.charAt(i);
                i++;
                setTimeout(typeWriter, Math.random() * 50 + 20);
            }
        };
        
        setTimeout(typeWriter, 100);
    }
    
    // Advanced shake with direction control
    shake(element, direction = 'horizontal', intensity = 5) {
        const directions = {
            horizontal: `translateX(${intensity}px)`,
            vertical: `translateY(${intensity}px)`,
            both: `translate(${intensity}px, ${intensity}px)`
        };
        
        element.style.animation = `shake-${direction} 0.6s ${this.config.easing.easeInOut}`;
        
        element.addEventListener('animationend', () => {
            element.style.animation = '';
        }, { once: true });
    }
    
    // Confetti with physics simulation
    createConfetti(count = 75, colors = ['#6366f1', '#8b5cf6', '#ec4899', '#10b981', '#f59e0b']) {
        const animationDuration = 3000 + Math.random() * 2000;
        
        for (let i = 0; i < count; i++) {
            const confetti = document.createElement('div');
            confetti.className = 'enhanced-confetti';
            confetti.style.cssText = `
                position: fixed;
                left: ${Math.random() * 100}vw;
                top: -10px;
                width: ${Math.random() * 10 + 5}px;
                height: ${Math.random() * 10 + 5}px;
                background: ${colors[Math.floor(Math.random() * colors.length)]};
                z-index: 9999;
                pointer-events: none;
                animation: confetti-fall ${animationDuration}ms linear forwards;
                animation-delay: ${Math.random() * 0.5}s;
                transform: rotate(${Math.random() * 360}deg);
            `;
            
            document.body.appendChild(confetti);
            
            setTimeout(() => confetti.remove(), animationDuration + 500);
        }
    }
    
    // Progress bar with easing
    animateProgressBar(element, targetValue, duration = this.config.duration.slow, ease = this.config.easing.easeOut) {
        let startValue = parseFloat(element.style.width) || 0;
        let startTime = null;
        
        const animate = (currentTime) => {
            if (!startTime) startTime = currentTime;
            const elapsed = currentTime - startTime;
            const progress = Math.min(elapsed / duration, 1);
            
            // Apply easing function
            const easedProgress = this.easeFunction(ease, progress);
            const currentValue = startValue + (targetValue - startValue) * easedProgress;
            
            element.style.width = `${currentValue}%`;
            
            if (progress < 1) {
                requestAnimationFrame(animate);
            }
        };
        
        requestAnimationFrame(animate);
    }
    
    // Custom easing function
    easeFunction(type, t) {
        const easings = {
            [this.config.easing.easeIn]: t * t,
            [this.config.easing.easeOut]: 1 - Math.pow(1 - t, 3),
            [this.config.easing.easeInOut]: t < 0.5 ? 4 * t * t * t : (t - 1) * (2 * t - 2) * (2 * t - 2) + 1,
            [this.config.easing.spring]: 1 - Math.pow(1 - t, 3) + t * Math.sin(t * Math.PI),
            [this.config.easing.bounce]: 7.5625 * (t < 1/2.75 ? t * t : t < 2/2.75 ? (t -= 1.5/2.75) * t + .75 : t < 2.5/2.75 ? (t -= 2.25/2.75) * t + .9375 : (t -= 2.625/2.75) * t + .984375)
        };
        return easings[type] || t;
    }
    
    // Smooth scroll with offset and easing
    smoothScrollTo(targetId, offset = 0, duration = this.config.duration.base) {
        const target = document.getElementById(targetId);
        if (!target) return;
        
        const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - offset;
        const startPosition = window.pageYOffset;
        const distance = targetPosition - startPosition;
        let startTime = null;
        
        const animate = (currentTime) => {
            if (!startTime) startTime = currentTime;
            const elapsed = currentTime - startTime;
            const progress = Math.min(elapsed / duration, 1);
            const eased = this.easeFunction(this.config.easing.easeOut, progress);
            
            window.scrollTo(0, startPosition + distance * eased);
            
            if (progress < 1) {
                requestAnimationFrame(animate);
            }
        };
        
        requestAnimationFrame(animate);
    }
    
    // Fade with direction
    fade(element, direction = 'in', duration = this.config.duration.base) {
        const isIn = direction === 'in';
        element.style.opacity = isIn ? '0' : '1';
        element.style.display = isIn ? 'block' : element.style.display;
        
        setTimeout(() => {
            element.style.transition = `opacity ${duration}ms ${this.config.easing.easeInOut}`;
            element.style.opacity = isIn ? '1' : '0';
            
            if (!isIn) {
                setTimeout(() => {
                    element.style.display = 'none';
                }, duration);
            }
        }, 10);
    }
    
    // Scale with bounce
    scale(element, scaleTo = 1, duration = this.config.duration.base) {
        const originalScale = element.style.transform ? 
            parseFloat(element.style.transform.match(/scale\(([^)]+)\)/)?.[1] || 1) : 1;
        
        element.style.transform = `scale(${scaleTo})`;
        element.style.transition = `transform ${duration}ms ${this.config.easing.bounce}`;
    }
    
    // Setup additional event listeners
    setupEventListeners() {
        // Keyboard navigation enhancements
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                this.closeAllModals();
            }
        });
        
        // Resize handler for responsive animations
        window.addEventListener('resize', () => {
            this.debounce(() => {
                this.recalculateAnimations();
            }, 250);
        });
    }
    
    closeAllModals() {
        document.querySelectorAll('[role="dialog"], .modal').forEach(modal => {
            modal.style.display = 'none';
        });
    }
    
    recalculateAnimations() {
        // Recalculate scroll observers on resize
        this.initScrollAnimations();
    }
    
    // Utility: Debounce function
    debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }
    
    // Apply theme-specific animations
    applyThemeAnimations() {
        const elements = document.querySelectorAll('[data-theme-animate]');
        elements.forEach(el => {
            this.fade(el, 'in', this.config.duration.fast);
        });
    }
    
    // Create advanced typing indicator
    createTypingIndicator(parentElement, color = '#6366f1') {
        const indicator = document.createElement('div');
        indicator.className = 'advanced-typing-indicator';
        indicator.innerHTML = `
            <div class="typing-dots">
                <span></span><span></span><span></span>
            </div>
            <span style="margin-left: 8px; color: var(--text-muted);">AI is thinking...</span>
        `;
        
        const style = document.createElement('style');
        style.textContent = `
            .advanced-typing-indicator {
                display: flex;
                align-items: center;
                gap: 8px;
                padding: 12px 16px;
                background: rgba(99, 102, 241, 0.1);
                border-radius: var(--radius-md);
                border: 1px solid var(--border-subtle);
                backdrop-filter: blur(10px);
                animation: typing-fade 2s ease-in-out infinite;
            }
            .typing-dots {
                display: flex;
                gap: 4px;
            }
            .typing-dots span {
                width: 8px;
                height: 8px;
                border-radius: 50%;
                background: ${color};
                display: inline-block;
                animation: typing-bounce 1.4s infinite ease-in-out;
            }
            .typing-dots span:nth-child(2) { animation-delay: 0.2s; }
            .typing-dots span:nth-child(3) { animation-delay: 0.4s; }
            @keyframes typing-bounce {
                0%, 80%, 100% { transform: scale(0.8); opacity: 0.5; }
                40% { transform: scale(1.2); opacity: 1; }
            }
            @keyframes typing-fade {
                0%, 100% { opacity: 1; }
                50% { opacity: 0.7; }
            }
        `;
        
        if (!document.querySelector('#advanced-typing-style')) {
            style.id = 'advanced-typing-style';
            document.head.appendChild(style);
        }
        
        if (parentElement) parentElement.appendChild(indicator);
        return indicator;
    }
}

// Initialize the enhanced animation system
const animations = new DoubtTutorAnimations();

// Global functions for easy access
window.DoubtTutorAnimations = {
    fadeIn: (el, duration) => animations.fade(el, 'in', duration),
    fadeOut: (el, duration) => animations.fade(el, 'out', duration),
    scaleIn: (el, duration) => animations.scale(el, 1, duration),
    shake: (el, direction, intensity) => animations.shake(el, direction, intensity),
    pulse: (el, intensity, duration) => animations.pulse(el, intensity, duration),
    createTypingIndicator: (parent, color) => animations.createTypingIndicator(parent, color),
    createConfetti: (count, colors) => animations.createConfetti(count, colors),
    animateProgressBar: (el, value, duration) => animations.animateProgressBar(el, value, duration),
    smoothScrollTo: (id, offset, duration) => animations.smoothScrollTo(id, offset, duration),
    scrollChat: () => animations.scrollChat()
};

// Enhanced shake keyframes
const enhancedShakeStyle = document.createElement('style');
enhancedShakeStyle.textContent = `
    @keyframes shake-horizontal {
        0%, 100% { transform: translateX(0); }
        10%, 30%, 50%, 70%, 90% { transform: translateX(-8px); }
        20%, 40%, 60%, 80% { transform: translateX(8px); }
    }
    @keyframes shake-vertical {
        0%, 100% { transform: translateY(0); }
        10%, 30%, 50%, 70%, 90% { transform: translateY(-8px); }
        20%, 40%, 60%, 80% { transform: translateY(8px); }
    }
    @keyframes shake-both {
        0%, 100% { transform: translate(0, 0); }
        25% { transform: translate(5px, -5px); }
        75% { transform: translate(-5px, 5px); }
    }
    @keyframes ripple-effect {
        to { transform: scale(4); opacity: 0; }
    }
    .skip-link:focus {
        top: 8px !important;
    }
    body.keyboard-nav :focus-visible {
        outline: 2px solid var(--primary);
        outline-offset: 2px;
        border-radius: var(--radius-sm);
    }
`;
document.head.appendChild(enhancedShakeStyle);

// Auto-scroll implementation
function enhancedScrollChat() {
    animations.scrollChat();
}
setInterval(enhancedScrollChat, 500);