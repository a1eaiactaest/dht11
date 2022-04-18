import React from 'react';
import { useParams } from 'react-router-dom';

import Header from '../shared/components/Header';

function StationHomepage(){
  const { station } = useParams();
  return (
    <main>
      <Header label={`Station: ${station} dashboard.`} />
    </main>
  );
};

export default StationHomepage;