import React, { useState } from "react";
import {
  Coffee,
  Camera,
  Mountain,
  Utensils,
  PartyPopper,
  Wallet,
  Gem,
  Backpack,
  Sparkles,
} from "lucide-react";
import { useNavigate, useLocation } from "react-router-dom";

export default function TravelStyle() {
  const navigate = useNavigate();
  const { state } = useLocation();

  const destination = state?.destination;
  const arrival = state?.arrival;
  const departure = state?.departure;
  const budget = state?.budget;
  const format_budget = state?.format_budget;

  /* -------------------- EXPERIENCE STYLES -------------------- */

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
      description: "Bars, clubs, late nights",
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


  const [spendingStyle, setSpendingStyle] = useState(null);

  const spendingOptions = [
    {
      id: "budget",
      title: "Budget",
      description: "Affordable options, good value",
      icon: <Backpack className="w-6 h-6" />,
    },
    {
      id: "balanced",
      title: "Balanced",
      description: "Mix of comfort & value",
      icon: <Wallet className="w-6 h-6" />,
    },
    {
      id: "premium",
      title: "Premium",
      description: "High quality experiences",
      icon: <Sparkles className="w-6 h-6" />,
    },
    {
      id: "luxury",
      title: "Luxury",
      description: "Top-tier restaurants & experiences",
      icon: <Gem className="w-6 h-6" />,
    },
  ];



  const handleContinue = async () => {
    const data = {
      travelStyle: selectedStyles,
      spendingStyle: spendingStyle,  
      destination,
      arrival,
      departure,
      budget,
      format_budget,
    };

    try {
      const res = await fetch("http://127.0.0.1:8000/api/plan-style/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
      });

      const json = await res.json();

      navigate("/travel-plan", {
        state: json,
      });

    } catch (err) {
      console.error(err);
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
            Pick what fits your vibe — and how you like to spend.
          </p>
        </div>

        {/* EXPERIENCE STYLES */}
        <h2 className="text-2xl font-semibold mb-6 text-gray-900">
          What do you want to do?
        </h2>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8 mb-16">
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

        {/* SPENDING BEHAVIOUR */}
        <h2 className="text-2xl font-semibold mb-6 text-gray-900">
          How do you like to spend?
        </h2>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-16">
          {spendingOptions.map((option) => {
            const active = spendingStyle === option.id;

            return (
              <div
                key={option.id}
                onClick={() => setSpendingStyle(option.id)}
                className={`cursor-pointer rounded-2xl border-2 p-5 transition
                  ${
                    active
                      ? "border-[#ac7339] bg-[#ac7339]/10 shadow-lg"
                      : "border-gray-200 bg-white hover:shadow-md"
                  }
                `}
              >
                <div className="mb-3 text-[#ac7339]">
                  {option.icon}
                </div>
                <h3 className="font-semibold text-gray-900">
                  {option.title}
                </h3>
                <p className="text-sm text-gray-600">
                  {option.description}
                </p>
              </div>
            );
          })}
        </div>

        {/* CONTINUE BUTTON */}
        <div className="flex justify-center">
          <button
            onClick={handleContinue}
            disabled={selectedStyles.length === 0 || !spendingStyle}
            className={`px-8 py-3 rounded-xl text-white font-medium transition shadow-md
              ${
                selectedStyles.length === 0 || !spendingStyle
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
