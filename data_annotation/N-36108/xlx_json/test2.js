const XLSX = require('xlsx');

const jsonData = [
    { name: "Alice", age: 30, city: "New York" },
    { name: "Bob", age: 25, city: "London" },
    { name: "Charlie", age: 35, city: "Paris" }
];

const exportToExcel = (jsonData, fileName = 'data.xlsx') => {
    // Step 1: Convert JSON to worksheet
    const ws = XLSX.utils.json_to_sheet(jsonData);

    // Step 2: Create a new workbook and add the worksheet to it
    const wb = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(wb, ws, 'Sheet1');

    // Step 3: Write the workbook to a buffer
    const excelBuffer = XLSX.write(wb, { bookType: 'xlsx', type: 'array' });

    // Step 4: Convert the buffer to a Blob and create a download link
    const data = new Blob([excelBuffer], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
    const url = window.URL.createObjectURL(data);
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', fileName); // Name the file
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
};

// Call the function with your JSON data
exportToExcel(jsonData);