# 🚀 Project Instructions

This guide explains how to build, run, and verify the project locally using **Docker Compose**.

---

## ⚙️ Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed and running.
- [Docker Compose](https://docs.docker.com/compose/) installed.
- AWS credentials with access to the required DynamoDB table.

---

## 📄 Environment Variables

Before running the project, you need to provide AWS credentials.

1. Copy the provided `.env.example` file:
```bash
cp .env.example .env
```

Fill in your AWS credentials in the .env file (keys will be provided by me):
```
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
```

## 📦 Running the Project

To build and start the app locally:

```docker-compose up --build -d```
> App will be running on port 5001

## 🔎 Verifying the Application
After the app is running, you can verify it using the provided verification.sh script:
```commandline
chmod +x verification.sh
./verification.sh
```

## ✅ Notes
- Make sure port 5001 is available on your machine.
- The DynamoDB key must exist and match exactly (case-sensitive) for the /secret endpoint to work properly.