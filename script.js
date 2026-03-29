const generateBtn = document.getElementById("generateBtn");
const promptInput = document.getElementById("prompt");
const outputArea = document.getElementById("output");

generateBtn.addEventListener("click", async () => {
    const prompt = promptInput.value;
    outputArea.textContent = "Generating...";

    try {
        // Example: call your backend API that runs Gizmoz
        const response = await fetch("/api/generate", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ prompt })
        });

        const data = await response.json();
        outputArea.textContent = data.output;
    } catch (err) {
        outputArea.textContent = "Error: " + err.message;
    }
});
