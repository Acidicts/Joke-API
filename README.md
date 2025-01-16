Here is the documentation for the Jokes API:

# Jokes API Documentation

## Base URL
```
https://joke-api-azure.vercel.app/
```

## Endpoints

### 1. Home
- **URL:** `/`
- **Method:** `GET`
- **Description:** Returns a welcome message and a list of available endpoints.
- **Response:**
  ```json
  {
    "message": "Welcome to the Jokes API",
    "endpoints": ["/random", "/get", "/add"]
  }
  ```

### 2. Get All Jokes
- **URL:** `/all`
- **Method:** `GET`
- **Description:** Retrieves all jokes from the database.
- **Response:**
  - **Success (200):**
    ```json
    {
      "jokes": ["Joke 1", "Joke 2", ...],
      "ids": [1, 2, ...]
    }
    ```
  - **Failure (404):**
    ```json
    {
      "message": "No jokes found"
    }
    ```

### 3. Get Random Joke
- **URL:** `/random`
- **Method:** `GET`
- **Description:** Retrieves a random joke from the database.
- **Response:**
  - **Success (200):**
    ```json
    {
      "joke": "Random Joke",
      "id": 1
    }
    ```
  - **Failure (404):**
    ```json
    {
      "message": "No jokes found"
    }
    ```

### 4. Get Joke by ID
- **URL:** `/get`
- **Method:** `GET`
- **Description:** Retrieves a joke by its ID.
- **Query Parameters:**
  - `id` (required): The ID of the joke to retrieve.
- **Response:**
  - **Success (200):**
    ```json
    {
      "joke": "Joke content"
    }
    ```
  - **Failure (404):**
    ```json
    {
      "message": "No jokes found"
    }
    ```

### 5. Add a New Joke
- **URL:** `/add`
- **Method:** `POST`
- **Description:** Adds a new joke to the database.
- **Request Body:**
  ```json
  {
    "content": "New joke content"
  }
  ```
- **Response:**
  - **Success (201):**
    ```json
    {
      "message": "Joke added successfully",
      "id": 1
    }
    ```
  - **Failure (400):**
    ```json
    {
      "message": "Invalid request"
    }
    ```

### 6. Delete a Joke
- **URL:** `/delete`
- **Method:** `DELETE`
- **Description:** Deletes a joke by its ID.
- **Request Body:**
  ```json
  {
    "id": 1
  }
  ```
- **Response:**
  - **Success (200):**
    ```json
    {
      "message": "Joke deleted successfully"
    }
    ```
  - **Failure (400):**
    ```json
    {
      "message": "Invalid request"
    }
    ```
  - **Failure (404):**
    ```json
    {
      "message": "No jokes found"
    }
    ```