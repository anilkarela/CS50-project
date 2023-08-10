window.history.replaceState({}, document.title, window.location.pathname);

const linkHead = document.getElementById("link-head")
const fullUrl = document.getElementById("url-input");
const shortUrl = document.getElementById("custom-input");
const message = document.getElementById("message");
const generatedUrl = document.getElementById("generated-url");

linkHead.innerHTML = window.location.host + "/"

const urlSelected = SHORT;
const receivedMessage = MESSAGE;


const getRandomString = () => {
    const chars = "abcdefghijklmnopqrstuvwxyz0123456789";
    let result = "";

    for (let i = 0; i < 6; i++) {
        const randomIndex = Math.floor(Math.random() * chars.length);
        result += chars.charAt(randomIndex);
    }

    return result;
};


if (urlSelected) {
    fullUrl.value = FULL;
}

shortUrl.value = urlSelected || getRandomString();

if (urlSelected && receivedMessage === "success") {
    generatedUrl.value = window.location.href + urlSelected;
} else {
    generatedUrl.value = "";
    generatedUrl.placeholder = "Generated URL"
}

if (receivedMessage === "taken") {
    message.innerHTML = "The short URL is already taken. Sorry";
} else if (receivedMessage === "success") {
    message.innerHTML = "Short URL created. Copy it and use.";
} else if (receivedMessage === "invalid") {
    message.innerHTML = "Short URL can only contain numbers and letters.";
}

shortUrl.addEventListener("click", () => {
    shortUrl.select();
});

const copyUrl = () => {
    if (urlSelected && generatedUrl.value) {
        document.getElementById("copy-button").innerHTML = "Copied";
        navigator.clipboard.writeText(generatedUrl.value);
    }
};
