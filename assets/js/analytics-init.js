// Initialize Vercel Web Analytics
import { inject } from './analytics.mjs';

// Inject the analytics script
inject({
  mode: 'production',
  debug: false
});
