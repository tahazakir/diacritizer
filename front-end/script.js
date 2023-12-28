function diacritizeText() {
    var inputText = document.getElementById("inputText").value;

    var dataToSend = JSON.stringify({ text: inputText });

    fetch('http://127.0.0.1:5000/diacritize', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: dataToSend
    })
    .then(response => response.json())
    .then(data => {
        // Display the diacritized text in the output 
        document.getElementById("outputText").value = data.diacritized_text;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function copyText() {
    var copyText = document.getElementById("outputText").value;
    navigator.clipboard.writeText(copyText)
        .then(() => {
            console.log('Text copied to clipboard');
        })
        .catch(err => {
            console.error('Failed to copy text: ', err);
        });
}
