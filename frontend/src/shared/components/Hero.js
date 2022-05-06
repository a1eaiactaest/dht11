import {useState, useEffect} from "react";
import Header from "./Header";
import Navbar from "./Navbar";
import { Blob2 } from "../UI/Blobs";

const Hero = (props) => {
  const [showBlob, setShowBlob] = useState(false);

  useEffect(() => {
    if (props.blob){
      setShowBlob(true);
    }
  });

  return (
    <>
      <div className='mx-auto relative mt-5'>
        <Navbar />
      </div>

      { showBlob ?
        <div className='my-40 mb-96 blob-header'>
          <Header label={props.header} styleName='text-9xl'/>
          <Blob2 /> 
        </div>
        : 
        <div className='my-20 blob-header'>
          <Header label={props.header} styleName='text-7xl'/>
        </div>
      }
    </>
  );
};

export default Hero;