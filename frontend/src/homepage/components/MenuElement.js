import React from "react";
import { Link } from "react-router-dom";

import "./MenuElement.css";

const MenuElement = (props) => {
  return (
    <div className="menu-elem">
      <Link to={`${props.href}`}>{props.name}</Link>
    </div>
  );
};

export default MenuElement;
