  
<p align="center">
  <a href="https://trackbasket.herokuapp.com/"><img width="500" height="300" src="https://user-images.githubusercontent.com/55954962/83821753-706c4f00-a68c-11ea-9c1b-2a2d24eddd94.jpg"></a>
</p>
TrackBasket is a grocery-delivery app for volunteer shoppers who serve people whose mobility is limited during the pandemic. The purpose of the app is to allow at-risk consumers to create shopping lists by searching items available at a nearby store and to make these lists available to volunteers who can sort them and select the one they can fulfill. Volunteers can chat with the at-risk consumer whose list they have adopted to ask for clarification while shopping. They can also update the status of the list they've adopted as they make progress with the shopping and the delivery.
<br><br><br><br>

<p align="center">
<a href="http://g.recordit.co/Fq4vHJEapy.gif"><img src="http://g.recordit.co/Fq4vHJEapy.gif" width="500" height="500"/></a>
</p>
<br><br>

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

Back end:
* Frameworks: Flask
* Websockets: Socket.io
* Language: Python 3.7
* Deployment: Heroku
* Database: PostgreSQL
* Testing: UnitTest, Coverage
* Dependency Management: Poetry
* Project Management: Github Project Board
* External API: Kroger

Front end:

* React Native
* React Navigation
* React Hooks/Context API
* Websockets: Socket.io
* Expo
* React Native Testing Library
* Jest

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

Retrieve a volunteer's profile information:
```sh
GET https://trackbasket.herokuapp.com/volunteer/<volunteer_id>
```
Expected response:
```sh
{
    "data": {
        "id": "volunteer",
        "attributes": {
           	"id": "test76687",
            	"name": "my test user",
              	"phone number": "719 342 3242"
        }
    }
}

```

Create a new volunteer:

```sh
POST https://trackbasket.herokuapp.com/volunteer/<volunteer_id>
{
     "name": "my test user",
     "phone_number": "719 342 3242"
}

```

Expected response:
```sh
{
    "volunteer": {
        "name": "my test user",
        "phone_number": "719 342 3242"
    }
}
```

Update a volunteer:
```sh
PATCH	 https://trackbasket.herokuapp.com/volunteer/<volunteer_id>
{
	     "name": "Bob Doe",
	     "phone_number": "719 342 3249"
}
```
Expected response:

```sh
{
    "data": {
        "id": "volunteer",
        "attributes": {
           	"id": "test76687",
            	"name": "Bob Doe",
              	"phone number": "719 342 3249"
        }
    }
}

```

### AtRiskUser Endpoint

Retrieve an at risk user's profile information:
```sh
GET https://trackbasket.herokuapp.com/atriskuser/<at_risk_user_id>
```
Create a new at risk user:
```sh
POST https://trackbasket.herokuapp.com/atriskuser/<at_risk_user_id>
{
    "name": "Alexis",
    "address": "125 ocean ave",
    "city": "Denver",
    "state": "ca",
    "zipcode": "80203",
    "phone_number": "123-456-7890"
}
```
Update an at risk user:
```sh
PATCH https://trackbasket.herokuapp.com/atriskuser/<at_risk_user_id>
```
Delete an at risk user:
```sh
DELETE https://trackbasket.herokuapp.com/atriskuser/<at_risk_user_id>
```

### ShoppingList Endpoint

Retrieve a shopping list's information:
```sh
GET https://trackbasket.herokuapp.com/shoppinglist/<at_risk_user_id>
```
Create a new shopping list:
```sh
POST https://trackbasket.herokuapp.com/shoppinglist/<at_risk_user_id>
```
Update a shopping list:
```sh
PATCH https://trackbasket.herokuapp.com/shoppinglist/<at_risk_user_id>
```
Delete shopping list:
```sh
DELETE https://trackbasket.herokuapp.com/shoppinglist/<at_risk_user_id>
```

### List of ShoppingLists Endpoint

Retrieve all shopping lists' and its information:
```sh
GET https://trackbasket.herokuapp.com/listshoppinglists
```

### Conversations Endpoint
Retrieve a conversation between an `at_risk_user` and a `volunteer` :
```sh
GET https://trackbasket.herokuapp.com/conversations?at_risk_user_id=<at_risk_user_id>&volunteer_id=<volunteer_id>
```
Expected response:

```sh
{
    "data": {
        "id": "conversation",
        "attributes": {
            "messages": [
                {
                    "text": "Alex: Can't find the butter",
                    "timestamp": "27/06/2020 04:43:23",
		    "author": "volunteer"
                },
                {
                    "text": "Meg: Forget about it, I don't need it",
                    "timestamp": "27/06/2020 04:43:35",
		    "author": "at_risk_user"
                },
                {
                    "text": "Alex: Alright",
                    "timestamp": "27/06/2020 04:43:43",
		    "author": "volunteer"
                }
            ]
        }
    }
}
```


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* Alex Robinson (PM) - [GitHub](https://github.com/scottalexandra)
* Eric Weissman (PM) - [GitHub](https://github.com/ericweissman)

## Developer GitHub Profiles

* Alexis Dumortier (Backend) - [GitHub](https://github.com/adumortier)
* Maria Ronauli (Backend) - [GitHub](https://github.com/mronauli)
* Ed Stoner (Frontend) - [GitHub](https://github.com/edlsto)
* Cody Smith (Frontend) - [GitHub](https://github.com/monstaro)


