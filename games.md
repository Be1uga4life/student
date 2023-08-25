---
layout: default
title: Student Blog
---

<style>
  body {
      background-color: #171515;
      color: #ffffff;
      animation: fadeInAnimation ease 3s;
      animation-iteration-count: 1;
      animation-fill-mode: forwards;
  }

  h1 {
    position: relative;
    color: rgb(0,255,255);
    font-size: 3rem;
    font-family: Monospace;
  }
</style>
<h1>Games</h1>

## <span style="color: white; font-size: 20px;">Calculator</span>

<div id="calculator">
<div style="max-width: 200px; background-color: #333333; padding: 10px;">
  <input type="text" id="display" disabled>
  <br />
  <button onclick="appendToDisplay('1')">1</button>
  <button onclick="appendToDisplay('2')">2</button>
  <button onclick="appendToDisplay('3')">3</button>
  <button onclick="appendToDisplay('*')">x</button>
  <button onclick="appendToDisplay('+')">+</button>
  <button onclick="appendToDisplay('-')">-</button>
  <br />
  <button onclick="appendToDisplay('4')">4</button>
  <button onclick="appendToDisplay('5')">5</button>
  <button onclick="appendToDisplay('6')">6</button>
  <button onclick="calculate()">=</button>
  <button onclick="appendToDisplay('/')">/</button>
  <button onclick="clearDisplay()">C</button>
  <br />
  <button onclick="appendToDisplay('7')">7</button>
  <button onclick="appendToDisplay('8')">8</button>
  <button onclick="appendToDisplay('9')">9</button>
  <br />
  <button onclick="appendToDisplay('0')">0</button>

</div>

<script>
  let display = document.getElementById('display');

  function appendToDisplay(value) {
    display.value += value;
  }

  function calculate() {
    try {
      display.value = eval(display.value);
    } catch (error) {
      display.value = 'Error';
    }
  }

  function clearDisplay() {
    display.value = '';
  }
</script>

<head>
  <br />
  <h2 span style="color: white; font-size: 20px;">Tic Tac Toe </h2>
  <style>
    .board {
      display: grid;
      grid-template-columns: repeat(3, 100px);
      grid-gap: 2px;
    }
    .cell {
      width: 100px;
      height: 100px;
      border: 1px solid white;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 24px;
      cursor: pointer;
    }
  </style>
</head>
<body>
  <div class="board" id="board">
    <div class="cell"></div>
    <div class="cell"></div>
    <div class="cell"></div>
    <div class="cell"></div>
    <div class="cell"></div>
    <div class="cell"></div>
    <div class="cell"></div>
    <div class="cell"></div>
    <div class="cell"></div>
  </div>

  <script>
    const board = document.getElementById('board');
    const cells = document.querySelectorAll('.cell');
    let currentPlayer = 'X';
    let gameActive = true;

    cells.forEach(cell => {
      cell.addEventListener('click', handleCellClick);
    });

    function handleCellClick(event) {
      const clickedCell = event.target;
      const clickedIndex = Array.from(cells).indexOf(clickedCell);

      if (gameActive && !cells[clickedIndex].textContent) {
        cells[clickedIndex].textContent = currentPlayer;
        checkWin();
        currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
      }
    }

    function checkWin() {
      const winCombinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], // Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], // Columns
        [0, 4, 8], [2, 4, 6]           // Diagonals
      ];

      for (const combination of winCombinations) {
        const [a, b, c] = combination;
        if (cells[a].textContent && cells[a].textContent === cells[b].textContent && cells[a].textContent === cells[c].textContent) {
          gameActive = false;
          alert(`${cells[a].textContent} wins!`);
          break;
        }
      }
    }
  </script>
</body>

<p><p>
<hr>