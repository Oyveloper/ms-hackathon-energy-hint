import React, {useEffect, useState} from 'react';

type GraphProps = {
  date: Date,
  meteringPointId: string
}

const Graph = ({date, meteringPointId}: GraphProps) => {
  const [dataPoints, setDataPoints] = useState([]);

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

    fetch(url.toString()).then((response) => response.json()).then((data) => setDataPoints(data))
  }, [date, meteringPointId])

  return (
    <div>
      Hei
    </div>
  );
}

const convertDateToString = (date: Date): string => {
  return date.getDay() + '/' + date.getMonth() + '/' + date.getFullYear() + ' ' + date.getHours() + ':' + date.getMinutes();
}

export default Graph;