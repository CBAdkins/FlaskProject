from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Azure App Service sets the PORT environment variable
    port = os.environ.get('PORT', '5000') 
    return f'Hello from Flask on Azure! Running on port: {port}'

# The Azure App Service startup command will execute this file.
if __name__ == '__main__':
    app.run(debug=True)
