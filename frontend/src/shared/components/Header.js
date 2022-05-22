import React from "react";

const Header = (props) => {
	return (
		<h1
			className={`text-slate-900 block my-1/2 w-full text-center font-bold z-50 ${props.styleName}`}
		>
			{props.label}
		</h1>
	);
};

export default Header;
