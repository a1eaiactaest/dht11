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
          RERE's purpose is to present issues of urban flora and fauna by creating a network of sensors which monitor environmental conditions.
          </Paragraph>
        </div>
      </div>
      <div className="flex-inline my-[10%]"></div>
    </div>
  );
};

export default Homepage;

