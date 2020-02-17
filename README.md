# A Simple Crawler

This repository is the solution to a challenge proposed to me.  
The application is a webcrawler, made with Selenium, that navigates through the Bovespa website and get a serie of values from Petrobras.

## Technologies
Python  
Selenium  
Docker

## Run with Docker
In the repository main folder, open the bash and run
```bash
docker build . -t simple-crawler
```
When the image finishes building, run the container with the command
```bash
docker run simple-crawler
```