---
layout: default
title: Student Blog
---
# Eric's Blog


Hello! My name is Eric, I am currently a Sophomore enrolled at DNHS. This is my blog dedicated to my AP CSP class

![](images/personal.png)

***
# <span>About me</span>

I was born in Maryland, but I quickly moved to Germany when I was just a few months old. After my 6th birthday we moved to San Diego, where I would spend my time until 5th grade, where we moved back to Germany yet again, where i stayed until 7th grade. For the final time, I moved back to San Diego during the middle of 7th grade.

Computer Science is one of my hobbies, I've always had interest for computer related things such as Python, Cybersecurity, and Linux Systems. 


I also post on Youtube channel from time to time (see link below), and here is my most popular video:

<iframe width="560" height="315" src="https://www.youtube.com/embed/vVOLzD9Wfu0?si=cR5fIrn8T8VcDFL8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<br />

If you have time, feel free to check out my [Github!](https://github.com/Be1uga4life)

***

# <span>Games</span>

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

<h1 span style="color: white; font-size: 20px;">Socials </h1>
<button onclick="window.location.href='https://www.youtube.com/channel/UCpWLvdZNtaNOUF3wfFe1_og'">
  <img src="data:image/jpeg;base64,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" alt="YouTube" style="width: 65px; height: 50px">
</button>


<style>

  body {
      background-color: #171515;
      color: #ffffff;
      animation: fadeInAnimation ease 3s;
      animation-iteration-count: 1;
      animation-fill-mode: forwards;
  }
  @keyframes fadeInAnimation {
      0% {
          opacity: 0;
      }
      100% {
          opacity: 1;
      }
  }

  h1::before {  
  transform: scaleX(0);
  transform-origin: bottom right;
}

h1:hover::before {
  transform: scaleX(1);
  transform-origin: bottom left;
}

h1::before {
  content: " ";
  display: block;
  position: absolute;
  top: 0; right: 0; bottom: 0; left: 0;
  inset: 0 0 0 0;
  background: rgb(0, 0, 0);
  z-index: -1;
  transition: transform .3s ease;
}

h1 {
  position: relative;
  color: rgb(0,255,255);
  font-size: 3rem;
  font-family: Monospace;
}

html {
  block-size: 100%;
  inline-size: 100%;
}

body {
  min-block-size: 100%;
  min-inline-size: 100%;
  margin: 0;
  box-sizing: border-box;
  display: grid;
  place-content: center;
  font-family: system-ui, sans-serif;
}

.block-container {
    padding-top: 1rem;
    padding-bottom: 0rem;
    padding-left: 5rem;
    padding-right: 5rem;
}

@media (orientation: landscape) {
  body {
    grid-auto-flow: column;
  }
}
</style>