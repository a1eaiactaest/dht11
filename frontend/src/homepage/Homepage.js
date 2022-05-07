import React from 'react';
import Header from '../shared/components/Header';
import Hero from '../shared/components/Hero';
import { Paragraph } from '../shared/components/Paragraph';

const Homepage = (props) => {

  return (
    <div className='flex flex-col fade'>
      <Hero header="RERE" blob={true}/>

      <div className="max-w-screen-md mx-auto">
        <div className="relative aspect-video">
          <iframe className="absolute w-full h-full inset-0" src="https://www.youtube.com/embed/u0sql4bx4PI"></iframe>

        </div>

        <div>
          <Header label="About" styleName="text-6xl my-20"></Header>
        </div>

        <div>
          <Paragraph styleName="font-sans text-slate-700 text-base text-center w-fit">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
          </Paragraph>
        </div>
      </div>
      <div className="flex-inline my-[10%]"></div>
    </div>
  );
};

export default Homepage;

