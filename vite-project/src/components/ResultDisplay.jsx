import React from 'react';


const ResultDisplay = ({ result }) => {

  return (
    <div className="result-display">
      <div className="head"> Result</div>
      <div className={result === 0 ? "negative" : "positive"}>{result==0?"NEGATIVE":"POSITIVE"}</div>
    </div>
  );
};
export default ResultDisplay;
