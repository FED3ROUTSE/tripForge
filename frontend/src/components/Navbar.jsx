import React from "react";
import whiteLogo1 from"../images/whiteLogo1.png";

export default function Navbar() {
  return (
    <nav className="w-full bg-white backdrop-blur-md shadow-lg py-4 px-6 flex items-center justify-between fixed top-0 left-0 z-50">

      {/* Logo */}
      <a 
        
        href="/" 
        className="text-2xl font-bold text-blue-600 hover:text-blue-700 transition"
      >
        <img src={whiteLogo1} alt="W3Schools.com" width="130" height="10"></img>
      </a>

      {/* Menu */}
      <ul className="flex gap-6">
        <li>
          <a 
            href="/about" 
            className="text-gray-700 hover:text-blue-600 font-medium transition"
          >
            About
          </a>
        </li>

        <li>
          <a 
            href="/contact" 
            className="text-gray-700 hover:text-blue-600 font-medium transition"
          >
            Contact Us
          </a>
        </li>
      </ul>
    </nav>
  );
}
