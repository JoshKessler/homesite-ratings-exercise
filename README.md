# homesite-ratings-exercise
Web application that takes in data about a home and returns an insurance premium quote.

Deployment Instructions
If Python3 is not installed on your machine, install it with Homebrew. (And if Homebrew isn't installed, follow the instructions at https://brew.sh/):
brew install python3

To create a virtual environment:
python3 -m venv kessler_rating

To activate the virtual environment:
source kessler_rating/bin/activate

cd into the project directory

To install dependencies:
python -m pip install -r requirements.txt

To launch the server:
python rating.py

The server runs on localhost, port 5000.

The server accepts POST requests at the / endpoint.