# Multilingual Number to Text Converter

This is a FastAPI-based application that converts numbers into their text representation in various languages. It leverages the `num2words` library to provide support for multiple languages.

## Features
- Convert numbers to words in multiple languages.
- RESTful API with a single endpoint for conversion.
- Error handling for unsupported languages and unexpected issues.
- Dockerized for easy deployment.
- Kubernetes configuration for scalable deployment.

## Technologies Used
- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python.
- **Pydantic**: For data validation and settings management using Python type annotations.
- **num2words**: A library to convert numbers to their word representation in various languages.
- **Docker**: For containerization.
- **Kubernetes**: For container orchestration.

## API Endpoints
### POST `/convert`
Converts a number to its text representation in the specified language.

#### Request Body (JSON):
```json
{
    "number": 123,
    "language": "en"
}
```
- `number` (required): The number to be converted.
- `language` (optional): The language code (e.g., `en` for English, `fr` for French). Defaults to English if not provided.

#### Response (JSON):
```json
{
    "number": 123,
    "text": "one hundred and twenty-three",
    "language": "en"
}
```

#### Error Responses:
- **400 Bad Request**: If the specified language is not supported.
- **500 Internal Server Error**: For any unexpected issues.

## Getting Started

### Prerequisites
- Python 3.12 or later
- Docker
- Kubernetes (Minikube recommended for local testing)

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd multilingual-number-to-text
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Testing
Run the test suite using `pytest`:
```bash
python -m pytest
```

## Deployment

### Docker
1. Build the Docker image:
   ```bash
   docker build -t multilingual-number-to-text:latest -f Dockerfile .
   ```
2. Run the Docker container:
   ```bash
   docker run -p 8000:8080 multilingual-number-to-text:latest
   ```
3. Access the application at `http://localhost:8000/docs`.

### Kubernetes
1. Start Minikube:
   ```bash
   minikube start
   ```
2. Load the Docker image into Minikube:
   ```bash
   minikube image load multilingual-number-to-text:latest
   ```
3. Apply Kubernetes configurations:
   ```bash
   kubectl apply -f k8s
   ```
4. Forward the port to access the application:
   ```bash
   kubectl port-forward deployment/multilingual-number-to-text 8000:8080
   ```
5. Access the application at `http://localhost:8000/docs`.

## Example Usage
### Request:
```bash
curl -X POST "http://127.0.0.1:8000/convert" \
-H "Content-Type: application/json" \
-d '{"number": 123, "language": "en"}'
```

### Response:
```json
{
    "number": 123,
    "text": "one hundred and twenty-three",
    "language": "en"
}
```
