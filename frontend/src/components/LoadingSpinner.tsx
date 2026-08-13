"use client";

import { useEffect, useState } from "react";
import "./LoadingSpinner.css";

const statusMessages = [
  "Analyzing financials...",
  "Gathering news insights...",
  "Evaluating industry trends...",
  "Assessing risk factors...",
  "Analyzing competitors...",
  "Generating investment memo...",
  "Synthesizing recommendations...",
  "Almost there...",
];

export default function LoadingSpinner() {
  const [statusIndex, setStatusIndex] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setStatusIndex((prev) => {
        if (prev < statusMessages.length - 1) {
          return prev + 1;
        }
        return prev;
      });
    }, 12000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gradient-to-br from-blue-50 to-indigo-50 dark:from-slate-900 dark:to-slate-800">
      <div className="space-y-8 text-center">
        {/* Spinning Loader */}
        <div className="flex justify-center">
          <div className="loader"></div>
        </div>

        {/* Company Analysis Header */}
        <h2 className="text-3xl font-bold text-gray-900 dark:text-white">
          Analyzing Investment Opportunity
        </h2>

        {/* Status Messages */}
        <div className="h-8 flex items-center justify-center">
          <p className="text-lg text-indigo-600 dark:text-indigo-400 font-medium animate-pulse">
            {statusMessages[statusIndex]}
          </p>
        </div>

        {/* Progress Bar */}
        <div className="w-80 h-3 bg-gray-200 dark:bg-gray-700 rounded-full overflow-hidden mx-auto">
          <div className="h-full bg-gradient-to-r from-indigo-500 to-blue-500 progress-bar"></div>
        </div>

        {/* Subtext */}
        <p className="text-sm text-gray-500 dark:text-gray-400 mt-4">
          This may take 60-90 seconds as we gather and analyze comprehensive data...
        </p>
      </div>
    </div>
  );
}
