// Client-side validation and UX enhancements
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const submitBtn = form ? form.querySelector('button[type="submit"]') : null;
    const yearInput = document.querySelector('input[name="year"]');
    const priceInput = document.querySelector('input[name="present_price"]');
    const kmsInput = document.querySelector('input[name="kms_driven"]');

    // --- Loading animation on form submit ---
    if (form && submitBtn) {
        form.addEventListener('submit', function(e) {
            // Check if there are client-side errors
            let hasError = false;
            
            if (yearInput) {
                const result = validateField(yearInput, validators.year);
                if (!result.valid) hasError = true;
            }
            if (priceInput) {
                const result = validateField(priceInput, validators.price);
                if (!result.valid) hasError = true;
            }
            if (kmsInput) {
                const result = validateField(kmsInput, validators.kms);
                if (!result.valid) hasError = true;
            }

            if (!hasError) {
                // Show loading state
                submitBtn.classList.add('loading');
                submitBtn.disabled = true;
                
                // Create spinner if it doesn't exist
                let spinner = submitBtn.querySelector('.spinner');
                if (!spinner) {
                    spinner = document.createElement('span');
                    spinner.className = 'spinner';
                    submitBtn.appendChild(spinner);
                }
                
                // Keep loading state (form will submit anyway)
                // The spinner will disappear when page reloads with result
            }
        });
    }

    // --- Real-time validation styling ---
    function validateField(input, validator) {
        const result = validator(input.value);
        if (result.valid) {
            input.classList.remove('input-error');
            input.style.borderColor = '#7b61ff';
        } else {
            input.classList.add('input-error');
            input.style.borderColor = '#e74c3c';
        }
        return result;
    }

    const validators = {
        year: (val) => {
            const num = parseInt(val);
            if (!val) return { valid: false, message: 'Year is required' };
            if (isNaN(num)) return { valid: false, message: 'Must be a number' };
            if (num < 1980) return { valid: false, message: 'Must be at least 1980' };
            if (num > 2026) return { valid: false, message: 'Cannot be in the future' };
            return { valid: true };
        },
        price: (val) => {
            const num = parseFloat(val);
            if (!val) return { valid: false, message: 'Price is required' };
            if (isNaN(num)) return { valid: false, message: 'Must be a number' };
            if (num <= 0) return { valid: false, message: 'Must be greater than 0' };
            if (num > 100) return { valid: false, message: 'Value seems too high' };
            return { valid: true };
        },
        kms: (val) => {
            const num = parseInt(val);
            if (!val) return { valid: false, message: 'Kilometers is required' };
            if (isNaN(num)) return { valid: false, message: 'Must be a number' };
            if (num < 0) return { valid: false, message: 'Cannot be negative' };
            if (num > 1000000) return { valid: false, message: 'Value seems too high' };
            return { valid: true };
        }
    };

    // Attach validation events
    if (yearInput) {
        yearInput.addEventListener('blur', function() {
            validateField(this, validators.year);
        });
        yearInput.addEventListener('input', function() {
            if (this.value && !this.classList.contains('input-error')) {
                // Only validate on input if already in error state
            }
        });
    }
    if (priceInput) {
        priceInput.addEventListener('blur', function() {
            validateField(this, validators.price);
        });
    }
    if (kmsInput) {
        kmsInput.addEventListener('blur', function() {
            validateField(this, validators.kms);
        });
    }

    // --- Reset button functionality ---
    const resetLink = document.querySelector('.btn-secondary');
    if (resetLink) {
        resetLink.addEventListener('click', function(e) {
            e.preventDefault();
            // Redirect to reset route
            window.location.href = '/reset';
        });
    }

    // --- Auto-scroll to result if it exists ---
    const resultSection = document.getElementById('result-anchor');
    if (resultSection) {
        // Remove loading state from button if it exists
        if (submitBtn) {
            submitBtn.classList.remove('loading');
            submitBtn.disabled = false;
        }
        
        setTimeout(function() {
            resultSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }, 400);
    }

    // --- Remove loading state on page load if no result ---
    if (!resultSection && submitBtn) {
        submitBtn.classList.remove('loading');
        submitBtn.disabled = false;
    }
});