import React from "react";

const Menu = (props) => {
  const Elements = props.elements.map((x) => <ul key={x}>{x}</ul>);

  return (
    <>
      <nav>{Elements}</nav>
    </>
  );
};

export default Menu;
