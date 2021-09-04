import { useEffect, useState } from "react";
import PieChart, { Appliance } from "./PieChart";

const PieChartPage: React.FC = () => {
  const [appliances, setAppliances] = useState<Appliance[] | null>(null);

  useEffect(() => {
    fetch("http://localhost:5000/distrobution")
      .then((result) => result.json())
      .then((result) => {
        if (result) {
          setAppliances(result as Appliance[]);
        }
      });
  }, []);

  return (
    <div>
      <h1>Distrobution of powerconsumption</h1>
      {appliances == null ? (
        <h1>Loading…</h1>
      ) : (
        <PieChart appliances={appliances} radius={200} />
      )}
    </div>
  );
};

export default PieChartPage;
