import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import TripInput from "./pages/tripInput";
import TripSummary from "./pages/TripSummary";
import Navbar from "./components/Navbar";

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<TripInput />} />
        <Route path="/trip-summary" element={<TripSummary />} />
      </Routes>
    </Router>
  );
}

export default App;
