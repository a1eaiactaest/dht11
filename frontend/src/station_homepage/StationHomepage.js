import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";

import Hero from "../shared/components/Hero";
import Dashboard from "./components/Dashboard";

function StationHomepage() {
  const { station } = useParams();
  const [allStations, setAllStations] = useState(false);

  useEffect(() => {
    if (station == "0") {
      setAllStations(true);
    }
  }, []);

  console.log(typeof station);
  return (
    <main>
      <>
        <Hero
          header={
            allStations
              ? "All stations dashboard."
              : `Station ${station} dashboard.`
          }
        />
      </>
      <Dashboard station={station} />
    </main>
  );
}

export default StationHomepage;
