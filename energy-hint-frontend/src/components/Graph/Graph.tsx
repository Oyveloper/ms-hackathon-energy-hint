import React, {useEffect, useMemo, useState} from 'react';
import {scaleBand, scaleLinear} from "@visx/scale";
import {Bar} from "@visx/shape";
import {AxisBottom} from '@visx/axis';
import {Text} from '@visx/text';

type DataPoint = {
  measurementTime: string,
  value: number,
  meteringpointId: string
}

type GraphProps = {
  date: Date,
  meteringPointId: string,
  height: number,
  width: number
}

const Graph = ({date, meteringPointId, height, width}: GraphProps) => {
  const [data, setData] = useState([]);

  useEffect(() => {
    const start = new Date(date.getTime());
    start.setHours(0);
    start.setMinutes(0);

    const end = new Date(date.getTime());
    end.setHours(23);
    end.setMinutes(59);

    const params = {
      'Start': convertDateToString(start),
      'End': convertDateToString(end),
      'MeteringpointId': meteringPointId
    }
    let url = new URL('https://power-hack.azurewebsites.net/Volumes');
    url.search = new URLSearchParams(params).toString();

    fetch(url.toString()).then((response) => response.json()).then((data) => setData(data))
  }, [date, meteringPointId])


  const xMax = 100;
  const xScale = useMemo(
    () =>
      scaleBand<number>({
        range: [0, width],
        domain: data.map(getHour),
      }),
    [data, xMax],
  );

  const maxValue = Math.max(...data.map(getValue));
  const yScale = useMemo(
    () =>
      scaleLinear<number>({
        range: [0, height],
        domain: [0, maxValue],
      }),
    [data, height],
  );

  if (!data.length) {
    return <div>Loading</div>;
  }

  const axisHeight = 30;
  return (
    <svg width={width} height={height}>
      <rect width={width} height={height} fill="url(#teal)" rx={14}/>
      <>
        {data.map((point) => {
          const hour = getHour(point);
          const power = getValue(point);
          const barWidth = xScale.bandwidth();
          const barX = xScale(hour);
          const barHeight = height - yScale(power);
          return (
            <>
              <Text style={{fontSize: 10, fontWeight: 'bold'}} fill={'rgba(246,190,0)'} textAnchor={'middle'} dx={barWidth / 2} x={barX} y={barHeight + 25} width={barWidth}>{Math.round(power * 100) / 10 + 'W'}</Text>
              <Bar
                key={`bar-${hour}`}
                x={barX}
                y={barHeight + axisHeight}
                width={barWidth}
                height={height}
                fill='rgba(246,190,0)'
              />
            </>
          );
        })}
        <AxisBottom
          top={height - axisHeight}
          scale={xScale}
          tickFormat={(value) => value.toString()}
          hideAxisLine={true}
          hideTicks={true}
          numTicks={xMax}
          tickLabelProps={() => ({
            fill: 'rgba(255, 255, 255, 1)',
            fontSize: 16,
            fontWeight: 'bold',
            textAnchor: 'middle',
          })}
        />
      </>
    </svg>
  );
}

const convertDateToString = (date: Date): string => {
  return date.getDay() + '/' + date.getMonth() + '/' + date.getFullYear() + ' ' + date.getHours() + ':' + date.getMinutes();
}

const getHour = (point: DataPoint): number => {
  const dateString = point.measurementTime;
  return parseInt(dateString.split('T')[1].split(':')[0]);
}

const getValue = (point: DataPoint): number => {
  return point.value;
}

export default Graph;