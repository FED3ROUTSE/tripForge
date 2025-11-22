import React, { useState } from "react";
import { MapPin, Calendar, DollarSign, Loader2 } from "lucide-react"; // Προσθήκη Loader2
import background from "../images/background.jpeg";

export default function TripInput() {
  const [formData, setFormData] = useState({
    destination: "",
    arrivalDate: "",
    departureDate: "",
    budget: "",
  });

  const [response, setResponse] = useState(null);
  const [isSubmitting, setIsSubmitting] = useState(false); // ΝΕΟ STATE: Loading

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setResponse(null);
    setIsSubmitting(true); // Ενεργοποίηση Loading

    const data = {
      destination: formData.destination,
      arrival: formData.arrivalDate,
      departure: formData.departureDate,
      budget: Number(formData.budget),
    };

    try {
      const res = await fetch("http://127.0.0.1:8000/api/plan-trip/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
      });
      const json = await res.json();
      setResponse(json);
    } catch (err) {
      console.error(err);
      setResponse({ error: "Failed to submit trip" });
    } finally {
      setIsSubmitting(false); // Απενεργοποίηση Loading (είτε επιτυχία είτε αποτυχία)
    }
  };

  return (
    <div className="relative min-h-screen w-full bg-gray-50">
      
      {/* BACKGROUND IMAGE LAYER */}
      <div
        className="fixed inset-0 bg-cover bg-center z-0"
        style={{
          backgroundImage: `url(${background})`,
          opacity: "0.4",
        }}
      />

      {/* CONTENT LAYER */}
      <div className="relative z-10 flex flex-col items-center justify-center min-h-screen px-4 py-12">
        
        {/* WHITE CARD CONTAINER */}
        <div className="w-full max-w-3xl bg-white rounded-2xl shadow-2xl p-8 bg-opacity-95 backdrop-blur-sm mt-10">
          
          <div className="text-center mb-8">
            <h1 className="text-gray-900 text-3xl md:text-4xl font-bold mb-2">
              Plan Your Next Adventure
            </h1>
            <p className="text-gray-500">Enter your trip details to get started</p>
          </div>

          <form onSubmit={handleSubmit} className="space-y-6">
            {/* Destination */}
            <div>
              <label className="block text-gray-700 mb-2 font-medium">Destination</label>
              <div className="relative">
                <MapPin className="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
                <input
                  type="text"
                  name="destination"
                  value={formData.destination}
                  onChange={handleChange}
                  placeholder="Where are you going?"
                  required
                  className="w-full pl-11 pr-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none transition-all"
                />
              </div>
            </div>

            {/* Dates Grid */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div>
                <label className="block text-gray-700 mb-2 font-medium">Date of Arrival</label>
                <div className="relative">
                  <Calendar className="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
                  <input
                    type="date"
                    name="arrivalDate"
                    value={formData.arrivalDate}
                    onChange={handleChange}
                    required
                    className="w-full pl-11 pr-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none transition-all"
                  />
                </div>
              </div>

              <div>
                <label className="block text-gray-700 mb-2 font-medium">
                  Date of Departure
                </label>
                <div className="relative">
                  <Calendar className="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
                  <input
                    type="date"
                    name="departureDate"
                    value={formData.departureDate}
                    onChange={handleChange}
                    required
                    className="w-full pl-11 pr-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none transition-all"
                  />
                </div>
              </div>
            </div>

            {/* Budget */}
            <div>
              <label className="block text-gray-700 mb-2 font-medium">Budget</label>
              <div className="relative">
                <DollarSign className="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
                <input
                  type="number"
                  name="budget"
                  value={formData.budget}
                  onChange={handleChange}
                  placeholder="Enter your budget"
                  min="0"
                  step="0.01"
                  required
                  className="w-full pl-11 pr-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none transition-all"
                />
              </div>
            </div>

            <button
              type="submit"
              disabled={isSubmitting} 
              className={`w-full text-white py-3 rounded-lg transition shadow-lg font-semibold text-lg flex items-center justify-center space-x-2 
                ${isSubmitting 
                  ? 'bg-blue-400 cursor-not-allowed' 
                  : 'bg-blue-600 hover:bg-blue-700'
                }`
              }
            >
              {isSubmitting ? (
                <>
                  <Loader2 className="w-5 h-5 animate-spin" />
                  <span>Planning Trip...</span>
                </>
              ) : (
                <span>Plan My Trip</span>
              )}
            </button>
          </form>

          {response && (
            <div className="mt-6 p-4 bg-gray-50 rounded-lg border border-gray-200">
              <pre className="text-sm text-gray-800 overflow-auto">
                {JSON.stringify(response, null, 2)}
              </pre>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}