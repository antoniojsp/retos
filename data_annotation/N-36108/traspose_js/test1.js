function pivotArray(data) {
  // Create an empty object to store the pivoted data.
  const pivotedData = {};

  // Iterate over each sub-array in the data array.
  data.forEach((row) => {
    // The first element in the sub-array is the key.
    const key = row[0];

    // The rest of the elements in the sub-array are the values.
    const values = {
      partNumber: row[1],
      availability: row[2],
      description: row[3],
      details: row[4],
      additionalInfo: row[5],
    };

    // Add the values to the pivoted data object using the key.
    pivotedData[key] = values;
  });

  // Return the pivoted data.
  return pivotedData;
}

// Example data array.
const data = [
  ['1505_310', 'Universal Parts', null, 'Branch-Off Fitting', 'for vacuum line', '08643'],
  ['686_1550439', 'B/E', null, 'Spark Plug', 'Super', null],
  ['111_689', 'B/E', null, 'Bulb', 'for brake, indicator, rear, rear fog and reversing light', null],
  ['107_2243', 'B/E', null, 'Bulb', 'for main and auxiliary headlight', null],
  ['1629_341161', 'B/E', null, 'Pedal Pad', 'for brake pedal', '30777, 10 93 0777'],
  ['3358_587', 'F/B', null, 'Bracket', 'for air filter', null],
  ['1776_258', 'C/T', null, 'Ball Socket', 'for shifting rod', '08715, 10 90 8715'],
  ['1427_13301', 'C/T', '✔', 'Flexible Disc', 'for propshaft', null],
];

// Pivot the data.
const pivotedData = pivotArray(data);

// Log the pivoted data.
console.log(pivotedData);