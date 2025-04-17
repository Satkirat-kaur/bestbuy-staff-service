## FINAL EXAM

### 1. Develop the Staff-Service Microservice 
- Built a lightweight RESTful microservice using **Python + Flask**
- Provided CRUD APIs to manage in-memory staff data
- Used environment variables for configuration (12-factor app principle)
# BestBuy Staff-Service 🧑‍💼

The **BestBuy Staff-Service** is a microservice designed to manage internal staff information. It provides RESTful APIs for CRUD operations (Create, Read, Update, Delete) using Python and Flask. Staff data is stored in memory and the service follows 12-Factor App principles.

---

## Features

- Create, read, update, and delete staff records
- Follows RESTful API design
- Lightweight Flask backend
- Deployed to Azure Kubernetes Service (AKS)
- Dockerized for portability
- CI/CD pipeline via GitHub Actions

---

## API Endpoints

| Method | Endpoint        | Description            |
|--------|------------------|------------------------|
| GET    | `/staff`         | Get all staff          |
| POST   | `/staff`         | Add new staff          |
| PUT    | `/staff/<id>`    | Update staff by ID     |
| DELETE | `/staff/<id>`    | Delete staff by ID     |

###  Sample JSON for POST:
```json
{
  "name": "John Doe",
  "position": "Sales Associate",
  "department": "Electronics",
  "email": "john.doe@bestbuy.com",
  "phone": "123-456-7890"
}
```

### 2. Containerize the Service
- Wrote a `Dockerfile` for the Flask service
- Built and tested the Docker image locally
- Pushed the image to Docker Hub:  
https://hub.docker.com/repository/docker/satkiratkaur/bestbuy-staff-service/general

- Committed Dockerfile with message: `Adding Dockerfile`

### 3. Deploy to Azure Kubernetes Service 
- Created AKS cluster via Azure CLI
- Generated and applied `deployment.yaml` with LoadBalancer service
- Deployed the containerized microservice to AKS
- Verified deployment and external IP with `kubectl get svc`
- Committed deployment file with: `Adding AKS deployment file`

  ![Alt Text](https://github.com/Satkirat-kaur/bestbuy-staff-service/blob/main/screenshots/aks%20pods%20running.png)
![Alt Text](https://github.com/Satkirat-kaur/bestbuy-staff-service/blob/main/screenshots/azure%20cluster.png)
![Alt Text](https://github.com/Satkirat-kaur/bestbuy-staff-service/blob/main/screenshots/final%20result%20on%20browser.png)


### 4. Set Up CI/CD Pipeline
- Created a GitHub Actions workflow (`ci_cd.yaml`)
- Configured secrets: `DOCKER_USERNAME`, `DOCKER_PASSWORD`, `KUBE_CONFIG_DATA`
- Automated build, push to Docker Hub, and deployment to AKS
- Verified workflow jobs on GitHub Actions
- Committed pipeline with: `Adding CI/CD pipeline`

![Alt Text](https://github.com/Satkirat-kaur/bestbuy-staff-service/blob/main/screenshots/github%20workflow.png)  





