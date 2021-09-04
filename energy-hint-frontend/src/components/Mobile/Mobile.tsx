import React from "react";
import styles from "./Mobile.module.css";

type Props = {
  children: React.ReactNode;
};

const MobileContainer = ({ children }: Props) => {
  return (
    <div className={styles.page}>
      <div className={styles.topBar} />
      <div className={styles.container}>{children}</div>
    </div>
  );
};

export default MobileContainer;
