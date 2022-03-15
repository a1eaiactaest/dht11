import React from "react";

import './MenuElement.css';

const MenuElement = (props) => {
  return (
    <ul><a href={props.href} className={`menu-elem`}>{props.name}</a></ul>
  );
}

export default MenuElement;
