## 🚨 Issues Encountered

### 🔸 AWS (DynamoDB)
- **Permission Limitations**
  - Lack of necessary IAM permissions on the DynamoDB table made it difficult to:
    - Understand the table schema (key structure).
    - Extract item values.
- **Solution**
  - After experimenting with possible key values, I discovered that the correct value was ``theDoctor`` instead of `thedoctor`.

---

### 🔸 Application Code
- **Port Conflict on Local Machine**
  - While running the app locally, I encountered:
    ```
    0.0.0.0:5000: bind: address already in use
    ```
  - Investigation using `netstat` revealed that a background process related to **Mac Control Center** (AirPlay Receiver) was already using port `5000`.
  - **Solution:**  
    - Changed the app port to `5001` to avoid conflicts.
    - Alternatively, disabling the AirPlay Receiver would also resolve it, but I opted for changing the port to avoid system changes.

---

- **Docker Context & Build Confusion**
  - Faced some recurring issues with:
    - Docker build context.
    - Correct `WORKDIR` usage.
    - Module import paths inside containers.
---
