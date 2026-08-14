"use client";

import { useState } from "react";

interface Props {
  onSubmit: (ticker: string) => void;
}

export default function SearchBar({
  onSubmit,
}: Props) {
  const [ticker, setTicker] = useState("");

  const submitTicker = () => {
    const normalizedTicker =
      ticker.trim().toUpperCase();

    if (!normalizedTicker) {
      return;
    }

    onSubmit(normalizedTicker);
  };

  return (
    <div className="w-full max-w-2xl">
      <div className="flex flex-col gap-3 sm:flex-row">
        <div className="relative flex-1">
          <input
            value={ticker}
            onChange={(e) =>
              setTicker(e.target.value)
            }
            onKeyDown={(e) => {
              if (e.key === "Enter") {
                submitTicker();
              }
            }}
            placeholder="Enter ticker symbol"
            maxLength={6}
            autoCapitalize="characters"
            className="w-full rounded-2xl border border-slate-200 bg-white/80 px-5 py-4 text-lg text-slate-900 shadow-sm outline-none transition placeholder:text-slate-400 focus:border-slate-400 focus:ring-4 focus:ring-slate-200/80 dark:border-slate-700 dark:bg-slate-900/80 dark:text-slate-50 dark:placeholder:text-slate-400 dark:focus:border-slate-500 dark:focus:ring-slate-700/60"
          />
        </div>

        <button
          onClick={submitTicker}
          className="rounded-2xl bg-slate-950 px-6 py-4 text-base font-semibold text-white shadow-lg shadow-slate-900/10 transition hover:-translate-y-0.5 hover:bg-slate-800 focus:outline-none focus:ring-4 focus:ring-slate-300 dark:bg-indigo-500 dark:hover:bg-indigo-400 dark:focus:ring-indigo-700/50"
        >
          Analyze
        </button>
      </div>
    </div>
  );
}