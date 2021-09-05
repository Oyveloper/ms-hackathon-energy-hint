import { useEffect, useState } from "react";
import { CenteredRow } from "../styled";
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
      <h1>Forbruksfordeling</h1>
      {appliances == null ? (
        <>
          <CenteredRow style={{ marginTop: "10px" }}>
            {/*<Spinner*/}
            {/*  as="span"*/}
            {/*  animation="border"*/}
            {/*  role="status"*/}
            {/*  aria-hidden="true"*/}
            {/*/>*/}
          </CenteredRow>
          <p>Laster data...</p>
        </>
      ) : (
        <PieChart appliances={appliances} radius={200} />
      )}
    </div>
  );
};

export default PieChartPage;
