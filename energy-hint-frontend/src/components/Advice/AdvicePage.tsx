import React, { useEffect, useState } from "react";
import { Container } from "react-bootstrap";
import AdviceCard, { Advice } from "./Advice";
import styles from "./AdvicePage.module.css";

// Constant URL and device ID because that's how we roll
const URL = "http://localhost:5000/advice/707057500100175148";

const AdvicePage = () => {
  const [advice, setAdvice] = useState<Advice[]>([]);

  useEffect(() => {
    fetch(URL).then((response) => {
      if (!response.ok) {
        console.error('Something went wrong')
        return;
      }

      response.json().then(setAdvice);
    });
  }, []);

  return (
    <Container className={styles.advicePage}>
      <h2>Varsler og tips</h2>
      {advice.map((adv, idx) => (
        <AdviceCard key={idx} advice={adv} />
      ))}
    </Container>
  );
};

export default AdvicePage;
