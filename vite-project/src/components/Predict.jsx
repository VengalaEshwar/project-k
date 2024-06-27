import React  from "react";
const Predict = () =>{
    return (
      <div className="predict">
      <form id="audioUploadForm" onSubmit={handleSubmit}>
        <label htmlFor="input-file" id="drop-area" ref={dropAreaRef}>
          <input
            type="file"
            accept="audio/*"
            id="input-file"
            hidden
            ref={inputFileRef}
          />
          <div id="img-view" ref={imageViewRef}>
            <img src="assets/upload.jpg" alt="Upload" />
            <p>
              Drag and drop or click here<br />to upload audio
            </p>
            <span>upload any audio from desktop</span>
          </div>
        </label>
        <button type="submit" className="submit-btn">
          predict
        </button>
      </form>
    </div>
    )
}
export default Predict;