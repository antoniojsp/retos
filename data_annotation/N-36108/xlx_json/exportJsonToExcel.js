import exportJsonToExcel from './excelExport.js';

const yourData = [
    { name: "Alice", age: 30, city: "New York" },
    { name: "Bob", age: 25, city: "London" },
    { name: "Charlie", age: 35, city: "Paris" }
];


const jsonData =


exportJsonToExcel(yourData, "name_of_file")