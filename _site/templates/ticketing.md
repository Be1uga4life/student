

<head>
  <title>CCG Ticketing</title>
  <link href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700" rel="stylesheet">
  <style>
    * {
      box-sizing: border-box;
    }
    html,
    body {
      min-height: 100vh;
      padding: 0;
      margin: 0;
      font-family: Roboto, Arial, sans-serif;
      font-size: 14px;
      color: white;
    }
/* Dropdown Button */
.dropbtn {
  background-color: #04AA6D;
  color: white;
  padding: 16px;
  font-size: 16px;
  border: none;
}
/* The container <div> - needed to position the dropdown content */
.dropdown {
  position: static;
  display: inline-block;
  transform: translateY(-225%);
}
/* Dropdown Content (Hidden by Default) */
.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f1f1f1;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}
/* Links inside the dropdown */
.dropdown-content a {
  color: black;
  padding: 12px 12px;
  text-decoration: none;
  display: block;
}
/* Change color of dropdown links on hover */
.dropdown-content a:hover {background-color: #ddd;}
/* Show the dropdown menu on hover */
.dropdown:hover .dropdown-content {display: block;}
/* Change the background color of the dropdown button when the dropdown content is shown */
.dropdown:hover .dropbtn {background-color: #3e8e41;}
    input,
    textarea {
      outline: none;
      color: white;
      font-family: Roboto, Arial, sans-serif;
      color: white;
    }
    body {
      display: flex;
      justify-content: center;
      align-items: center;
      padding: 20px;
      background: #121212;
      color: white;
    }
    h1 {
      margin-top: 0;
      font-weight: 500;
      color: white;
    }
    form {
      position: relative;
      width: 80%;
      border-radius: 30px;
      background: #242323;
      color: white;
    }
    .form-left-decoration,
    .form-right-decoration {
      content: "";
      position: absolute;
      width: 50px;
      height: 20px;
      border-radius: 20px;
      color: white;
    }
    .form-left-decoration {
      bottom: 60px;
      left: -30px;
      color: white;
    }
    .form-right-decoration {
      top: 60px;
      right: -30px;
      color: white;
    }
    .form-left-decoration:before,
    .form-left-decoration:after,
    .form-right-decoration:before,
    .form-right-decoration:after {
      content: "";
      position: absolute;
      width: 50px;
      height: 20px;
      border-radius: 30px;
      color: white;
    }
    .form-left-decoration:before {
      top: -20px;
      color: white;
    }
    .form-left-decoration:after {
      top: 20px;
      left: 10px;
      color: white;
    }
    .form-right-decoration:before {
      top: -20px;
      right: 0;
      color: white;
    }
    .form-right-decoration:after {
      top: 20px;
      right: 10px;
      color: white;
    }
    .circle {
      position: absolute;
      bottom: 80px;
      left: -55px;
      width: 20px;
      height: 20px;
      border-radius: 50%;
      color: white;
    }
    .form-inner {
      padding: 40px;
      color: white;
    }
    .form-inner input,
    .form-inner textarea {
      display: block;
      width: 100%;
      padding: 15px;
      margin-bottom: 10px;
      border: none;
      border-radius: 20px;
      background: grey;
      color: white;
    }
    .form-inner textarea {
      resize: none;
      color: white;
    }
    button {
      width: 100%;
      padding: 10px;
      margin-top: 20px;
      border-radius: 20px;
      border: none;
      border-bottom: 4px solid #151515;
      background: #0d0d0d;
      font-size: 16px;
      font-weight: 400;
      color: white;
    }
    .delete {
      width: 100%;
      padding: 10px;
      margin-top: 20px;
      background: green;
      font-size: 16px;
      font-weight: 400;
      margin-top: -170px;
    }
    button:hover {
      background: grey;
    }
    @media (min-width: 568px) {
      form {
        width: 60%;
      }
    
  </style>
</head>

<body>
  <form action="/create_ticket" method="post" class="decor">
    <div class="form-left-decoration"></div>
    <div class="form-right-decoration"></div>
    <div class="circle"></div>
    <div class="form-inner">
      <h1>Submit a ticket</h1>
      <input color='white' name='a' type="text" placeholder="subject">
      <textarea name='b' placeholder="Message..." rows="3"></textarea>
      <button type="submit" href="/">Submit</button>
    </div>
  </form>

  <form action="/delete_ticket" method="post" class="decor">
    <button class="delete" href="/"> Clear Tickets </button>
  </form>

  <form action="/show_tickets" method="post" class="decor">
    <button class="delete" href="/"> Show Tickets </button>
    <label for="fileDropdown">Select a file:</label>
    <select id="fileDropdown"></select>
  </form>

  <script>
      document.addEventListener("DOMContentLoaded", function () {
    // Get a reference to the dropdown element
    const fileDropdown = document.getElementById("fileDropdown");

    // Make an AJAX request to retrieve the list of files in a directory
    // Replace 'your_server_endpoint' with the actual endpoint that provides the list of files.
    fetch("/tickets")
        .then(response => response.json()) // Assuming the server returns a JSON array of file names
        .then(data => {
            data.forEach(filename => {
                // Create an option element for each file and add it to the dropdown
                const option = document.createElement("option");
                option.value = filename;
                option.textContent = filename;
                fileDropdown.appendChild(option);
            });
        })
        .catch(error => {
            console.error("Error fetching file list:", error);
        });
});
</script>

</body>

