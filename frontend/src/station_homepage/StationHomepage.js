import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

import Header from '../shared/components/Header';
import Dashboard from './components/Dashboard';

function StationHomepage(){
  const { station } = useParams();
  const [allStations, setAllStations] = useState(false);

  useEffect(() => {
    if (station == "0"){
      setAllStations(true);
    };
  },[]);

  return (
    <main>
      <>
      <Header label={
        allStations ? "All stations dashboard."
        : `Station ${station} dashboard.`
      } />
      </>
      {/*Dashboard component here */}
      <Dashboard />
    </main>
  );
};

export default StationHomepage;