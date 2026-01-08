import { useLocation } from "react-router-dom";
import { MapPin, Calendar, DollarSign, Clock, SunSnow, ArrowDown } from "lucide-react";

export default function TripSummary() {
  const { state } = useLocation();
  console.log("TripSummary state:", state);

  if (!state) {
    return (
      <div className="pt-24 flex justify-center">
        <p className="text-gray-600">No trip data available</p>
      </div>
    );
  }

  return (
    <div className="relative min-h-screen w-full bg-gray-50 pt-24 px-4">

      {/* BACKGROUND IMAGE */}
      {state.city_map && (
        <div
          className="fixed inset-0 bg-cover bg-center z-0"
          style={{
            backgroundImage: `url(${state.city_map})`,
            opacity: 0.4,
            filter: "grayscale(100%) brightness(0.6) contrast(1.2)",
          }}
        />
      )}

      {/* CONTENT */}
      <div className="relative z-10 max-w-6xl mx-auto">

        {/* CARDS GRID */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">

          {/* LEFT CARD */}
          <div className="bg-white rounded-2xl shadow-xl p-8 flex flex-col">
            <h2 className="text-3xl font-bold text-gray-900 mb-6 text-center">
              Your Trip Summary
            </h2>

            <div className="space-y-4 text-lg text-gray-700">
              <div className="flex items-center justify-between border-b pb-2">
                <div className="flex items-center gap-2">
                  <MapPin className="w-5 h-5 text-gray-500" />
                  <span className="font-medium">Destination</span>
                </div>
                <span>{state.destination}</span>
              </div>

              <div className="flex items-center justify-between border-b pb-2">
                <div className="flex items-center gap-2">
                  <Calendar className="w-5 h-5 text-gray-500" />
                  <span className="font-medium">Arrival</span>
                </div>
                <span>{state.arrival}</span>
              </div>

              <div className="flex items-center justify-between border-b pb-2">
                <div className="flex items-center gap-2">
                  <Calendar className="w-5 h-5 text-gray-500" />
                  <span className="font-medium">Departure</span>
                </div>
                <span>{state.departure}</span>
              </div>

              <div className="flex items-center justify-between border-b pb-2">
                <div className="flex items-center gap-2">
                  <DollarSign className="w-5 h-5 text-gray-500" />
                  <span className="font-medium">Budget</span>
                </div>
                <span>£{state.budget}</span>
              </div>
            </div>
          </div>

          {/* RIGHT CARD */}
          <div className="bg-white rounded-2xl shadow-xl p-8 flex flex-col text-gray-700">
            <h2 className="text-3xl font-bold text-gray-900 mb-6 text-center">
              Your Trip Insights
            </h2>

            <div className="space-y-4 text-lg">
              <div className="flex items-center justify-between border-b pb-2">
                <div className="flex items-center gap-2">
                  <Clock className="w-5 h-5 text-gray-500" />
                  <span className="font-medium">Duration</span>
                </div>
                <span>{state.duration_days} days</span>
              </div>

              <div className="flex items-center justify-between border-b pb-2">
                <div className="flex items-center gap-2">
                  <DollarSign className="w-5 h-5 text-gray-500" />
                  <span className="font-medium">Daily Budget</span>
                </div>
                <span>
                  £
                  {new Intl.NumberFormat("en-GB", {
                    minimumFractionDigits: 0,
                    maximumFractionDigits: 2,
                  }).format(state.daily_budget)}
                  /day
                </span>
              </div>

              <div className="flex items-center justify-between border-b pb-2">
                <div className="flex items-center gap-2">
                  <DollarSign className="w-5 h-5 text-gray-500" />
                  <span className="font-medium">Local Currency</span>
                </div>
                <span>
                  {state.currency.code} – {state.currency.name} ({state.currency.symbol})
                </span>
              </div>

              <div className="flex items-center justify-between border-b pb-2">
                <div className="flex items-center gap-2">
                  <SunSnow className="w-5 h-5 text-gray-500" />
                  <span className="font-medium">Season</span>
                </div>
                <span>{state.season_label}</span>
              </div>
            </div>
          </div>

        </div>

       {/* QUICK FACTS BUTTON */}
<div className="mt-8 flex justify-center">
  <button
    onClick={() => {
      document
        .getElementById("quick-facts")
        ?.scrollIntoView({ behavior: "smooth" });
    }}
    className="
      group
      flex items-center gap-2
      px-5 py-2.5
      rounded-xl
      bg-white
      shadow-sm
      text-black
      text-sm
      font-medium
      transition-all duration-300
      hover:shadow-md
      hover:-translate-y-0.5
      active:translate-y-0
    "
  >
    <span>Quick Facts</span>

    <ArrowDown
      className="
        w-4 h-4
        transition-transform duration-300
        group-hover:translate-y-1
      "
    />
  </button>
</div>

      </div>
    </div>
  );
}
