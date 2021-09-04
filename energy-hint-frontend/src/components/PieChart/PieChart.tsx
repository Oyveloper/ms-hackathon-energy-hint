import React from "react";
import { Pie } from "@visx/shape";
import { Group } from "@visx/group";
import { scaleOrdinal } from "@visx/scale";

export type Appliance = {
  name: string;
  power: number;
};

type PieChartProps = {
  appliances: Appliance[];
  radius: number;
  padding?: number;
  fontSize?: number;
};

function PieChart({
  appliances,
  radius,
  fontSize = 16,
  padding = 8,
}: PieChartProps) {
  console.log(appliances[0]);
  const getApplianceColor = scaleOrdinal({
    domain: appliances.map((appliance) => appliance.name),
    range: ["#34344A", "#80475E", "#CC5A71", "#FFE066"],
  });
  const getPower = (appliance: Appliance): number =>
    Math.round(appliance.power * 100) / 100;
  return (
    <svg width={radius * 2} height={radius * 2}>
      <Group top={radius + padding} left={radius}>
        <Pie
          data={appliances}
          pieValue={getPower}
          outerRadius={radius - padding}
        >
          {(pie) => {
            console.log(pie);
            return pie.arcs.map((arc, index) => {
              const { name } = arc.data;
              const [centroidX, centroidY] = pie.path.centroid(arc);
              const arcPath = pie.path(arc) || undefined;
              return (
                <g key={`arc-${name}-${index}`}>
                  <path d={arcPath} fill={getApplianceColor(name)} />
                  <text></text>
                  <text
                    x={centroidX}
                    y={centroidY}
                    fill="#ffffff"
                    fontSize={fontSize}
                    fontWeight={"bold"}
                    textAnchor="middle"
                  >
                    {arc.data.name}
                  </text>
                  <text
                    x={centroidX}
                    y={centroidY}
                    fill="#ffffff"
                    fontSize={fontSize}
                    dy={30}
                    fontWeight={"bold"}
                    textAnchor="middle"
                  >
                    {Math.round(arc.data.power) + "Wh"}
                  </text>
                </g>
              );
            });
          }}
        </Pie>
      </Group>
    </svg>
  );
}

export default PieChart;
