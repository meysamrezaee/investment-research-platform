
const backend_url = process.env.NEXT_PUBLIC_BACKEND_URL;
if (!backend_url) {
  throw new Error(
    "Missing NEXT_PUBLIC_BACKEND_URL. Please create frontend/.env.local"
  );
}

export interface ResearchResponse {
  company: string;
  rating: string;
  confidence: number;
  financial_score: number;
  industry_score: number;
  competitive_score: number;
  safety_score: number;
  thesis: string;
  key_metrics: Record<string, string | number>;
  strengths: string[];
  risks: string[];
  upgrade_catalyst: string;
  downgrade_catalyst: string;
  report_file: string;
}

export async function analyzeStock(
  company: string
): Promise<ResearchResponse> {
  const response = await fetch(
    `${backend_url}/research`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        company
      })
    }
  );

  if (!response.ok) {
    throw new Error("Failed to analyze stock");
  }

  return response.json();
}