chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.action === "urlChanged") {
    // Send the URL to the background script for checking
    chrome.runtime.sendMessage(
      {
        action: "checkUrl",
        url: message.url,
      },
      (response) => {
        console.log(`URL: ${message.url}, isPhishing: ${response.isPhishing}`);
      }
    );
  }
});
