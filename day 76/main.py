from flask import Flask


app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index(): 
  return 'Hello from Flask!'

@app.route('/portfolio') 
def portfolio():
  page = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your Name - Portfolio</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to your CSS file -->
</head>
<body>
    <header>
        <nav>
            <div class="container">
                <h1>Your Name</h1>
                <ul>
                    <li><a href="#about">About</a></li>
                    <li><a href="#portfolio">Portfolio</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </div>
        </nav>
    </header>

    <section id="about">
        <div class="container">
            <h2>About Me</h2>
            <p>Write a brief introduction about yourself here.</p>
        </div>
    </section>

    <section id="portfolio">
        <div class="container">
            <h2>Portfolio</h2>
            <!-- Add your portfolio projects here -->
            <div class="project">
                <img src="project1.jpg" alt="Project 1">
                <h3>Project 1</h3>
                <p>Description of the project goes here.</p>
            </div>
            <div class="project">
                <img src="project2.jpg" alt="Project 2">
                <h3>Project 2</h3>
                <p>Description of the project goes here.</p>
            </div>
            <!-- Add more project entries as needed -->
        </div>
    </section>

    <section id="contact">
        <div class="container">
            <h2>Contact Me</h2>
            <p>You can reach me at your@email.com</p>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>&copy; 2023 Your Name. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>

"""
  return page
  

app.route('/linktree')
def linktree():
  page = f""""""
  return page

app.run(host='0.0.0.0', port=81)

