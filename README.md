## CI/CD & Kubernetes Deployment
### Overview

This project demonstrates the development, containerization, and deployment of a Django application using modern DevOps practices. It includes:

Django web application development using Python.

Docker containerization of the Django app.

Deployment on a Kubernetes cluster running on AWS EC2.

CI/CD automation with GitHub Actions and pipeline integration with Docker Hub.

## Features

Web app backend: Django project web pages.

Containerized deployment: Dockerized application for consistent environments.

Kubernetes deployment: Scalable deployment using Deployment and Service manifests.

CI/CD: Automated builds and deployments via GitHub Actions.

Cloud-ready: Runs on an EC2-hosted Kubernetes cluster.

## Project Structure
Menu-Django/
├── mysite/                 # Django project folder
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── requirements.txt
├── Dockerfile
├── django-deployment.yaml  # Kubernetes Deployment manifest
├── django-service.yaml     # Kubernetes Service manifest
├── .github/workflows/      # GitHub Actions CI/CD workflows
└── README.md

## Tech Stack

Programming / Frameworks: Python, Django

DevOps & CI/CD: Docker, GitHub Actions

Kubernetes: Deployments, Services, NodePort

Cloud: AWS EC2 (Kubernetes cluster)

