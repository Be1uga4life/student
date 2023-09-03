
<head>
    <title>Login</title>
</head>
<body>
    <h2>Login</h2>
    <form id="login-form">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required><br><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br><br>
        <button type="button" onclick="authenticate()">Login</button>
    </form>
    <p id="result"></p>

    <script>
        function authenticate() {
            var username = document.getElementById("username").value;
            var password = document.getElementById("password").value;

            // Check if the credentials are correct (for demonstration purposes only)
            if (username === "EroxYII" && password === "Hyp3rionIsTheG0atButPr1las3yIsnT") {
                document.getElementById("result").textContent = "Login successful! The flag is: flag{dont_go_into_will's_basement}";
            } else {
                document.getElementById("result").textContent = "Invalid credentials. Please try again.";
            }
        }
    </script>
</body>

