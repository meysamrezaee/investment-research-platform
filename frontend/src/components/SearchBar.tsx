"use client";

import { useState } from "react";

interface Props {
  onSubmit: (ticker: string) => void;
}

export default function SearchBar({
  onSubmit
}: Props) {
  const [ticker, setTicker] = useState("");

  return (
    <div className="flex gap-3">
      <input
        value={ticker}
        onChange={(e) => setTicker(e.target.value)}
        placeholder="MSFT"
        className="border rounded-lg px-4 py-2 w-80"
      />

      <button
        onClick={() => onSubmit(ticker)}
        className="bg-black text-white px-4 py-2 rounded-lg"
      >
        Analyze
      </button>
    </div>
  );
}