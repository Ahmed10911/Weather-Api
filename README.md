# Weather-Api

Participants:
    1. 221042  M umar 
    2. 221024 M atif 
    3. 221096 Ahmed Bilal 
    4. 221104 Syed Zaryab Abbas Naqvi 

The link for the repository "https://github.com/Ahmed10911/Weather-Api.git"



<!-- ----------------------------------------------------------------------------------
                     1). The purpose of the API.
----------------------------------------------------------------------- -->

# Purpose
The Weather API is a Flask-based application that allows users to retrieve real-time weather information for a specific city. By leveraging the OpenWeather API, the application provides essential weather details, such as temperature, description, humidity, and wind speed. This API is useful for developers looking to integrate weather data into their web or mobile applications.

# Features
1. Retrieve current weather data for any city.
2. Real-time weather updates using OpenWeather API.
3. Easy-to-use API with json and rendered_template.
4. Simple, clean web interface to display weather data.


<!-- ----------------------------------------------------------------------------------
                 2). How to install dependencies and run the API.
----------------------------------------------------------------------- -->

1. Clone the repository:
    using command git clone https://github.com/Ahmed10911/Weather-Api.git

2. Set up a virtual environment 
    Setting a virtual environment was optional, but the environment makes the thing simple and isolated to install different packages.
    command: python -m venv venv
    For Activation: venv/bin/activate

3. Install dependencies
    1. Flask Package
    pip install flask

    2. Requests Package
    pip install Requests

4. Set up your API Key:
    API_KEY = '23fa10113efc5efb071a444b3cd0add7'

    This was the key I get from the weather server(openweathermap.org) for API.
    link: 'https://api.openweathermap.org/data/2.5/weather'

5. Run the Flask application
    To run the api we use the vs code editor and click on execute button or by writing the name of file on the terminal.
    command: python app.py


<!-- ----------------------------------------------------------------------------------
                 3). How each member contributed to the project.
----------------------------------------------------------------------- -->

Participants:
.
    1. 221096 Ahmed Bilal(Api Development):
        Created the repository of weather and invite the rest of us as collaborator on git hub.
        Created the virtual environment and install the dependecies regarding project and create an api to fetch weather details from the server and push and pull to the git hub.
.
.
    2. 221104 Syed Zaryab Abbas(Structure the Api Appearance):
        Created the html files to structure the website for api and commit and push the changes to the github and merge them with main branch using pull requests.
.
.
    3. 221024 Muhammad Atif(Styling the Api):
        Created the css file to style the html files and make the website interactive and organized. Commit and push the changes to the github and merge them with main branch using pull requests.
.
.
    4. 221042 Muhummad Umer(Testing and Documentation):
        Tests the api's performance ,working ,correctness whether it shows the result according to the server' data.
        Created this README file which contain the documentation and description of the API.


<!-- ----------------------------------------------------------------------------------
                    4). Steps for testing the API.
----------------------------------------------------------------------- -->

Here’s a brief overview of the tests:

1. Test Home Page:
Ensures the home page (/) responds with a welcome message and status code 200.

2. Test Weather Endpoint with Valid City:
Sends a valid city name and checks that the weather data is returned correctly.

3. Test Weather Endpoint Without City:
Validates that  error is returned if no city name is provided.

4. Test Weather Endpoint with Invalid City:
Checks that a error is returned when an invalid city name is used.

5. Test to compare the result of Api with the servers data.
Checks that data in Api mathches with the data of the server. 

Screentshots will be available on the doc file. 






