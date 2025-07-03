## Issues
- AWS
  - Lack of permissions regarding DynamoDB table caused difficulty to understand the scheme and to extract Item value
- Code
  - Once running the app locally i got  ` 0.0.0.0:5000: bind: address already in use`
    - Investigated with `netstat`, found a process which turns out to be my `Mac Control Center`
    - Either changing the app port or turn off a specific feature of AirPlay receiver solve the issue, decided to change the port to `5001`
  - Issues with docker context when running the app and/or installing packages, always a bit confusing.