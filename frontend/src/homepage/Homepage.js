import React from 'react';
import MenuElement from './components/MenuElement.js';

const Homepage = (props) => {
  return (
    <React.Fragment>
      <MenuElement href='menu1' name='menu1'/>
      <MenuElement href='menu2' name='menu2'/>
      <MenuElement href='menu3' name='menu3'/>
      <MenuElement href='menu4' name='menu4'/>
    </React.Fragment>

  );
};

export default Homepage;
