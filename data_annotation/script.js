let board = [
  ['','',''],
  ['','',''],
  ['','','']
];

let playerTurn = 'red';
const winningConditions = [
  [0, 0, 0], [0, 1, 0], [0, 2, 0],
  [1, 0, 1], [1, 1, 1], [1, 2, 1],
  [2, 0, 2], [2, 1, 2], [2, 2, 2],
  [0, 0, 1], [0, 1, 2], [1, 0, 2],
  [2, 0, 1], [2, 1, 0], [1, 1, 0]
];

function makeMove(row, col) {
    console.log(board);
  if(board[row][col] === '') {
    board[row][col] = playerTurn;
    document.getElementById('tic-tac-toe-board').children[row].children[col].innerText = playerTurn;
    if(checkWin()) {
      setWinner();
      resetBoard();
    } else {
      playerTurn = playerTurn === 'red' ? 'yellow' : 'red';
    }
  }
}

function checkWin() {
  for(let i = 0; i < winningConditions.length; i++) {
    const [a, b, c] = winningConditions[i];
    if(board[a][b] === playerTurn && board[a][b] === board[a][c] && board[a][c] === board[c][b]) {
      return true;
    }
  }
  return false;
}

function setWinner() {
  const winnerText = document.getElementById('winner');
  winnerText.innerText = `Winner is ${playerTurn}!`;
  winnerText.style.display = 'block';
}

function resetBoard() {
  board = [
    ['','',''],
    ['','',''],
    ['','','']
  ];
  playerTurn = 'red';
  const cells = document.getElementsByClassName('cell');
  for(let i = 0; i < cells.length; i++) {
    cells[i].innerText = '';
  }
  document.getElementById('winner').style.display = 'none';
}