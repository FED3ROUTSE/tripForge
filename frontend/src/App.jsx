import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";

import TripInput from "./pages/tripInput";
import Navbar from './components/Navbar';

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
      <Route exact path = "/" element={<TripInput />}
      />
      </Routes>
    </Router>
  );
}

export default App;
