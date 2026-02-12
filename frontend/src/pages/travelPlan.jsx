import React, { useState } from "react";
import { MapPin, Calendar, Clock, Hotel, RefreshCcw } from "lucide-react";
import { useLocation } from "react-router-dom";

export default function TravelPlan() {
  const { state } = useLocation();

  const [hotel, setHotel] = useState("");
  const [showHotelInput, setShowHotelInput] = useState(false);

  if (!state) {
    return (
      <div className="pt-24 text-center text-gray-500">
        No travel plan data available
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50 pt-24 px-4">
      <div className="max-w-6xl mx-auto">

        {/* HEADER */}
        <div className="mb-10 text-center">
          <h1 className="text-4xl font-bold text-gray-900 mb-3">
            Your Travel Plan
          </h1>
          <p className="text-gray-600 flex justify-center items-center gap-2">
            <MapPin className="w-4 h-4" />
            {state.destination}
            <span className="mx-2">•</span>
            <Calendar className="w-4 h-4" />
            {state.arrival} → {state.departure}
          </p>
        </div>

        {/* HOTEL SECTION */}
        <div className="bg-white rounded-2xl shadow-md p-6 mb-12">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <Hotel className="text-gray-600" />
              <h2 className="text-lg font-semibold text-gray-800">
                Staying somewhere?
              </h2>
            </div>

            <button
              onClick={() => setShowHotelInput(!showHotelInput)}
              className="text-sm text-[#527a7a] font-medium hover:underline"
            >
              {showHotelInput ? "Hide" : "Add hotel"}
            </button>
          </div>

          {showHotelInput && (
            <div className="mt-4">
              <input
                type="text"
                placeholder="Hotel name or area (optional)"
                value={hotel}
                onChange={(e) => setHotel(e.target.value)}
                className="w-full border rounded-xl px-4 py-2 focus:outline-none focus:ring-2 focus:ring-[#527a7a]"
              />
              <p className="text-xs text-gray-500 mt-2">
                This helps optimize distances between activities.
              </p>
            </div>
          )}
        </div>

        {/* ITINERARY */}
        <div className="space-y-10">

          {/* DAY CARD */}
          {[1, 2, 3].map((day) => (
            <div
              key={day}
              className="bg-white rounded-2xl shadow-lg p-6"
            >
              <h3 className="text-2xl font-semibold text-gray-900 mb-4">
                Day {day}
              </h3>

              <div className="space-y-4">
                {[1, 2, 3].map((activity) => (
                  <div
                    key={activity}
                    className="flex items-start gap-4 border-b pb-4 last:border-none"
                  >
                    <Clock className="mt-1 text-gray-400 w-5 h-5" />
                    <div>
                      <h4 className="font-medium text-gray-800">
                        Activity placeholder
                      </h4>
                      <p className="text-sm text-gray-500">
                        Short description of the activity goes here.
                      </p>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          ))}
        </div>

        {/* ACTIONS */}
        <div className="flex justify-center mt-16 pb-20">
          <button
            className="group flex items-center gap-2 px-6 py-3 rounded-xl
                       bg-[#527a7a] text-white font-medium
                       hover:bg-[#446565] transition shadow-md"
          >
            <RefreshCcw className="w-4 h-4 group-hover:rotate-180 transition-transform duration-500" />
            Regenerate Plan
          </button>
        </div>

      </div>
    </div>
  );
}
