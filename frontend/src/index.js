import { render } from "react-dom";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";

import App from "./App";

import Stations from "./routes/stations";
import Learn from "./routes/learn";
import Data from "./routes/data";
import StationHomepage from "./station_homepage/StationHomepage";


const rootElement = document.getElementById("root");

render(
  <BrowserRouter>
    <Routes>
      <Route 
        path="/" 
        element={
          <App />
        }>
      </Route>

      <Route 
        path="/station_index" 
        element={
          <Stations />
        }>
      </Route>

      <Route 
        path="/stations/:station" 
        element={
          <StationHomepage />
        }>
      </Route>

      <Route 
        path="/data" 
        element={
          <Data />
        }>
      </Route>

      <Route 
        path="/edu" 
        element={
          <Learn />
        }>
      </Route>

      <Route path='*' element={<Navigate to='/' />} />

    </Routes>
  </BrowserRouter>,
  rootElement
);
