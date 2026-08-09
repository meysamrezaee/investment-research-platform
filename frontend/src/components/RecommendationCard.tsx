interface Props {
  rating: string;
  confidence: number;
  thesis: string;
}

export default function RecommendationCard({
  rating,
  confidence,
  thesis
}: Props) {
  const color =
    rating === "BUY"
      ? "text-green-600"
      : rating === "SELL"
      ? "text-red-600"
      : "text-yellow-600";

  return (
    <div className="bg-white dark:bg-darkgraybackground rounded-2xl shadow p-6">
      <h2 className={`text-3xl font-bold ${color}`}>
        {rating}
      </h2>

      <p className="text-sm text-gray-500 dark:text-gray-300 mt-2">
        Confidence: {confidence}/10
      </p>

      <p className="mt-4 text-gray-700 dark:text-gray-300">
        {thesis}
      </p>
    </div>
  );
}