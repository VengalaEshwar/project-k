let mediaRecorder;
let audioChunks = [];

document.getElementById("recordButton").addEventListener("click", async () => {
  let stream = await navigator.mediaDevices.getUserMedia({ audio: true });
  mediaRecorder = new MediaRecorder(stream);
  mediaRecorder.start();

  mediaRecorder.addEventListener("dataavailable", (event) => {
    audioChunks.push(event.data);
  });

  mediaRecorder.addEventListener("stop", () => {
    const audioBlob = new Blob(audioChunks, { type: "audio/wav" });
    const audioUrl = URL.createObjectURL(audioBlob);
    const audio = document.getElementById("audioPlayback");
    audio.src = audioUrl;

    document.getElementById("uploadButton").disabled = false;
  });

  document.getElementById("recordButton").disabled = true;
  document.getElementById("stopButton").disabled = false;
});

document.getElementById("stopButton").addEventListener("click", () => {
  mediaRecorder.stop();
  document.getElementById("recordButton").disabled = false;
  document.getElementById("stopButton").disabled = true;
});

document.getElementById("uploadButton").addEventListener("click", async () => {
  const audioBlob = new Blob(audioChunks, { type: "audio/wav" });
  const formData = new FormData();
  formData.append("audio", audioBlob, "recorded_audio.wav");

  fetch("http://127.0.0.1:5001/predictparkinsons", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.error) {
        document.getElementById("result").innerText = "Error: " + data.error;
      } else {
        document.getElementById("result").innerText =
          "Prediction: " + data.prediction;
      }
    })
    .catch((error) => {
      document.getElementById("result").innerText = "Error: " + error.message;
    });

  // Reset for next recording
  audioChunks = [];
  document.getElementById("uploadButton").disabled = true;
});