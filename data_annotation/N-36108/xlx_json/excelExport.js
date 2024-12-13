import * as XLSX from 'xlsx';

function exportJsonToExcel(jsonData, fileName = 'data.xlsx') {
    // 1. Convert JSON data to worksheet
    const ws = XLSX.utils.json_to_sheet(jsonData);

     // 2. Create workbook and append sheet
    const wb = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(wb, ws, "Sheet1");

    // 3. Generate Excel buffer
    const excelBuffer = XLSX.write(wb, { bookType: 'xlsx', type: 'array' });

    // 4. Create Blob
    const data = new Blob([excelBuffer], {
        type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    });

    // 5. Trigger the Download
    const url = window.URL.createObjectURL(data);
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', fileName);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    // Cleanup
     window.URL.revokeObjectURL(url);


}

// Example usage:
//const jsonData = [
//    { name: "Alice", age: 30, city: "New York" },
//    { name: "Bob", age: 25, city: "London" },
//    { name: "Charlie", age: 35, city: "Paris" }
//];
//
//exportJsonToExcel(jsonData, "employees.xlsx");

 // Optional: This export is if you want to use from another file
  export default exportJsonToExcel
