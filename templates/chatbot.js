// chatbot.js

function sendChatMessage() {
    const userMessage = document.getElementById('userMessage').value;
    const chatbox = document.getElementById('chatbox');

    // Display user's message
    chatbox.innerHTML += `<p><strong>You:</strong> ${userMessage}</p>`;

    // Determine emotion based on user's message (simplified for the example)
    const detectedEmotion = detectEmotion(userMessage);

    // Generate emotional response
    const chatbotResponse = generateResponse(detectedEmotion);

    // Display chatbot's response
    chatbox.innerHTML += `<p><strong>Chatbot:</strong> ${chatbotResponse}</p>`;

    // Clear input field
    document.getElementById('userMessage').value = '';
}

function detectEmotion(userMessage) {
    // Simplified emotion detection (you can replace this with more advanced techniques)
    const positiveKeywords = ['happy', 'joy', 'excited'];
    const negativeKeywords = ['sad', 'angry', 'frustrated'];

    const lowercaseMessage = userMessage.toLowerCase();

    if (positiveKeywords.some(keyword => lowercaseMessage.includes(keyword))) {
        return 'happy';
    } else if (negativeKeywords.some(keyword => lowercaseMessage.includes(keyword))) {
        return 'sad';
    } else {
        return 'neutral';
    }
}

function generateResponse(emotion) {
    // Generate responses based on detected emotion
    switch (emotion) {
        case 'happy':
            return 'I\'m glad to hear that! 😊';
        case 'sad':
            return 'I\'m sorry you\'re feeling that way. 😢';
        default:
            return 'Interesting. Tell me more.';
    }
}
