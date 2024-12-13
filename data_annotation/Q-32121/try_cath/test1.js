function pivotArray(data) {
  const headers = ["Part Number", "Supplier", "Check", "Part Name", "Description", "OE Number"];
  const pivotedData = {};

  for (const row of data) {
    const partNumber = row[0];
    pivotedData[partNumber] = {};

    for (let i = 0; i < headers.length; i++) {
      pivotedData[partNumber][headers[i]] = row[i];
    }
  }

  return pivotedData;
}

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

const pivotedResult = pivotArray(data);
console.log(JSON.stringify(pivotedResult, null, 2));


// Example of accessing a specific part's information:
console.log("\nExample access:")
console.log("Part 1505_310 Description:", pivotedResult["1505_310"]["Description"]);
console.log("Part 1427_13301 Check:", pivotedResult["1427_13301"]["Check"]);
