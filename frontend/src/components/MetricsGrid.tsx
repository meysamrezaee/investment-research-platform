interface Props {
  metrics: Record<
    string,
    string | number
  >;
}

export default function MetricsGrid({
  metrics
}: Props) {
  return (
    <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
      {Object.entries(metrics).map(
        ([key, value]) => (
          <div
            key={key}
            className="bg-white dark:bg-darkgraybackground rounded-xl shadow p-4"
          >
            <div className="text-sm text-gray-600 dark:text-gray-300">
              {key
                .replaceAll("_", " ")
                .toUpperCase()}
            </div>

            <div className="font-semibold mt-1 text-gray-900 dark:text-white">
              {value}
            </div>
          </div>
        )
      )}
    </div>
  );
}