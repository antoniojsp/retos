document.addEventListener("DOMContentLoaded", function () {
    const dropdown = document.getElementById("myDropdown");

    // Load the saved option from localStorage
    const savedOption = localStorage.getItem("selectedOption");
    if (savedOption) {
        dropdown.value = savedOption;
    }

    // Save the selected option to localStorage on change
    dropdown.addEventListener("change", function () {
        localStorage.setItem("selectedOption", dropdown.value);
    });

    // Automatically click the dropdown to show the selected option (if needed)
    // Uncomment the line below if you want to simulate a click
    // dropdown.dispatchEvent(new Event("change"));
});
