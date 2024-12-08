# CI/CD Pipeline for Flask Application

This repository contains a CI/CD pipeline for a Flask application. The pipeline automates testing, Docker image creation, artifact handling, and deployment to a Kubernetes cluster using Helm.

---

## Features

- **Continuous Integration (CI):**
  - Runs unit tests for the Flask application using `pytest`.
  - Builds a Docker image of the application.
  - Scans the Docker image for vulnerabilities using Trivy (optional).
  - Pushes the Docker image to DockerHub.
  - Packages Helm charts and uploads them as artifacts.

- **Continuous Deployment (CD):**
  - Deploys the Flask application to a local Kubernetes cluster using `kind` (Kubernetes in Docker).
  - Supports optional deployment with manually specified Docker image tags.
  - Tests the deployed application to ensure successful deployment.

---

## Folder Structure

```plaintext
.
├── app/                      # Flask application code
│   ├── tests/                # Unit tests for the Flask app
│   └── requirements.txt      # Python dependencies
├── helm/                     # Helm chart for the application
│   ├── templates/            # Kubernetes manifests (deployment, service, etc.)
│   └── values.yaml           # Helm chart default values
├── .github/workflows/        # GitHub Actions workflows
│   ├── ci.yml                # CI pipeline
│   └── cd.yml                # CD pipeline
└── README.md                 # Project documentation
