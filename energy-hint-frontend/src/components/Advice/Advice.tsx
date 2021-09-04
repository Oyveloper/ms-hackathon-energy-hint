import React from "react";
import { Check, LightningFill, X } from "react-bootstrap-icons";
import { Button, Container } from "react-bootstrap";
import { addShadow, LeftCenterRow, RightCenterRow } from "../styled";
import styles from "./Advice.module.css";

const AdviceContainer = addShadow(Container);

export interface Advice {
  consumption: number;
  timestamp: Date;
  type: string;
}

type Props = {
  advice: Advice;
};

const makeAdviceString = (advice: Advice) => {
  switch (advice.type) {
    case "SPIKE":
      return (
        "Du brukte " + advice.consumption + " kW strøm " + advice.timestamp
      );
  }

  return "En feil har oppstått!";
};

const AdviceCard = ({ advice }: Props) => {
  return (
    <AdviceContainer className={styles.advice}>
      <LeftCenterRow>
        <p>
          <LightningFill className={styles.icon} size={24} />{" "}
          {makeAdviceString(advice)}
        </p>
      </LeftCenterRow>

      <RightCenterRow>
        <Button variant="outline-success">
          <Check size={30} />
        </Button>
        <Button variant="outline-danger">
          <X size={30} />
        </Button>
      </RightCenterRow>
    </AdviceContainer>
  );
};

export default AdviceCard;
