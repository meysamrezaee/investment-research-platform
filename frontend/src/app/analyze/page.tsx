// frontend/src/app/analyze/page.tsx

"use client";

import {
  Suspense,
  useEffect,
  useRef,
  useState,
} from "react";

import { useSearchParams } from "next/navigation";

import {
  analyzeStock,
  ResearchResponse,
} from "@/lib/api";

import RecommendationCard from "@/components/RecommendationCard";
import ScoreBreakdown from "@/components/ScoreBreakdown";
import MetricsGrid from "@/components/MetricsGrid";
import LoadingSpinner from "@/components/LoadingSpinner";

function AnalysisContent() {
  const [data, setData] =
    useState<ResearchResponse | null>(
      null
    );

  const [loading, setLoading] =
    useState(true);

  const searchParams =
    useSearchParams();

  const ticker =
    searchParams.get("ticker");

  const hasRun = useRef(false);

  useEffect(() => {
    if (!ticker) {
      setLoading(false);
      return;
    }

    if (hasRun.current) {
      return;
    }

    hasRun.current = true;

    analyzeStock(ticker)
      .then(setData)
      .finally(() =>
        setLoading(false)
      );
  }, [ticker]);

  if (loading) {
    return <LoadingSpinner />;
  }

  if (!data) {
    return (
      <div className="p-10">
        No data found
      </div>
    );
  }

  return (
    <main className="max-w-6xl mx-auto p-8 space-y-8">
      <h1 className="text-4xl font-bold">
        {data.company}
      </h1>

      <RecommendationCard
        rating={data.rating}
        confidence={data.confidence}
        thesis={data.thesis}
      />

      <ScoreBreakdown
        financial={
          data.financial_score
        }
        industry={
          data.industry_score
        }
        competitive={
          data.competitive_score
        }
        safety={data.safety_score}
      />

      <MetricsGrid
        metrics={data.key_metrics}
      />

      <section className="grid md:grid-cols-2 gap-6">
        <div className="bg-white dark:bg-darkgraybackground shadow rounded-2xl p-6">
          <h2 className="font-bold mb-3">
            Strengths
          </h2>

          <ul className="space-y-2">
            {data.strengths.map((s) => (
              <li key={s}>
                ✅ {s}
              </li>
            ))}
          </ul>
        </div>

        <div className="bg-white dark:bg-darkgraybackground shadow rounded-2xl p-6">
          <h2 className="font-bold mb-3">
            Risks
          </h2>

          <ul className="space-y-2">
            {data.risks.map((r) => (
              <li key={r}>
                ⚠️ {r}
              </li>
            ))}
          </ul>
        </div>
      </section>

      <section className="grid md:grid-cols-2 gap-6">
        <div className="bg-green-50 dark:bg-darkgreenbackground rounded-2xl p-6">
          <h2 className="font-bold">
            Upgrade Catalyst
          </h2>

          <p className="mt-2">
            {
              data.upgrade_catalyst
            }
          </p>
        </div>

        <div className="bg-red-50 dark:bg-darkredbackground rounded-2xl p-6">
          <h2 className="font-bold">
            Downgrade Catalyst
          </h2>

          <p className="mt-2">
            {
              data.downgrade_catalyst
            }
          </p>
        </div>
      </section>
    </main>
  );
}

export default function AnalysisPage() {
  return (
    <Suspense
      fallback={
        <div className="p-10">
          Loading...
        </div>
      }
    >
      <AnalysisContent />
    </Suspense>
  );
}