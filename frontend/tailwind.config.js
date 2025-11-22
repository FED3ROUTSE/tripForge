/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}"
  ],
  theme: {
    extend: {
      keyframes: {
        'takeoff-move': { // Αυτό είναι το όνομα του keyframe
          '0%': { transform: 'translateY(100px) translateX(-50px) rotate(0deg)', opacity: '1' },
          '50%': { transform: 'translateY(-50px) translateX(25px) rotate(-15deg)' },
          '100%': { transform: 'translateY(-150px) translateX(100px) rotate(-30deg)', opacity: '1' },
        },
        'landing-move': { // Αυτό είναι το όνομα του keyframe
          '0%': { transform: 'translateY(-150px) translateX(100px) rotate(-30deg)', opacity: '0' },
          '1%': { opacity: '1' }, // Για να εμφανιστεί αμέσως στην αρχή
          '50%': { transform: 'translateY(-50px) translateX(25px) rotate(-15deg)' },
          '100%': { transform: 'translateY(100px) translateX(-50px) rotate(0deg)', opacity: '1' },
        },
      },
      animation: { // Αυτό συσχετίζει το keyframe με ένα class name
        'takeoff': 'takeoff-move 1.5s forwards ease-out',
        'landing': 'landing-move 1.5s forwards ease-in',
      },
    },
  },
  plugins: [],
}