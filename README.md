# homesite-ratings-exercise
Description
--------
Web application that takes in data about a home and returns an insurance premium quote.

Deployment Instructions
---------
If Python3 is not installed on your machine, install it with Homebrew. (And if Homebrew isn't installed, follow the instructions at https://brew.sh/):
`brew install python3`

To create a virtual environment:
`python3 -m venv <environment name>`

To activate the virtual environment:
`source <environment name>/bin/activate`

cd into the project directory

To install dependencies:
`python -m pip install -r requirements.txt`

To launch the server:
`python rating.py`

The server runs on localhost, port 5000.

Input format
--------
The server accepts POST requests at the / endpoint. It expects a JSON body with the following fields:
```
"CustomerID" : integer
"DwellingCoverage" : positive integer
"HomeAge" : positive integer
"RoofType" : "Asphalt Singles", "Tin", or "Wood"
"NumberOfUnits" : integer between 1 and 4, inclusive

An optional "PartnerDiscount" field can be either "Y" or "N" (and is interpreted as "N" if absent).
```
