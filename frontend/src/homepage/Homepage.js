import React from 'react';
import MenuElement from './components/MenuElement.js';
import Navbar from '../shared/components/Navbar.js';

const Homepage = (props) => {
  const dirs = [
    ['Home', '/'],
    ['Stations', '/station_index'],
    ['Data', '/data'],
    ['Learn', '/edu'],
    ['About the Project', '/about'],
  ];

  return (
    <>
      <Navbar elements={dirs}/>
    </>
  );
};

export default Homepage;
