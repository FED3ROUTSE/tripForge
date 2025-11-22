import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

import TripInput from "./components/tripInput";
import Navbar from './components/Navbar';

function App() {
  return (
    <div>
      <Navbar />
      <TripInput />
    </div>
  );
}

export default App;
