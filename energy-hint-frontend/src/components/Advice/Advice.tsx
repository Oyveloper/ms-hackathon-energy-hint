import React, { useState } from "react";
import { Check, LightningFill, X } from "react-bootstrap-icons";
import { Button, Col, Container } from "react-bootstrap";
import { addShadow, LeftCenterRow, RightCenterRow } from "../styled";
import styles from "./Advice.module.css";

const AdviceContainer = addShadow(Container);

export interface Advice {
  consumption: number;
  timestamp: Date;
  type: string;
}

export interface HighDailyAdvice extends Advice {
  average: number;
}

type Props = {
  advice: Advice;
};

const round = (num: number) => {
  return Math.round((num + Number.EPSILON) * 100) / 100;
};

const getDate = (date: Date) => {
  const _date = new Date(date);
  return new Date(
    Date.UTC(_date.getFullYear(), _date.getMonth(), _date.getDate())
  );
};

const formatDate = (date: Date) => {
  let seconds = Math.floor((Date.now() - date.valueOf()) / 1000);
  let interval = seconds / 2592000;
  if (interval > 1) {
    return " på " + date.toLocaleDateString();
  }

  interval = seconds / 86400;
  if (interval > 1) {
    return "for " + Math.floor(interval) + " dager siden";
  }

  return "i går";
};

const makeAdviceString = (advice: Advice) => {
  switch (advice.type) {
    case "SPIKE":
      return (
        "Du brukte " +
        round(advice.consumption) +
        " kWh strøm " +
        advice.timestamp
      );
    case "DAILY":
      const daily = advice as HighDailyAdvice;
      const percent = advice.consumption / daily.average;
      return (
        "Du brukte " +
        round(advice.consumption) +
        " kWh " +
        formatDate(getDate(advice.timestamp)) +
        ". Dette er " +
        Math.round(percent * 100) +
        "% av normal bruk."
      );
  }

  return "En feil har oppstått!";
};

const AdviceCard = ({ advice }: Props) => {
  const [hidden, setHidden] = useState<boolean>(false);

  const hide = () => setHidden(true);

  return hidden ? null : (
    <AdviceContainer className={styles.advice}>
      <LeftCenterRow>
        <Col xs={1}>
          <LightningFill className={styles.icon} size={24} />
        </Col>
        <Col>
          <p>{makeAdviceString(advice)}</p>
        </Col>
      </LeftCenterRow>

      <RightCenterRow>
        <Button onClick={hide} variant="outline-success">
          <Check size={30} />
        </Button>
        <Button onClick={hide} variant="outline-danger">
          <X size={30} />
        </Button>
      </RightCenterRow>
    </AdviceContainer>
  );
};

export default AdviceCard;
