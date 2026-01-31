import React, { useState } from "react";
import { Coffee, Camera, Mountain, Utensils, PartyPopper } from "lucide-react";
import { useNavigate } from "react-router-dom";

export default function TravelStyle() {
  const navigate = useNavigate();

  const [selectedStyles, setSelectedStyles] = useState([]);


  const styles = [
    {
      id: "relaxed",
      title: "Relaxed",
      description: "Slow mornings, cafés, walks, and chill vibes",
      icon: <Coffee className="w-7 h-7" />,
    },
    {
      id: "sightseeing",
      title: "Sightseeing",
      description: "Landmarks, history, museums, must-see spots",
      icon: <Camera className="w-7 h-7" />,
    },
    {
      id: "adventure",
      title: "Adventure",
      description: "Hiking, nature, outdoor activities",
      icon: <Mountain className="w-7 h-7" />,
    },
    {
      id: "food",
      title: "Food Focused",
      description: "Local cuisine, street food, restaurants",
      icon: <Utensils className="w-7 h-7" />,
    },
    {
      id: "nightlife",
      title: "Nightlife",
      description: "Bars, clubs, late nights, social vibes",
      icon: <PartyPopper className="w-7 h-7" />,
    },
  ];

  const toggleStyle = (id) => {
    setSelectedStyles((prev) =>
      prev.includes(id)
        ? prev.filter((s) => s !== id)
        : [...prev, id]
    );
  };

  const [response, setResponse] = useState(null);
  const data = {
    travelStyle: selectedStyles,
  }

  const handleContinue = async () => {
    // Later you’ll pass selectedStyles to backend / next page
    try {
      const res = await fetch("http://127.0.0.1:8000/api/plan-style/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
      });
      const json = await res.json();
      navigate("", {
      state: json,
      
    });
      console.log("Selected travel styles:", selectedStyles);
      setResponse(json);
    } catch (err) {
      console.error(err);
      setResponse({ error: "Failed to submit trip" });
    }
  };


  

  return (
    <div className="min-h-screen bg-[#ac7339]/10 pt-28 px-4">
      <div className="max-w-6xl mx-auto">
        
        {/* HEADER */}
        <div className="text-center mb-14">
          <h1 className="text-4xl font-bold text-gray-900 mb-4">
            Choose Your Travel Style
          </h1>
          <p className="text-gray-700 max-w-2xl mx-auto">
            This helps us divide your days better — from relaxed mornings to
            active afternoons and lively nights.
          </p>
        </div>

        {/* STYLE CARDS */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
          {styles.map((style) => {
            const active = selectedStyles.includes(style.id);

            return (
              <div
                key={style.id}
                onClick={() => toggleStyle(style.id)}
                className={`cursor-pointer rounded-2xl border-2 p-6 transition
                  ${
                    active
                      ? "border-[#ac7339] bg-[#ac7339]/10 shadow-lg"
                      : "border-gray-200 bg-white hover:shadow-md"
                  }
                `}
              >
                <div
                  className={`w-12 h-12 rounded-xl flex items-center justify-center mb-4
                    ${
                      active
                        ? "bg-[#ac7339] text-white"
                        : "bg-gray-100 text-gray-700"
                    }
                  `}
                >
                  {style.icon}
                </div>

                <h3 className="text-xl font-semibold text-gray-900 mb-2">
                  {style.title}
                </h3>
                <p className="text-gray-600 text-sm">
                  {style.description}
                </p>
              </div>
            );
          })}
        </div>

        {/* FOOTER ACTION */}
        <div className="flex justify-center mt-16">
          <button
            onClick={handleContinue}
            disabled={selectedStyles.length === 0}
            className={`px-8 py-3 rounded-xl text-white font-medium transition shadow-md
              ${
                selectedStyles.length === 0
                  ? "bg-gray-400 cursor-not-allowed"
                  : "bg-[#ac7339] hover:bg-[#94632f]"
              }
            `}
          >
            Continue
          </button>
        </div>
      </div>
    </div>
  );
}