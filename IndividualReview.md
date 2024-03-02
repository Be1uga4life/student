---
title: Individual Review
layout: base
description: Individual Review for Tri 2
permalink: /IndividualReview
categories: [C4.9]
tags: [javascript]
---

<style>
    body {
      animation: fadeInAnimation ease 3s;
      animation-iteration-count: 1;
      animation-fill-mode: forwards;
  }

  body { 
    background-color: #121212; 
    color: #ffffff; 
  } 

  hr {
    background-color: #7289da;
  }

  .color {
    color: #7289da;
  }

  body {
    padding: 25px;
    background-color: #121212;
    color: #ffffff;
    transition-duration: 0.2s;
    font-family: Monospace;
  }

  h1 {
    color: cyan;
  }

  h2 {
    color: cyan;
  }

  code {
    color: cyan;
  }

  table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 20px;
  }

  th, td {
    border: 1px solid #7289da;
    padding: 8px;
    text-align: left;
  }

  th {
    background-color: #7289da;
    color: #ffffff;
  }

  tr:nth-child(even) {
    background-color: #424242;
  }

  .image-cell {
    width: 600px;
    vertical-align: top;
  }

  .image {
    width: 100%;
  }
</style>

## Face Login Screen Documentation
 
The Face Login Screen 

<table>
  <thead>
    <tr>
      <th>Requirements</th>
      <th>Images</th>
      <th>Completed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>User Input</td>
      <td class="image-cell">
        <img class="image" src="https://cdn.discordapp.com/attachments/957882131206520843/1213007641136336936/image.png?ex=65f3e866&is=65e17366&hm=6607eb375b0af2230d8951a3d7561ae4fd6279e71e74c014d96d91bfe53600ca&" alt="User Input">
      </td>
      <td>The User needs to input his face, and his corresponding user onto the login screen is shown to the left. Essentially what happens, is the frontend accesses the camera, and takes a picture when the "capture" button is pressed. This then triggers the event to get the username, along with the photo. The photo is converted to Base64 to send to the Backend.</td>
    </tr>
    <tr>
      <td>User Input (Code) </td>
      <td class="image-cell">
        <img class="image" src="https://cdn.discordapp.com/attachments/957882131206520843/1213008820658376735/image.png?ex=65f3e97f&is=65e1747f&hm=7a6d4ec1824fa11ff2af86232467b8287b64a6e525d4aa8396050ac2a9c706a0&" alt="User Input">
      </td>
      <td>The code for sending the form to the backend is as follows:</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Use of at least one list (or other collection type) to represent a collection of data that is stored and used to manage program complexity and help fulfill the program’s purpose</td>
      <td class="image-cell">
        <img class="image" src="https://cdn.discordapp.com/attachments/957882131206520843/1213013646230163456/image.png?ex=65f3edfd&is=65e178fd&hm=b6c7a4a45b959cf72d4d0e333861092285ddc785dd4c5cbf7a8ef53862912039&" alt="User Input">
      </td>
      <td>If the login succeeds, a JWT token should be sent to the frontend. This JWT token is then stored to be used in later functions in other games that invovle figuring out which user is playing the game, or how long they were logged in, or how many times did they log in </td>
    </tr>
    <tr>
      <td>One procedure that contributes to the program’s intended purpose, where you have defined: the procedure’s name, the return type (if necessary), one or more parameters</td>
      <td class="image-cell">
        <img class="image" src="https://cdn.discordapp.com/attachments/957882131206520843/1213018111205187604/image.png?ex=65f3f226&is=65e17d26&hm=d9e1059a18fa24a84297f2675adc7f95764b42cd3e24bc46f389ac5372fbffb6&" alt="User Input">
      </td>
      <td>This is the Backend code for taking care of the picture that is being sent. The picture that is being sent is first parsed into an actual image, and saved within a directory called "/static/unknown", this is then compared with the user's pre-existing registered face located in "/static/face". They are compared using a python tool named face_recognition. Then, it either outputs a True or False.</td>
    </tr>
    <tr>
      <td>An algorithm that includes sequencing, selection, and iteration that is in the body of the selected procedure</td>
      <td class="image-cell">
        <img class="image" src="https://cdn.discordapp.com/attachments/957882131206520843/1213022043579093052/image.png?ex=65f3f5d0&is=65e180d0&hm=aed33bdf524833766a7a76f497d50b91c64213297a17af708c2478cfa81fe2ea&" alt="User Input">
      </td>   
      <td>My program utilizes selection, as previously mentioned, I have to compare two faces, and output a boolean value. Using that Boolean value, I decide whether or not the user should or should not be authenticated into the system</td> 
    </tr>
    <tr>
      <td>Calls to your student-developed procedure</td>
      <td class="image-cell">
        <img class="image" src="https://cdn.discordapp.com/attachments/957882131206520843/1213163827827445821/image.png?ex=65f479dc&is=65e204dc&hm=78540439d59d23907e35e318a1440e4f790bc53da8028581e0373023f2937e17&" alt="User Input">
      </td>  
      <td>The capture function is used in sync with the capture function as seen above</td>
    </tr>
    <tr>
      <td>Instructions for output based on input.</td>
      <td class="image-cell">
        <img class="image" src="https://cdn.discordapp.com/attachments/1173876301233410108/1213025656296964096/image.png?ex=65f3f92d&is=65e1842d&hm=354e78d725e3e3dd3deed62c0c26ff5ce8da8eae0722b3fc41d68f4ca7dd1956&" alt="User Input">
      </td>  
      <td>The output is just the JWT token. Whether or not it's given to you is completley based on whether you authenticated or not. If not, the system will alert you that you haven't authenticated succesfully.</td>
    </tr>
  </tbody>
</table>

Frontend Commits: https://github.com/Saaras859/ByteJam/commits/main/
Backend Commits: https://github.com/Be1uga4life/ByteJam_Backend/commits/main/


In Total: 39 commits