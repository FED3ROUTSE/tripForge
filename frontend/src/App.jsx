import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import TripInput from "./pages/TripInput";
import TripSummary from "./pages/TripSummary";
import TravelStyle from "./pages/TravelStyle";
import Navbar from "./components/Navbar";

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<TripInput />} />
        <Route path="/trip-summary" element={<TripSummary />} />
        <Route path="/travel-style" element = {<TravelStyle />} />
      </Routes>
    </Router>
  );
}

export default App;
