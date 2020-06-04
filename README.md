  
<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://trackbasket.herokuapp.com/">
  </a>
  
  <h1 align="center">Track Basket</h1> <br><br>
  
TrackBasket is a grocery-delivery app for volunteer shoppers who serve people whose mobility is limited during the pandemic. The purpose of the app is to allow at-risk consumers to create shopping lists by searching items available at a nearby store and to make these lists available to volunteers who can sort them and select the one they can fulfill.


<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
  * [Schema](#schema)
* [Getting Started](#getting-started)
  * [Installation](#installation)
  * [Testing](#testing)

<!-- ABOUT THE PROJECT -->
## About The Project

As the thread of COVID-19 rises, it's not safe for some people to leave their house, even to buy essentials. Trackbasket connects this at-risk population with volunteers who shop for and deliver customized grocery lists.

### Built With

* Frameworks: Flask
* Deployment: Heroku
* Database: PostgreSQL
* Testing: UnitTest, Coverage
* Dependency Management: Poetry
* Project Management: Github Project Board
* External API: Kroger

### Schema

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Installation

1. Clone the repo
```sh
git clone https://github.com/track-basket/trackbasket_BE
```
2. Install Python

3. Install Poetry 

4. Run the app locally
```sh
python trackbasket_be/app.py
```
5. Your credentials should be stored locally

### Testing

Run the test suite from the `trackbasket_be` directory:

```sh
python -m unittest discover
```

## Back End Endpoints 

### Volunteer Endpoint

Retrieve a volunteer profile information:
```sh
GET https://trackbasket.herokuapp.com/volunteer/<volunteer_id>
```
Create a new volunteer:

```sh
POST https://trackbasket.herokuapp.com/volunteer/<volunteer_id>

```

### AtRiskUser Endpoints

### ShoppingList Endpoints

### List of ShoppingLists Endpoint


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [GrowStuff.org](https://www.growstuff.org/)
* [Google Dev](https://console.developers.google.com/)
* Gabz Cirbo for designing the GardenThat logo! 

## Developer GitHub Profiles

* Paul Debevec - [GitHub](https://github.com/PaulDebevec) <br>
* Alexis Dumortier - [GitHub](https://github.com/adumortier)<br>
* Nathan Keller - [GitHub](https://github.com/nkeller1)<br>
* Will Kunz - [GitHub](https://github.com/willkunz13)<br>

Deployed Application on Heroku: [GardenThat!](https://gardenthat.herokuapp.com/)
