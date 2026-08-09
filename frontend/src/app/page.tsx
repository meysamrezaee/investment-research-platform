// frontend/src/app/page.tsx
"use client";

import { useRouter } from "next/navigation";

import SearchBar from "@/components/SearchBar";

export default function HomePage() {
  const router = useRouter();

  const analyze = (
    ticker: string
  ) => {
    router.push(
      `/analyze?ticker=${ticker}`
    );
  };

  return (
    <main className="min-h-screen flex items-center justify-center">
      <div className="space-y-8 text-center">
        <h1 className="text-5xl font-bold">
          Investment Research Platform
        </h1>

        <p className="text-gray-500">
          Analyze any stock and receive
          an investment recommendation.
        </p>

        <SearchBar
          onSubmit={analyze}
        />
      </div>
    </main>
  );
}