# ✅ Development Process Summary

## 🔨 Steps of the Development Process

1. **Project Setup**
   - Cloned the project under my GitHub account.
   - Stored required secrets in the GitHub repository:
     - DockerHub credentials.
     - AWS credentials.

2. **AWS & DynamoDB Integration**
   - Used Python with `boto3` to connect to DynamoDB.
   - Encountered permission issues:
     - Only allowed to use `GetItem`.
     - Initial attempts with key `'thedoctor'` returned an empty response.
   
3. **Local Development**
   - Created and ran a dummy Flask application locally for testing.

4. **DockerHub Integration**
   - Opened a DockerHub account.
   - Created a Personal Access Token (PAT) for automated pushes.

5. **Project Structure Planning**
   - Designed initial project structure with relevant folders and placeholder files.

6. **Health Check Endpoint**
   - Built logic for the `/health` endpoint.

7. **Containerization**
   - Wrote a `Dockerfile`.
   - Created a `docker-compose.yml`.
   - Verified functionality with `.env` file integration.

8. **DynamoDB Key Discovery**
   - Discovered the correct DynamoDB key (`theDoctor` — case-sensitive) through testing.

9. **Secret Endpoint**
   - Built logic for the `/secret` endpoint to fetch secret data.

10. **Verification & Testing**
    - Ensured `verifications.sh` passed successfully.

11. **CI/CD Automation**
    - Set up GitHub Actions for CI/CD pipeline:
      - Automated testing, building, and pushing Docker images.

12. **Testing & Documentation**
    - Wrote and ran tests using `pytest`.
    - Integrated tests into the CI pipeline.
    - Documented the process throughout the task.
---
