<div align="center">

# 🌤️ Weatherly 🌧️




</div>



<p align="center">
  <a href="https://www.python.org" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a>
  <a href="https://www.djangoproject.com/" target="_blank"> <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/> </a>
  <a href="https://www.docker.com/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker" width="40" height="40"/> </a>
  <a href="https://www.postgresql.org" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original-wordmark.svg" alt="postgresql" width="40" height="40"/> </a>
  <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/> </a>
  <a href="https://www.w3.org/html/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a>
  <a href="https://www.w3schools.com/css/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a>
  <a href="https://reactjs.org" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/react/react-original.svg" alt="react" width="40" height="40"/> </a>
  <a href="https://www.nginx.com" target="_blank"> <img src="https://www.vectorlogo.zone/logos/nginx/nginx-icon.svg" alt="nginx" width="40" height="40"/> </a>
  <a href="https://www.gunicorn.org" target="_blank"> <img src="https://www.vectorlogo.zone/logos/gunicorn/gunicorn-icon.svg" alt="gunicorn" width="40" height="40"/> </a>
</p>

---

## 🎞️ Demo

<p align="center">
  <img src="Document/Video/video.gif" alt="Weatherly Presentation" width="600">
</p>

---

## 📋 Table of Contents
- [🎯 Goal](#goal)
- [✨ Features](#features)
- [🚀 Setup](#setup)
  - [🔹 First Step](#first-step)
  - [🔹 Clone Project](#clone-project)
  - [🐳 Docker](#docker)
    - [🛠 Development](#development)
      - [🎨 Flake8 & Black](#flake8--black)
    - [🚢 Deployment](#deployment)
      - [⚙ Gunicorn & Nginx](#gunicorn--nginx)
- [🙏 Thanks](#thanks)


---

## 🎯 Goal
Weatherly provides real-time weather forecasts with a user-friendly interface, using Django for backend, React for frontend, and Docker for deployment.

---

## ✨ Features
- Real-time weather updates
- Mobile-friendly UI with React
- Dockerized development and production environments
- Linting and code formatting with **Flake8** & **Black**
- Secure deployment with **Gunicorn** & **Nginx**
- PostgreSQL database for reliable data storage

---

## 🚀 Setup

### 🔹 First Step
Make sure you have [Docker](https://www.docker.com/) installed on your computer.

### 🔹 Clone Project
```bash
git clone https://github.com/mohammadmatin2000/Weatherly.git
```


## Docker
Docker is a powerful tool for run, deploying and transferring project, so i decided to use it .

As i said i separet my site, so for running it on development or deployment mode, you should follow one of these section :

## Development
```bash
docker-compose up --build -d
```
By running this command everything creat and run automaticlly, after everything is over you can oppen <a href='127.0.0.1:8000'>127.0.0.1:8000</a> on your browser to see the resault

This version of website is for <b>developers</b> to testing and editting

This version has some tools that it is not exist in [Deployment](#deployment) like :


<hr>

### Flake8 and Black
As i said <a href='https://pypi.org/project/flake8-django/'>Flake8</a> and <a href='https://pypi.org/project/black/'>Black</a> are helping for reformat all codes by <a href='https://peps.python.org/pep-0008/'>PEP8</a> rule, for using enter this command :
```bash
docker-compose exec backend sh -c "black . -l 78 && flake8"
```


## Deployment
```bash
docker-compose -f docker-compose-stage.yml up --build -d
```
<h3>After Docker Compose is run, React will start and then you need to click on the link to go to the game.</h3>

```bash
http://localhost:3000
```
By running this command everything creat and run automaticlly, after everything is over you can oppen <a href='127.0.0.1:8000'>127.0.0.1</a> on your browser to see the resault

This version of website is for <b>normal user</b> to take a look to site

This version has some tools that it is not exist in [Development](#development) like :
### Gunicorn and Nginx
To set your project to deployment mode, you have to change DEBUG mode to False . This thing is a good way to make your site more secure but there is a disadvantages, statics and medias doesn't serve moreover django can't transfer requests on website so it's the time that <a href='https://gunicorn.org/'>Gunicorn</a> and <a href='https://nginx.org/en/'>Nginx</a> come .
<hr>

<div align="center">
<h1 align="center">Thanks for visiting</h1>
<h3 align="center">I hope that you enjoy it, Let me know if you have any suggestion</h3>
</div>


