import {BellFill, PieChartFill} from 'react-bootstrap-icons';
import {useHistory, useLocation} from "react-router";
import styles from './BottomNavigation.module.css';

function BottomNavigation() {
  const history = useHistory();
  const path = useLocation().pathname;

  return (
    <div className={styles.bottomNavigation}>
      <div onClick={() => history.push('')} className={path !== '/' ? styles.icon : ''}>
        <BellFill fontSize={'35'}/>
      </div>
      <div onClick={() => history.push('/distribution')}
           className={path !== '/distribution' ? styles.icon : ''}>
        <PieChartFill fontSize={'35'}/>
      </div>
    </div>
  );
}

export default BottomNavigation
