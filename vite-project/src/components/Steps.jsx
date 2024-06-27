import React from "react";
import VideoFile from '../../assets/parkinsons.mp4'
const Steps = () => {
    return (
        <div className="steps">
          <video  className="video" loop autoPlay muted>
            <source src={VideoFile} />
          </video>
        </div>
    )
}
export default Steps;
{/* <div className="head-steps">Parkinsons Prediction Tool</div>
          <div className="body-steps"></div> */}