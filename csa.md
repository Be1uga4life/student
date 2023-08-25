---
layout: schedule
title: Computer Science "A"
units: "1,2,3,4,5,6,7,8,9"
course: csa
---
<body>
  <div id="filler"></div>

  <div id="container">
    <div id="one"><img src="images/1.jpg"></div>
    <div id="two"><img src="images/2.jpg"></div>
    <div id="three"><img src="images/3.jpg"></div>
  </div>

  <script>
    window.addEventListener('scroll', function() {
      let num = window.scrollY / window.innerHeight;
      let x = 0;

      document.getElementById('filler').style.display = 'none';

      if(num <= 1) {
        document.getElementById('one').style.opacity = 1-num;
        x = (1-num)*2;
        document.getElementById('one').style.transform = 'translate3d('+x+'%,'+x+'%,0px) scale(1,1) rotate(-3deg)';
      } else if(num > 1 && num <= 2) {
        document.getElementById('two').style.opacity = 2-num;
        x = (2-num)*2;
        document.getElementById('two').style.transform = 'translate3d('+x+'%,-'+x+'%,0px) scale(1,1) rotate(5deg)';
      } else if(num > 2 && num <= 3) {
        document.getElementById('three').style.opacity = 3-num;
        x = (3-num)*2;
        document.getElementById('three').style.transform = 'translate3d('+x+'%,'+x+'%,0px) scale(1,1) rotate(-15deg)';
      } else {
        document.getElementById('filler').style.display = 'block';
      }
    })
  </script>
</body>