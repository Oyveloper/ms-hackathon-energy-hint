import React, { useEffect, useState } from "react";
import { Container } from "react-bootstrap";
import AdviceCard from "./Advice";
import styles from "./AdvicePage.module.css";

const AdvicePage = () => {
  const [advice, setAdvice] = useState<string[]>([]);

  useEffect(() => {
    // TODO: Load advice from back-end
  }, []);

  return (
    <Container className={styles.advicePage}>
      <h2>Råd og tips</h2>
      {advice.map((adv, idx) => (
        <AdviceCard key={idx} advice={adv} />
      ))}
    </Container>
  );
};

export default AdvicePage;
