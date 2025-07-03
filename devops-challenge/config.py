import os

IMAGE_REPOSITORY = os.getenv("IMAGE_REPOSITORY", "https://hub.docker.com/repository/docker/roiko5/devops-exercise/")
GITHUB_REPOSITORY = os.getenv("GITHUB_REPOSITORY", "https://github.com/roiko2/devops-challenge")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID", "")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY", "")
AWS_REGION = os.getenv("AWS_REGION", "eu-west-1")
TABLE_NAME = os.getenv("TABLE_NAME", "devops-challenge")