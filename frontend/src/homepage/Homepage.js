import React from 'react';
import Navbar from '../shared/components/Navbar';
import Header from '../shared/components/Header';
import { Paragraph } from '../shared/components/Paragraph';
import { Blob1, Blob2, Blob3 } from '../shared/UI/Blobs';

const Homepage = (props) => {
  const dirs = [
    ['Home', '/'],
    ['Stations', '/station_index'],
    ['Data', '/data'],
    ['Learn', '/edu'],
    ['About the Project', '/about'],
  ];

  return (
    <div className='flex flex-col'>
      <div className='mx-auto relative mt-5'>
        <Navbar elements={dirs}/>
      </div>

      <div className='my-40 mb-96 blob-header'>
        <Header label="RERE" styleName='text-9xl'/>
        <Blob2 />
      </div>

      <div>
        <Header label="About" styleName="text-6xl my-20"></Header>
      </div>

      <div className="mx-[20%]">
        <Paragraph styleName="font-sans text-slate-700 text-base text-center w-fit">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </Paragraph>
      </div>
    </div>
  );
};

export default Homepage;
