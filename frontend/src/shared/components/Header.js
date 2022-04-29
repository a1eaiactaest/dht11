import React from 'react';

const Header = (props) => {
  return (
    <h1 className="text-slate-900 block w-full text-center text-5xl font-bold font">{props.label}</h1>
  );
};

export default Header;
