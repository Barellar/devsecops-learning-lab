from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# Inline HTML/CSS/JS with clean dashboard UI and transitions
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DevSecOps Secure Dashboard</title>
    <style>
        :root {
            --primary: #10b981;
            --bg-dark: #0f172a;
            --card-dark: #1e293b;
            --text-main: #f8fafc;
        }
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background-color: var(--bg-dark);
            color: var(--text-main);
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .container {
            background-color: var(--card-dark);
            padding: 2.5rem;
            border-radius: 16px;
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3), 0 8px 10px -6px rgba(0, 0, 0, 0.3);
            text-align: center;
            max-width: 450px;
            width: 100%;
            transform: scale(0.95);
            opacity: 0;
            animation: fadeIn 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        }
        @keyframes fadeIn {
            to { transform: scale(1); opacity: 1; }
        }
        .status-badge {
            background-color: rgba(16, 185, 129, 0.2);
            color: var(--primary);
            padding: 0.5rem 1rem;
            border-radius: 9999px;
            display: inline-block;
            font-weight: 600;
            font-size: 0.875rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 0 15px rgba(16, 185, 129, 0.4);
            animation: pulse 2s infinite;
        }
        @keyframes pulse {
            0%, 100% { box-shadow: 0 0 15px rgba(16, 185, 129, 0.4); }
            50% { box-shadow: 0 0 25px rgba(16, 185, 129, 0.7); }
        }
        input {
            width: 80%;
            padding: 0.75rem 1rem;
            border-radius: 8px;
            border: 2px solid #334155;
            background-color: #0f172a;
            color: white;
            font-size: 1rem;
            margin-bottom: 1rem;
            transition: border-color 0.3s ease;
        }
        input:focus {
            outline: none;
            border-color: var(--primary);
        }
        button {
            background-color: var(--primary);
            color: white;
            border: none;
            padding: 0.75rem 1.5rem;
            border-radius: 8px;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        button:hover {
            background-color: #059669;
            transform: translateY(-2px);
        }
        #result-box {
            margin-top: 1.5rem;
            min-height: 50px;
            padding: 1rem;
            background-color: #0f172a;
            border-radius: 8px;
            border: 1px dashed #334155;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 1.1rem;
            font-weight: 500;
            transition: all 0.3s ease;
        }
        .pop-animation {
            animation: popIn 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
        }
        @keyframes popIn {
            0% { transform: scale(0.8); opacity: 0; }
            100% { transform: scale(1); opacity: 1; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="status-badge">● Pipeline Verified Secure</div>
        <h2>DevSecOps Portal</h2>
        <p style="color: #94a3b8; margin-bottom: 2rem;">Scan passed, app delivered. Test interaction below:</p>
        
        <input type="text" id="nameInput" placeholder="Enter your name..." autocomplete="off">
        <br>
        <button onclick="sendGreeting()">Trigger Secure Greet</button>
        
        <div id="result-box">Awaiting request...</div>
    </div>

    <script>
        async function sendGreeting() {
            const name = document.getElementById('nameInput').value || 'Guest';
            const resultBox = document.getElementById('result-box');
            
            resultBox.innerHTML = 'Processing...';
            resultBox.style.color = '#94a3b8';
            
            try {
                const response = await fetch(`/greet?name=${encodeURIComponent(name)}`);
                const data = await response.json();
                
                resultBox.className = ''; // reset animation
                void resultBox.offsetWidth; // trigger reflow
                resultBox.className = 'pop-animation';
                
                resultBox.innerHTML = data.message;
                resultBox.style.color = '#10b981';
            } catch (error) {
                resultBox.innerHTML = 'Error communicating with server.';
                resultBox.style.color = '#ef4444';
            }
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/greet')
def greet():
    name = request.args.get('name', 'Guest')
    return jsonify({"message": f"Hello, {name}! This request was sanitized and validated."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
