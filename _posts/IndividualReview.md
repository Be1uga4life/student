---
title: Week 0 Documentation
layout: base
description: A thorough documentation of Week 0  
permalink: /Blogs/Week1
categories: [C4.9]
tags: [javascript]
---

<style>
    body {
      animation: fadeInAnimation ease 3s;
      animation-iteration-count: 1;
      animation-fill-mode: forwards;
  }

   body { background-color: #121212; color: #ffffff; } 
  hr{background-color: #7289da;}
  .color{color:#7289da;}
  body {
    padding: 25px;
    background-color: #121212;
    color: #ffffff;
    transition-duration: 0.2s;
    font-family: Monospace;
  }
  hr{background-color: #7289da;}

  h1 {
    color: cyan;
  }

  h2 {
    color: cyan;
  }

  code {
    color: cyan;
  }
</style>

## Face Login Screen Documentation
 
The Face Login Screen 

<table>
  <thead>
    <tr>
      <th>Requirements</th>
      <th>Completed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Instructions for input from the user (including user actions that trigger events)</td>
      <td>There is a math question displayed each round. The user can input the answer to the displayed math question into the interactive Answer Box. The code takes this user input, and compares it to a computer solved answer of the question displayed. If the answers are equal, the code generates a number between 2 and 12 to simulate rolling two dice. The player will move forward on the board however many steps generated.</td>
    </tr>
    <tr>
      <td>Use of at least one list (or other collection type) to represent a collection of data that is stored and used to manage program complexity and help fulfill the program’s purpose</td>
      <td>This code assigns a specific price value to each position on the game board. Since the values on the visual board are just for show, we need to be able to access another set of values for calculations. For instance, the second item in the list (1:100) corresponds to the second box or “step” on the visual board, which is valued at 100 dollars. These values align with the visual representation of the board but are primarily used for calculations and algorithms rather than visual display purposes. When accessing to calculate how much money the player or ai earns when they land on a specific box, I call this list instead of the values used for the css display.</td>
    </tr>
    <tr>
      <td>One procedure that contributes to the program’s intended purpose, where you have defined: the procedure’s name, the return type (if necessary), one or more parameters</td>
      <td>Procedure Name (move), parameters: token and steps.</td>
    </tr>
    <tr>
      <td>An algorithm that includes sequencing, selection, and iteration that is in the body of the selected procedure</td>
      <td>Selection: If/Else Statements. Iteration: The setTimeout function introduces a delay between actions, enabling the repetition of certain tasks over time, creating a form of iteration in the program.</td>
    </tr>
    <tr>
      <td>Calls to your student-developed procedure</td>
      <td>Calling move function: move()</td>
    </tr>
    <tr>
      <td>Instructions for output (tactile, audible, visual, or ) based on input and program functionality</td>
      <td>Add instructions for output here.</td>
    </tr>
  </tbody>
</table>

[Go back]({{site.baseurl}}/weeklylog)  