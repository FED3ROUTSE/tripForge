import { useLocation } from "react-router-dom";
import { MapPin, Calendar, DollarSign, Clock, SunSnow, ArrowDown } from "lucide-react";
import { useEffect, useRef, useState } from "react";

function FadeInSection({ children, delay = 0 }) {
  const ref = useRef(null);
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setVisible(true);
          observer.disconnect();
        }
      },
      { threshold: 0.15 }
    );

    if (ref.current) observer.observe(ref.current);

    return () => observer.disconnect();
  }, []);

  return (
    <div
      ref={ref}
      className={`
        transition-all duration-700 ease-out
        ${visible ? "opacity-100 translate-y-0" : "opacity-0 translate-y-6"}
      `}
      style={{ transitionDelay: `${delay}ms` }}
    >
      {children}
    </div>
  );
}

export default function TripSummary() {
  const { state } = useLocation();

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
        {/* TOP CARDS */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          {/* LEFT CARD */}
          <FadeInSection>
            <div className="bg-white rounded-2xl shadow-xl p-8">
              <h2 className="text-3xl font-bold text-gray-900 mb-6 text-center">
                Your Trip Summary
              </h2>

              <div className="space-y-4 text-lg text-gray-700">
                <InfoRow icon={<MapPin />} label="Destination" value={state.destination} />
                <InfoRow icon={<Calendar />} label="Arrival" value={state.arrival} />
                <InfoRow icon={<Calendar />} label="Departure" value={state.departure} />
                <InfoRow icon={<DollarSign />} label="Budget" value={`£${state.budget}`} />
              </div>
            </div>
          </FadeInSection>

          {/* RIGHT CARD */}
          <FadeInSection delay={150}>
            <div className="bg-white rounded-2xl shadow-xl p-8">
              <h2 className="text-3xl font-bold text-gray-900 mb-6 text-center">
                Your Trip Insights
              </h2>

              <div className="space-y-4 text-lg text-gray-700">
                <InfoRow
                  icon={<Clock />}
                  label="Duration"
                  value={`${state.duration_days} days`}
                />
                <InfoRow
                  icon={<DollarSign />}
                  label="Daily Budget"
                  value={`£${state.daily_budget}/day`}
                />
                <InfoRow
                  icon={<DollarSign />}
                  label="Currency"
                  value={`${state.currency.code} – ${state.currency.name} (${state.currency.symbol})`}
                />
                <InfoRow
                  icon={<SunSnow />}
                  label="Season"
                  value={state.season_label}
                />
              </div>
            </div>
          </FadeInSection>
        </div>

        {/* QUICK FACTS BUTTON */}
        <FadeInSection delay={300}>
          <div className="mt-8 flex justify-center">
            <button
              onClick={() =>
                document
                  .getElementById("quick-facts")
                  ?.scrollIntoView({ behavior: "smooth", 
                  })
              }
              className="group flex items-center gap-2 px-5 py-2.5 rounded-xl bg-white shadow-sm text-black text-sm font-medium hover:shadow-md transition"
            >
              <span>Quick Facts</span>
              <ArrowDown className="w-4 h-4 group-hover:translate-y-1 transition-transform" />
            </button>
          </div>
        </FadeInSection>

        {/* QUICK FACTS */}
        <div
          className="relative z-10 max-w-6xl mx-auto mt-72 pb-24"
        >
          {/* CITY HERO */}
{state.city_photo && (
  <FadeInSection>
    <div className="mb-16">
      <div className="relative overflow-hidden rounded-2xl shadow-xl">

        {/* IMAGE */}
        <img
          src={state.city_photo.url}
          alt={state.destination}
          className="w-full h-[420px] object-cover"
        />

        {/* Dark overlay for title */}
        <div className="absolute inset-0 bg-black/30 flex items-end">
          <h3 className="text-white text-3xl font-semibold p-6">
            {state.destination}
          </h3>
        </div>

        {/* Attribution bar — attached to bottom */}
        <div className="absolute bottom-0 left-0 w-full px-4 py-2 flex justify-end rounded-b-2xl">
          <a
            href={state.city_photo.link}
            target="_blank"
            rel="noopener noreferrer"
            className="text-xs text-white hover:text-gray-200 transition"
          >
            Photo by {state.city_photo.author} on Unsplash
          </a>
        </div>

      </div>
    </div>
  </FadeInSection>
)}


          {/* ATTRACTIONS */}
          <Section title="Popular Attractions">
            {Object.entries(state.attraction_photos).map(
              ([name, photo], index) => (
                <FadeInSection key={name} delay={index * 120}>
                  <PhotoCard title={name} photo={photo} />
                </FadeInSection>
              )
            )}
          </Section>

          {/* FOOD */}
          <Section title="Local Cuisine">
            {Object.entries(state.food_photos).map(
              ([name, photo], index) => (
                <FadeInSection key={name} delay={index * 120}>
                  <PhotoCard title={name} photo={photo} />
                </FadeInSection>
              )
            )}
          </Section>
        </div>
      </div>
    </div>
  );
}

/* ---------- SMALL COMPONENTS ---------- */

function InfoRow({ icon, label, value }) {
  return (
    <div className="flex items-center justify-between border-b pb-2">
      <div className="flex items-center gap-2 text-gray-500">
        {icon}
        <span className="font-medium text-gray-700">{label}</span>
      </div>
      <span>{value}</span>
    </div>
  );
}

function Section({ title, children }) {
  return (
    <div className="mb-20">
      <h3 className="text-3xl font-semibold text-gray-900 mb-8">
        {title}
      </h3>
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
        {children}
      </div>
    </div>
  );
}

function PhotoCard({ title, photo }) {
  return (
    <div className="group bg-white rounded-2xl shadow-md overflow-hidden hover:shadow-xl transition">
      <img
        src={photo.url}
        alt={title}
        className="w-full h-52 object-cover"
      />
      <div className="p-4">
        <h4 className="text-lg font-medium text-gray-800">{title}</h4>
        <Attribution photo={photo} />
      </div>
    </div>
  );
}

function Attribution({ photo }) {
  return (
    <a
      href={photo.link}
      target="_blank"
      rel="noopener noreferrer"
      className="block mt-2 text-xs text-gray-500 hover:text-gray-700"
    >
      Photo by {photo.author} on Unsplash
    </a>
  );
}