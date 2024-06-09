//_____________________________________________________________________________________________________________________
// this script is for drag-drop feature
const dropArea = document.getElementById("drop-area");
const inputFile = document.getElementById("input-file");
const imageView = document.getElementById("img-view");
let imageContent = "";
inputFile.addEventListener("change", uploadImage);
function uploadImage() {
  let audioLink = URL.createObjectURL(inputFile.files[0]);
  imageView.style.backgroundImage = `url(assets/audio.png)`;
  imageContent=imageView.textContent;
  imageView.textContent = "";
  imageView.style.border = 0;
  let btn = document.querySelector(".submit-btn");
  btn.style.zIndex = 5;
}

dropArea.addEventListener("dragover", function (e) {
  e.preventDefault();
});
dropArea.addEventListener("drop", function (e) {
  e.preventDefault();
  inputFile.files = e.dataTransfer.files;
  uploadImage();
});

//_____________________________________________________________________________________________________________________
//this script is for functionality of uplaod

let submit =document.querySelector(".submit-btn");
submit.addEventListener("click", async (event) => {
    submit.style.backgroundColor = "#514d4d";
    let form=document.getElementById("audioUploadForm");
    // event.preventDefault();
    const formData = new FormData(form);
    console.log("started the  submit");
    fetch("http://127.0.0.1:5001/predictparkinsons", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.error) {
        //   document.getElementById("result").innerText = "Error: " + data.error;
        console.log("fetched the data got error");
        } else {
        //   document.getElementById("result").innerText =
        //     "Prediction: " + data.prediction;
        console.log("fetched the data");
        }
        
      })
      .catch((error) => {
        // document.getElementById("result").innerText = "Error: " + error.message;
        console.log("fetched the data got error");
      });
  });