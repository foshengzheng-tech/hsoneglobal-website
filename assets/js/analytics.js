// Vercel Web Analytics
// This script initializes Vercel Web Analytics for page view tracking
(function() {
  // Inject analytics script from Vercel
  function injectAnalytics() {
    if (typeof window === 'undefined') return;
    
    // Initialize queue
    if (window.va) return;
    window.va = function va() {
      var args = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : [];
      if (!window.vaq) window.vaq = [];
      window.vaq.push(args);
    };
    
    // Set mode to auto-detect (production on Vercel, development locally)
    window.vam = 'auto';
    
    // Get the analytics script path
    // When deployed on Vercel with Analytics enabled, this will be available
    var scriptSrc = '/_vercel/insights/script.js';
    
    // Check if script is already loaded
    if (document.head.querySelector('script[src*="' + scriptSrc + '"]')) return;
    
    // Create and inject the script
    var script = document.createElement('script');
    script.src = scriptSrc;
    script.defer = true;
    script.setAttribute('data-sdk', 'web-analytics');
    
    script.onerror = function() {
      console.log('[Vercel Web Analytics] Analytics script will be available after deployment to Vercel with Analytics enabled.');
    };
    
    document.head.appendChild(script);
  }
  
  // Initialize analytics when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', injectAnalytics);
  } else {
    injectAnalytics();
  }
})();
