fetch("http://127.0.0.1:5000/chat", {
    method: "POST",
    headers: { 
        "Content-Type": "application/json",
        "a8f947b49cf33dfcca2fc44de3e0bbf88d1acae46ed2655606ab45ac1e46f37f": "a8f947b49cf33dfcca2fc44de3e0bbf88d1acae46ed2655606ab45ac1e46f37f"  // Replace with the correct key
    },
    body: JSON.stringify({ message: userText })
})
.then(response => response.json())
.then(data => {
    appendMessage(data.response, "ai-message");  // Show response in chat
})
.catch(error => {
    appendMessage("⚠ Error: " + error.message, "ai-message");
});
