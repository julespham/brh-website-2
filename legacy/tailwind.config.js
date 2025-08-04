/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./*.html", "./script.js"],
  theme: {
    extend: {
      colors: {
        'primary': '#2563eb',
        'secondary': '#dc2626', 
        'accent': '#f59e0b',
        'text-dark': '#111827',
        'text-gray': '#6b7280',
        'text-light': '#9ca3af',
        'bg-gray': '#f9fafb',
        'border-color': '#e5e7eb'
      },
      fontFamily: {
        'telex': ['Telex', 'sans-serif'],
        'system': ['-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif']
      },
      maxWidth: {
        'container': '1200px'
      }
    },
  },
  plugins: [],
}