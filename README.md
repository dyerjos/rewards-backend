<div id="top"></div>


<br />
<div align="center">
  <h3 align="center">Rewards App</h3>

  <p align="center">
    A backend to handle earning and spending reward points
    <br />
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project


### Built With

* [Django](https://www.djangoproject.com/)
* and :heart:

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

* [Docker Desktop](https://www.docker.com/products/docker-desktop/)


### Installation

1. Make sure your Docker daemon is running by starting up your Docker Desktop app

2. Run Docker Compose and build your Docker image by using this line in your terminal:

    ```shell
    docker-compose up -d --build
    ```

    Alternatively if the image is already built, you can run:

    ```shell
    docker-compose up -d
    ```

3. Server is now running on http://127.0.0.1:8000/


<p align="right">(<a href="#top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

There are several endpoints that can be used:
- http://127.0.0.1:8000/ (the home page)
- http://127.0.0.1:8000/spend_points
- http://127.0.0.1:8000/get_balance
- http://127.0.0.1:8000/admin (if you create a superuser)

A neat thing about the Django Rest Framework is that if you go directly to directly to one of these URLs (while the server is running) you can see information about the endpoint such as what http request methods are allowed.

Endpoints that allow POST/PUT methods even have text areas for you to add JSON and submit without using a client like Postman or Insomnia.

### Endpoint details

http://127.0.0.1:8000/ (the home page)
- allows a GET request to retrieve a list of all transactions in the database and their initial point amounts
- allows a POST request to add single transactions:
  ```
  { "payer": "DANNON", "points": 1000, "timestamp": "2020-11-02T14:00:00Z" }
  ```

http://127.0.0.1:8000/spend_points
- allows a POST request to spend points:
  ```
  { "points": 5000 }
  ```

http://127.0.0.1:8000/get_balance
- allows a GET request to retrieve total rewards points available per payer

http://127.0.0.1:8000/admin
- if you are curious about one of my favorite Django features run this in your terminal:
  ```
  docker-compose exec web python manage.py createsuperuser
  ```
  and then follow the prompts that follow. This will add you as a super user to your django server which you will then use to sign in to the admin site. Here you can play around, see existing transactions, and create some new transactions.

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

- [x] Setup new Django Project
- [x] Add Black for code formatting
- [x] Initial README work
- [x] Setup project with PostgreSQL
- [x] Setup endpoints
- [x] Document the API
- [ ] Add tests if for a production environment


<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Joshua Dyer - dyerjo@mail.gvsu.edu


<p align="right">(<a href="#top">back to top</a>)</p>

