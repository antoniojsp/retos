document.addEventListener("DOMContentLoaded", function () {
    // Get references to form elements
    const dateField = document.getElementById("date");
    const messageField = document.getElementById("message");
    const nameField = document.getElementById("name");
    const clearBtn = document.getElementById("clearBtn");
    const submitBtn = document.getElementById("submitBtn");

    // Set the current date in the date field
    dateField.valueAsDate = new Date();

    // Add event listeners to buttons
    clearBtn.addEventListener("click", function () {
        // Clear the form fields
        dateField.value = "";
        messageField.value = "";
        nameField.value = "";
    });

    submitBtn.addEventListener("click", function () {
        // Get the values from the form fields
        const date = dateField.value;
        const message = messageField.value;
        const name = nameField.value;

        // Check if all fields are filled
        if (!date || !message || !name) {
            alert("Please fill all the fields.");
            return;
        }

        // Create a JSON object with the note data
        const note = {
            date,
            message,
            name,
        };

        // Convert the JSON object to a string
        const data = JSON.stringify(note);

        // Create a new Blob object with the JSON data and set the content type to "text/json"
        const file = new Blob([data], { type: "text/json" });

        // Generate a file name with the current date and time
        const fileName = `note_${new Date().toISOString().replace(/[^0-9a-z]/gi, "_")}.json`;

        // Create a URL object (URL.createObjectURL()) from the Blob object (file)
        const url = URL.createObjectURL(file);

        // Create an anchor element (a) with the URL and file name
        const a = document.createElement("a");
        a.href = url;
        a.download = fileName;
        a.style.display = "none";

        // Append the anchor element to the DOM
        document.body.appendChild(a);

        // Click on the anchor element to trigger the file download
        a.click();

        // Remove the anchor element from the DOM after a short delay (1 second)
        setTimeout(function () {
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
        }, 1000);
    });
});