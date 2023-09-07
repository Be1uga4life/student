<style> 
  hr{background-color: #7289da;}
  body {
    padding: 25px;
    background-color: #121212;
    color: white;
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


    h1 {
        color: cyan;
    }

    button {
        background: royalblue;
        color: white;
    }

</style>



<h1> Weather Report </h1>
<head>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.3/jquery.min.js"></script>
    <style>
        table, th, td { border: 1px solid cyan; border-collapse: collapse; }
        td, th {padding: 10px;}
    </style>
</head>
<body>
    <button id="getDataButton">Get Data from API</button>
    <input type="text" id="searchInput" placeholder="Enter a key to search">
    <button id="searchButton">Search</button>
    <div id="jsonData"></div>
    <table border="1">
        <tbody id="table-body"></tbody>
    </table>
    <script>
  <h1>Weather Report</h1>
  <button id="getDataButton">Get Data from API</button>
  <input type="text" id="searchInput" placeholder="Enter a key to search">
  <button id="searchButton">Search</button>
  <div id="jsonData"></div>
  <table border="1">
    <tbody id="table-body"></tbody>
  </table>
  <div id="searchResult"></div> <!-- Add a div to display search results -->
  
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.3/jquery.min.js"></script>
  <style>
    /* Additional styles here if needed */
  </style>

  <script>
    // Define the API endpoint URL
    const apiUrl = 'https://api.weatherapi.com/v1/current.json?key=935574b3cab243fc9d950024230209&q=San Diego&aqi=yes';
    
    // Function to make the API call when the button is clicked
    document.getElementById('getDataButton').addEventListener('click', fetchData);

    function fetchData() {
      fetch(apiUrl)
        .then(response => {
          // Check if the response status is OK (200)
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          return response.json(); // Parse the JSON response
        })
        .then(data => {
          // Handle the data from the API
          convertToVerticalTable(data); // Call the function to populate the table
        })
        .catch(error => {
          // Handle errors
          console.error('There was a problem with the fetch operation:', error);
        });
    }

    function convertToVerticalTable(jsonData) {
      const tableBody = document.getElementById("table-body");
      for (const key in jsonData.location) {
        const row = document.createElement("tr");
        const cellKey = document.createElement("td");
        const cellValue = document.createElement("td");
        cellKey.textContent = key;
        cellValue.textContent = jsonData.location[key];
        row.appendChild(cellKey);
        row.appendChild(cellValue);
        tableBody.appendChild(row);
      }
      for (const key in jsonData.current) {
        const row = document.createElement("tr");
        const cellKey = document.createElement("td");
        const cellValue = document.createElement("td");
        cellKey.textContent = key;
        cellValue.textContent = jsonData.current[key];
        row.appendChild(cellKey);
        row.appendChild(cellValue);
        tableBody.appendChild(row);
      }
    }
  </script>

  <script>
    // Add an event listener for the search button
    document.getElementById('searchButton').addEventListener('click', searchTable);

    function searchTable() {
      const searchInput = document.getElementById('searchInput').value.toLowerCase();
      const tableRows = document.querySelectorAll('#table-body tr');
      // Loop through each table row and check if it contains the search input
      let found = false;
      tableRows.forEach(row => {
        const cells = row.querySelectorAll('td');
        cells.forEach(cell => {
          const cellText = cell.textContent.toLowerCase();
          if (cellText.includes(searchInput)) {
            // Display the matching row in the searchResult div
            document.getElementById('searchResult').textContent = 'Found: ' + row.textContent;
            found = true;
          }
        });
      });
      // If no match is found, display a message
      if (!found) {
        document.getElementById('searchResult').textContent = 'No matching row found.';
      }
    }
  </script>
</body>