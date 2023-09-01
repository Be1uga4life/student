---
layout: default
title: Student Blog
---


<style>
  #loader-wrapper {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1001;
}
#loader-wrapper .loader-section {
  position: fixed;
  top: 0;
  width: 51%;
  height: 100%;
  background: #000;
  z-index: 1000;
  -webkit-transform: translateX(0);
          transform: translateX(0);
}
#loader-wrapper .loader-section.section-left {
  left: 0;
}
#loader-wrapper .loader-section.section-right {
  right: 0;
}
#loader {
  display: block;
  position: relative;
  left: 50%;
  top: 50%;
  width: 150px;
  height: 150px;
  margin: -75px 0 0 -75px;
  border-radius: 50%;
  border: 3px solid transparent;
  border-top-color: #3498db;
  -webkit-animation: spin 2s linear infinite;
          animation: spin 2s linear infinite;
  z-index: 99999;
}
#loader:before {
  content: "";
  position: absolute;
  top: 5px;
  left: 5px;
  right: 5px;
  bottom: 5px;
  border-radius: 50%;
  border: 3px solid transparent;
  border-top-color: cyan;
  -webkit-animation: spin 3s linear infinite;
          animation: spin 3s linear infinite;
}
#loader:after {
  content: "";
  position: absolute;
  top: 15px;
  left: 15px;
  right: 15px;
  bottom: 15px;
  border-radius: 50%;
  border: 3px solid transparent;
  border-top-color: white;
  -webkit-animation: spin 1.5s linear infinite;
          animation: spin 1.5s linear infinite;
}
.loaded #loader-wrapper {
  visibility: hidden;
  -webkit-transform: translateY(-100%);
          transform: translateY(-100%);
  -webkit-transition: all 0.3s 1s ease-out;
  transition: all 0.3s 1s ease-out;
}
.loaded #loader-wrapper .loader-section.section-left {
  -webkit-transform: translateX(-100%);
          transform: translateX(-100%);
  -webkit-transition: all 0.7s 0.3s cubic-bezier(0.645, 0.045, 0.355, 1);
  transition: all 0.7s 0.3s cubic-bezier(0.645, 0.045, 0.355, 1);
}
.loaded #loader-wrapper .loader-section.section-right {
  -webkit-transform: translateX(100%);
          transform: translateX(100%);
  -webkit-transition: all 0.7s 0.3s cubic-bezier(0.645, 0.045, 0.355, 1);
  transition: all 0.7s 0.3s cubic-bezier(0.645, 0.045, 0.355, 1);
}
.loaded #loader {
  opacity: 0;
  -webkit-transition: all 0.3s ease-out;
  transition: all 0.3s ease-out;
}
@-webkit-keyframes spin {
  0% {
    -webkit-transform: rotate(0deg);
            transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(360deg);
            transform: rotate(360deg);
  }
}
@keyframes spin {
  0% {
    -webkit-transform: rotate(0deg);
            transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(360deg);
            transform: rotate(360deg);
  }
}

.loaded #loader-wrapper {
  visibility: hidden;
  transform: translateY(-100%);
}
.loaded #loader {
  opacity: 0;
}

.typewriter h1 {
  overflow: hidden; /* Ensures the content is not revealed until the animation */
  font-family: Monospace;
  border-right: .015em solid orange; /* The typwriter cursor */
  white-space: nowrap; /* Keeps the content on a single line */
  margin: 0 auto; /* Gives that scrolling effect as the typing happens */
  letter-spacing: 0.015em; /* Adjust as needed */
  animation: 
    typing 2.5s steps(30, end),
    blink-caret .75s step-end infinite;
  animation-delay: 2000ms;
  animation-fill-mode: both;
}

/* The typing effect */
@keyframes typing {
  from { width: 0 }
  to { width: 100% }
}

/* The typewriter cursor effect */
@keyframes blink-caret {
  from, to { border-color: transparent }
  50% { border-color: white; }
}

h1:hover {
  font-size: 50px;
}
</style>

<script>
  document.addEventListener("DOMContentLoaded", function() {
  setTimeout(function() {
      document.querySelector("body").classList.add("loaded");
  }, 2000)
});
</script>

<style>
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

<div class="typewriter">
  <h1>Eric's Blog</h1>
</div>

<div id="loader-wrapper">
  <div id="loader"></div>
  <div class="loader-section section-left"></div>
  <div class="loader-section section-right"></div>
</div>

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

<hr>

<h1 span style="color: white; font-size: 20px;">Socials </h1>


<style>

  body {
      animation: fadeInAnimation ease 3s;
      animation-iteration-count: 1;
      animation-fill-mode: forwards;
  }
  @keyframes fadeInAnimation {
      0% {
          opacity: 0;
      }
      100% {
          opacity: 0.75;
      }
  }

h1 {
  position: relative;
  font-size: 3rem;
  font-family: Monospace;
  color: cyan;
}

p {
  font-family: Monospace;
}
</style>

<style> 
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
<script src="https://apis.google.com/js/platform.js"></script>

<div class="g-ytsubscribe" data-channelid="UCpWLvdZNtaNOUF3wfFe1_og" data-layout="full" data-theme="dark" data-count="default"></div>

