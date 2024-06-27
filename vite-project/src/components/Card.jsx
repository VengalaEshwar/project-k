import React from 'react';

const Card = ({ num,title ,content}) => {
  return (
    <div className={`card card-${num}`}>
      <div className="first-content"></div>
      <div className="second-content">
        <span>{title}</span>
        <p className="dancing-script-font-p card-p">
          {content}
        </p>
      </div>
    </div>
  );
};

export default Card;
