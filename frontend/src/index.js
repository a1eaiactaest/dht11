import {render} from "react-dom";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";

import App from "./App";

import Stations from "./routes/stations";
import Education from "./routes/education";
import About from "./routes/about";
import Data from "./routes/data";


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
        path="/stations" 
        element={
          <Stations />
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
          <Education />
        }>
      </Route>

      <Route 
        path="/about" 
        element={
          <About />
        }>
      </Route>

      <Route path='*' element={<Navigate to='/' />} />

    </Routes>
  </BrowserRouter>,
  rootElement
);
