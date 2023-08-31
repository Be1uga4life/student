---
layout: default
title: Student Blog
---

<style> body { background-color: #121212; color: #7e92d6; } 
  p{font-family: sans-serif;}
  hr{background-color: #7289da;}
  .color{color:#7289da;}
  body {
    padding: 25px;
    background-color: #282b30;
    color: #7289da;
    font-size: 16px;
    transition-duration: 0.2s;
  }
  hr{background-color: #7289da;}
  .dark-mode {
    background-color: white;
    color: black;
    transition-duration: 0.2s;
  }
  .bar-dark{background-color: black}
  
  .border-dark {
    border: 2px solid black;
  }
  .cells-dark {
    width: 100px;
      height: 100px;
      border: 1px solid black;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 24px;
      cursor: pointer;
  }
  .board {
      display: grid;
      grid-template-columns: repeat(3, 100px);
      grid-gap: 2px;
    }
    .cell {
      width: 100px;
      height: 100px;
      border: 1px solid #7289da;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 24px;
      cursor: pointer;
    }
</style>


<script>
  
var IsLoggedIn1 = "true";
function myFunction() {
  var element = document.body;
  element.classList.toggle("dark-mode");
  var elem = document.querySelectorAll("#border");
  elem.forEach(function(border) {
    border.classList.toggle("border-dark");
    });
  var bars = document.querySelectorAll("#bar");
  bars.forEach(function(bar) {
    bar.classList.toggle("bar-dark");
    });
  var cellz = document.querySelectorAll("#cells");
  cellz.forEach(function(cells) {
    cells.classList.toggle("cell");
    cells.classList.toggle("cells-dark");
    });
}
</script>

<style>
  body {
    padding: 25px;
    background-color: #121212;
    color: #ffffff;
    font-size: 25px;
    transition-duration: 0.2s;
  }
  hr{background-color: #7289da;}
  .dark-mode {
    background-color: white;
    color: black;
    transition-duration: 0.2s;
  }
  .bar-dark{background-color: black}
  
  .border-dark {
    border: 2px solid black;
  }
  .cells-dark {
    width: 100px;
      height: 100px;
      border: 1px solid black;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 24px;
      cursor: pointer;
  }
  .board {
      display: grid;
      grid-template-columns: repeat(3, 100px);
      grid-gap: 2px;
    }
    .cell {
      width: 100px;
      height: 100px;
      border: 1px solid #7289da;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 24px;
      cursor: pointer;
    }
</style>


<script>
  
var IsLoggedIn1 = "true";
function myFunction() {
  var element = document.body;
  element.classList.toggle("dark-mode");
  var elem = document.querySelectorAll("#border");
  elem.forEach(function(border) {
    border.classList.toggle("border-dark");
    });
  var bars = document.querySelectorAll("#bar");
  bars.forEach(function(bar) {
    bar.classList.toggle("bar-dark");
    });
  var cellz = document.querySelectorAll("#cells");
  cellz.forEach(function(cells) {
    cells.classList.toggle("cell");
    cells.classList.toggle("cells-dark");
    });
}
</script>
<p style="font-size:36px;font-weight:bold;"> Games </p>

<hr id="bar">

<p style="font-size:24px;font-weight:bold;"> Calculator </p>

<div id="calculator">
<div style="max-width: 200px; background-color: #424549; padding: 10px;">
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

  <br />
  <hr id="bar">
  <p style="font-size:24px;font-weight:bold;"> Tic Tac Toe </p>  


  <div class="board" id="board">
    <div class="cell" id="cells"></div>
    <div class="cell" id="cells"></div>
    <div class="cell" id="cells"></div>
    <div class="cell" id="cells"></div>
    <div class="cell" id="cells"></div>
    <div class="cell" id="cells"></div>
    <div class="cell" id="cells"></div>
    <div class="cell" id="cells"></div>
    <div class="cell" id="cells"></div>
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