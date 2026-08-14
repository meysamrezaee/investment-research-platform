// frontend/src/app/page.tsx
"use client";

import { useRouter } from "next/navigation";

import SearchBar from "@/components/SearchBar";

const sampleTickers = [
  "AAPL",
  "MSFT",
  "NVDA",
  "AMZN",
];

export default function HomePage() {
  const router = useRouter();

  const analyze = (ticker: string) => {
    router.push(`/analyze?ticker=${ticker}`);
  };

  return (
    <main className="min-h-screen bg-[radial-gradient(circle_at_top,_#f8fafc_0%,_#eef2ff_35%,_#f8fafc_100%)] px-6 py-12 text-slate-900 transition-colors dark:bg-[radial-gradient(circle_at_top,_#020817_0%,_#0f172a_35%,_#020817_100%)] dark:text-slate-50">
      <div className="mx-auto max-w-6xl">
        <div className="mx-auto w-full max-w-5xl rounded-[32px] border border-slate-200 bg-white/80 p-8 shadow-[0_20px_60px_rgba(15,23,42,0.08)] backdrop-blur-sm md:p-12 dark:border-slate-700 dark:bg-slate-900/80 dark:shadow-[0_20px_60px_rgba(2,6,23,0.6)]">
          <div className="mx-auto max-w-[900px] text-center">
            <div className="mb-6 inline-flex items-center rounded-full border border-indigo-200 bg-indigo-50 px-3 py-1 text-sm font-medium text-indigo-700 dark:border-indigo-500/30 dark:bg-indigo-500/10 dark:text-indigo-200">
              AI-powered investment research
            </div>

            <h1 className="mx-auto max-w-full text-[clamp(2.25rem,3.0vw,5.25rem)] font-black leading-[0.95] tracking-[-0.04em] text-slate-950 dark:text-white">
              Know what matters before investing.
            </h1>

            <p className="mx-auto mt-5 max-w-[1100px] text-lg text-slate-600 md:text-xl dark:text-slate-300">
              Compare financial strength, competitive position, and risk in one concise, investor-ready report.
            </p>

            <div className="mt-8 flex justify-center">
              <SearchBar onSubmit={analyze} />
            </div>

            <div className="mt-6 flex flex-wrap items-center justify-center gap-2 text-sm text-slate-500 dark:text-slate-400">
              <span>Popular tickers:</span>
              {sampleTickers.map((ticker) => (
                <button
                  key={ticker}
                  type="button"
                  onClick={() => analyze(ticker)}
                  className="rounded-full border border-slate-200 bg-slate-50 px-3 py-1.5 font-medium text-slate-700 transition hover:border-slate-300 hover:bg-slate-100 dark:border-slate-700 dark:bg-slate-800 dark:text-slate-200 dark:hover:border-slate-600 dark:hover:bg-slate-700"
                >
                  {ticker}
                </button>
              ))}
            </div>
          </div>
        </div>

        <div className="mt-10 grid gap-4 md:grid-cols-3">
          {[
            {
              title: "Fundamental analysis",
              text: "Evaluate revenue quality, profitability, and balance-sheet strength.",
            },
            {
              title: "Competitive edge",
              text: "Review the business moat, sector trends, and market positioning.",
            },
            {
              title: "Risk framing",
              text: "Surface the main catalysts, threats, and conviction drivers in context.",
            },
          ].map((item) => (
            <div
              key={item.title}
              className="rounded-2xl border border-slate-200 bg-white p-5 shadow-sm dark:border-slate-800 dark:bg-slate-900"
            >
              <h2 className="text-lg font-semibold text-slate-900 dark:text-white">
                {item.title}
              </h2>
              <p className="mt-2 text-sm leading-6 text-slate-600 dark:text-slate-300">
                {item.text}
              </p>
            </div>
          ))}
        </div>
      </div>
    </main>
  );
}