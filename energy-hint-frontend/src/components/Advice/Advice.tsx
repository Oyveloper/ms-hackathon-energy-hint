import React from "react";
import { Check, LightningFill, X } from "react-bootstrap-icons";
import { Button, Col, Container } from "react-bootstrap";
import { addShadow, LeftCenterRow, RightCenterRow, SpaceBetweenCenterRow } from "../styled";
import styles from "./Advice.module.css";

const AdviceContainer = addShadow(Container);

type Props = {
    advice: String;
}

const AdviceCard = ({ advice }: Props) => {
    return (<AdviceContainer className={styles.advice}>
        <LeftCenterRow>
            <LightningFill className={styles.icon} size={24} />
            <p>{advice}</p>
        </LeftCenterRow>

        <RightCenterRow>
            <Button variant="outline-success">
                <Check size={30} />
            </Button>
            <Button variant="outline-danger">
                <X size={30} />
            </Button>
        </RightCenterRow>
    </AdviceContainer>)
}

export default AdviceCard;