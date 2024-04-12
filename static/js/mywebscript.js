
function displayResponse(response) {
    if (typeof response !== 'string') {
        console.error('Invalid response type');
        return;
    }

    const sanitizedResponse = escapeHTML(response);
    const formattedResponse = sanitizedResponse.replace(/\n/g, '<br>');
    document.getElementById("system_response").innerHTML = formattedResponse;
}

function escapeHTML(text) {
    return text.replace(/[&<>"']/g, function(match) {
        switch(match) {
            case "&":
                return "&amp;";
            case "<":
                return "&lt;";
            case ">":
                return "&gt;";
            case "\"":
                return "&quot;";
            case "'":
                return "&#x27;";
            default:
                return match;
        }
    });
}

let RunSentimentAnalysis = () => {
    showLoading();
    textToAnalyze = document.getElementById("textToAnalyze").value;

    if (typeof textToAnalyze !== 'string') {
        console.error('Invalid input type');
        hideLoading();
        return;
    }

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            displayResponse(xhttp.responseText);
            hideLoading();
        }
    };

    const encodedText = encodeURIComponent(textToAnalyze);

    xhttp.open("GET", "emotionDetector?textToAnalyze=" + encodedText, true);
    xhttp.send();
};