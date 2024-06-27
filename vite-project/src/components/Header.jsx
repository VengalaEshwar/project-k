import React from 'react';
const Header = () => {
  return (
    <div className="header-1">
      <div className="header-2">
        <div className="nav-bar-1">
          <div className="nav-bar">
            <div className="logo"></div>
            <a href="#">Home</a>
            <a href="#">Feature</a>
            <a href="#">Tool</a>
            <a href="#">contact</a>
            {/* <a href="#">login</a> */}
          </div>
        </div>
        <div className="header-content-box">
          <div className="header-content-box-left">
            <div className="header-title">NeuroVista</div>
            <p className="header-title-p">
            In every disorder, there is a message from the soul
            </p>
            <p id="carl" className="dancing-script-font-p"> - Carl Jung</p>
          </div>
          <div className="header-content-box-right"></div>
        </div>
      </div>
    </div>
  );
};

export default Header;
