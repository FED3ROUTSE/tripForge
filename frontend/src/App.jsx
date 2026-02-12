import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import TripInput from "./pages/tripInput";
import TripSummary from "./pages/TripSummary";
import TravelStyle from "./pages/travelStyle";
import TravelPlan from "./pages/travelPlan"; 
import Navbar from "./components/Navbar";

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<TripInput />} />
        <Route path="/trip-summary" element={<TripSummary />} />
        <Route path="/travel-style" element={<TravelStyle />} />
        <Route path="/travel-plan" element={<TravelPlan />} />
      </Routes>
    </Router>
  );
}

export default App;