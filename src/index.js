let mediaRecorder;
let audioChunks = [];

const startButton = document.getElementById('startButton');
const stopButton = document.getElementById('stopButton');
const statusDisplay = document.getElementById('status');
const audioPlayback = document.getElementById('audioPlayback');
const responseDiv = document.getElementById('response');

navigator.mediaDevices.getUserMedia({ audio: true })
    .then(stream => {
        mediaRecorder = new MediaRecorder(stream);

        mediaRecorder.onstart = () => {
            statusDisplay.textContent = "Status: Recording...";
            audioChunks = [];
        };

        mediaRecorder.ondataavailable = event => {
            audioChunks.push(event.data);
        };

        mediaRecorder.onstop = () => {
            statusDisplay.textContent = "Status: Recording stopped.";
            const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
            const audioURL = URL.createObjectURL(audioBlob);
            audioPlayback.src = audioURL;
            audioPlayback.style.display = 'block';

            // Send the audio to the backend
            const formData = new FormData();
            formData.append('audio', audioBlob, 'uploaded_audio.wav');

            fetch('http://127.0.0.1:5000/process-audio', {
                method: 'POST',
                body: formData,
            })
                .then(response => response.json())
                .then(data => {
                    if (data.error) {
                        responseDiv.textContent = "Error: " + data.error;

                    } else {
                        console.log(data.advice)
                        responseDiv.innerHTML = `
                        <p><strong> Response: </strong> ${data.advice} </p>
                    `;
                    }
                })
                .catch(error => {
                    responseDiv.textContent = "An Error occurred: " + error.message;
                });
        };

        startButton.addEventListener('click', () => {
            mediaRecorder.start();
            startButton.disabled = true;
            stopButton.disabled = false;
        });

        stopButton.addEventListener('click', () => {
            mediaRecorder.stop();
            startButton.disabled = false;
            stopButton.disabled = true;
        });
    })
    .catch(error => {
        alert('Error accessing the, Microphone: ' + error.message);
    });