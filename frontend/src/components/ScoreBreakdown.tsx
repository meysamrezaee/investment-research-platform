interface Props {
  financial: number;
  industry: number;
  competitive: number;
  safety: number;
}

export default function ScoreBreakdown({
  financial,
  industry,
  competitive,
  safety
}: Props) {
  const Row = ({
    label,
    value
  }: {
    label: string;
    value: number;
  }) => (
    <div>
      <div className="flex justify-between mb-1">
        <span>{label}</span>
        <span>{value}/10</span>
      </div>

      <div className="bg-gray-200 h-3 rounded">
        <div
          className="bg-indigo-500 h-3 rounded"
          style={{
            width: `${value * 10}%`
          }}
        />
      </div>
    </div>
  );

  return (
    <div className="bg-white dark:bg-darkgraybackground rounded-2xl shadow p-6 space-y-4">
      <Row
        label="Financial"
        value={financial}
      />

      <Row
        label="Industry"
        value={industry}
      />

      <Row
        label="Competitive"
        value={competitive}
      />

      <Row
        label="Safety"
        value={safety}
      />
    </div>
  );
}