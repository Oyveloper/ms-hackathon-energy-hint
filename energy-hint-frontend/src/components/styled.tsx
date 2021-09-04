import React, { FunctionComponent } from "react";
import { Container, Row, Spinner } from "react-bootstrap";
import styled from "styled-components";

/**
 * Simple spinner for when something is loading
 *
 * @param props - The props
 */
export const DefaultSpinner: FunctionComponent = (props) => {
    return (
        <Spinner as="span" animation="border" size="sm" role="status" aria-hidden="true">
            <span className="sr-only">{props.children}</span>
        </Spinner>
    );
};


/**
 * Creates a styled component with a box shadow
 *
 * @param comp - The component
 */
export const addShadow = (comp: React.ComponentType<any>): any => {
    return styled(comp)`
      border-radius: 5px;
      box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    `;
};

/**
* A {@link Container} with a box-shadow
*/
export const ShadowedContainer = addShadow(Container);

/**
 * A {@link Row} (CSS Flexbox) with all components both vertically
 * and horizontally centered.
 */
export const CenteredRow = styled(Row)`
  justify-content: center;
  align-items: center;
`;

/**
 * A {@link Row} (CSS Flexbox) with all components vertically centered
 * and horizontally left-aligned.
 */
export const LeftCenterRow = styled(Row)`
  justify-content: flex-start;
  align-items: center;
`;

/**
 * A {@link Row} (CSS Flexbox) with all components vertically centered
 * and horizontally right-aligned.
 */
export const RightCenterRow = styled(Row)`
  justify-content: flex-end;
  align-items: center;
`;

/**
 * A {@link Row} (CSS Flexbox) with all components vertically centered
 * and horizontally spaced out.
 */
export const SpaceBetweenCenterRow = styled(Row)`
 justify-content: space-between;
 align-items: center;
`;
