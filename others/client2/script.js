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
  imageContent = imageView.textContent;
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
document.addEventListener("DOMContentLoaded", () => {
    console.log("DOM fully loaded and parsed");
    
    let form = document.querySelector("#audioUploadForm");
    if (!form) {
        console.error("Form element not found");
        return;
    }

    form.addEventListener("submit", async (event) => {
        event.preventDefault();  // Prevent the default form submission action
        console.log("Submit event listener triggered");

        let submit = document.querySelector(".submit-btn");
        if (submit) {
            submit.style.backgroundColor = "#514d4d";
        } else {
            console.error("Submit button not found");
        }

        const formData = new FormData(form);
        const fileInput = document.getElementById("input-file");
        if (!fileInput) {
            console.error("File input element not found");
            return;
        }

        const file = fileInput.files[0];
        if (file) {
            formData.append("audioFile", file);
        } else {
            console.error("No file selected");
            return;
        }

        console.log("Started the submit");

        try {
            let response = await fetch("http://127.0.0.1:5001/predictparkinsons", {
                method: "POST",
                body: formData,
            });

            if (!response.ok) {
                throw new Error(`HTTP error status: ${response.status}`);
            }

            let data = await response.json();
            console.log("Received response:", data);
            // Handle the response data here
        } catch (error) {
            console.error("Fetch error:", error);
        }
    });
});
