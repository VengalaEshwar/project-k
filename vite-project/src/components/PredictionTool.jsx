import React, { useState, useRef, useEffect } from "react";
import Steps from './Steps';
import ResultDisplay from "./ResultDisplay";
import Loader from './Loader';
const PredictionTool = () => {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null); // State to hold the prediction result
  const inputFileRef = useRef(null);
  const imageViewRef = useRef(null);
  const dropAreaRef = useRef(null);

  useEffect(() => {
    const inputFile = inputFileRef.current;
    const imageView = imageViewRef.current;
    const dropArea = dropAreaRef.current;

    const uploadImage = () => {
      if (inputFile.files && inputFile.files[0]) {
        const audioLink = URL.createObjectURL(inputFile.files[0]);
        imageView.style.backgroundImage = `url(assets/audio.png)`;
        imageView.textContent = "";
        imageView.style.border = 0;
        const btn = document.querySelector(".submit-btn");
        btn.style.zIndex = 5;
      }
    };

    const handleDragOver = (e) => {
      e.preventDefault();
    };

    const handleDrop = (e) => {
      e.preventDefault();
      inputFile.files = e.dataTransfer.files;
      setFile(inputFile.files[0]);
      uploadImage();
    };

    inputFile.addEventListener("change", (event) => {
      setFile(event.target.files[0]);
      uploadImage();
    });

    dropArea.addEventListener("dragover", handleDragOver);
    dropArea.addEventListener("drop", handleDrop);

    return () => {
      inputFile.removeEventListener("change", uploadImage);
      dropArea.removeEventListener("dragover", handleDragOver);
      dropArea.removeEventListener("drop", handleDrop);
    };
  }, []);

  const handleSubmit = async (event) => {
    event.preventDefault();
    console.log("Submit event listener triggered");
  
    if (!file) {
      console.error("No file selected");
      return;
    }
  
    const formData = new FormData();
    formData.append("audioFile", file);
  
    try {
      setMethod(<Loader/>);
      const response = await fetch("http://127.0.0.1:5001/predictparkinsons", {
        method: "POST",
        body: formData,
      });
  
      if (!response.ok) {
        throw new Error(`HTTP error status: ${response.status}`);
      }
  
      const data = await response.json();
      setResult(data.prediction); // Assuming the response contains a 'prediction' field
      console.log("Received response:", data.prediction);
      method = setMethod(<ResultDisplay result={data.prediction} />);
    } catch (error) {
      console.error("Fetch error:", error);
    }
  };
  
  let [method,setMethod] = useState(<Steps/>);
  return (
    <div className="product-outer">
      <div className="product">
        {method}
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
      </div>
    </div>
  );
};

export default PredictionTool;
