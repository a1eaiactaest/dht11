import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

import Hero from '../shared/components/Hero';
import Dashboard from './components/Dashboard';

function StationHomepage(){
  const { station } = useParams();
  const [allStations, setAllStations] = useState(false);

  useEffect(() => {
    if (station == "0"){
      setAllStations(true);
    };
  },[]);

  console.log(typeof(station));
  return (
    <div className='flex flex-col justify-center mx-auto'>
      <>
      <Hero header={
        allStations ? "All stations dashboard."
        : `Station ${station} dashboard.`
      } />
      </>
      <div className='relative mx-[20%]'>
        <Dashboard station={station}/>
      </div>
    </div>
  );
};

export default StationHomepage;