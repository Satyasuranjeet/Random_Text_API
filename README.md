
# Random Text Generation API

This is a simple Python API built using Flask that generates random text, including words, sentences, and paragraphs. It also includes a basic health-check route to confirm the system is working.

## Features

- **Generate Random Text**: Generate random words, sentences, or paragraphs.
- **Health-Check Route**: A route to verify if the system is up and running.

## Requirements

Before running the project, make sure you have the following installed:

- **Python 3.x**: [Download Python](https://www.python.org/downloads/)
- **Flask**: Python web framework

You can install the dependencies listed in the `requirements.txt` file by running:

```bash
pip install -r requirements.txt
```

## Installation

1. Clone the repository or download the code to your local machine.

2. Navigate to the project folder and install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:

   ```bash
   python random_text_api.py
   ```

4. The API will be accessible at `http://127.0.0.1:5000/`.

## API Endpoints

### 1. Health-Check Route
- **GET** `/`
  - **Description**: Check if the system is running properly.
  - **Parameters**: None
  - **Response**:
    ```json
    {
      "message": "System is working properly!"
    }
    ```

### 2. Generate Random Text
You can access the `/generate` route with parameters to generate random text. The endpoint allows you to specify the type and length of the text.

- **Random words**: Generates a list of random words.
  - Example: Generate 5 random words:
    ```
    http://127.0.0.1:5000/generate?length=5&type=word
    ```
    - **Response**:
      ```json
      {
        "text": "lorem ipsum dolor sit amet consectetur adipiscing elit"
      }
      ```

- **Random sentences**: Generates random sentences.
  - Example: Generate 3 random sentences:
    ```
    http://127.0.0.1:5000/generate?length=3&type=sentence
    ```
    - **Response**:
      ```json
      {
        "text": "Lorem ipsum dolor sit amet. Consectetur adipiscing elit. Sed do eiusmod tempor incididunt."
      }
      ```

- **Random paragraphs**: Generates random paragraphs.
  - Example: Generate 2 random paragraphs:
    ```
    http://127.0.0.1:5000/generate?length=2&type=paragraph
    ```
    - **Response**:
      ```json
      {
        "text": "Lorem ipsum dolor sit amet. Consectetur adipiscing elit. Sed do eiusmod tempor incididunt.\n\nLorem ipsum dolor sit amet. Consectetur adipiscing elit. Sed do eiusmod tempor incididunt."
      }
      ```

### 3. Generate Random Words
- **GET** `/generate/words`
  - **Description**: Generate random words.
  - **Parameters**:
    - `length` (integer, optional): The number of words to generate. Default is 10.
  - **Response**:
    - Example:
      ```json
      {
        "text": "lorem ipsum dolor sit amet consectetur adipiscing elit"
      }
      ```

### 4. Generate Random Sentences
- **GET** `/generate/sentences`
  - **Description**: Generate random sentences.
  - **Parameters**:
    - `length` (integer, optional): The number of sentences to generate. Default is 3.
  - **Response**:
    - Example:
      ```json
      {
        "text": "Lorem ipsum dolor sit amet. Consectetur adipiscing elit. Sed do eiusmod tempor incididunt."
      }
      ```

### 5. Generate Random Paragraphs
- **GET** `/generate/paragraphs`
  - **Description**: Generate random paragraphs.
  - **Parameters**:
    - `length` (integer, optional): The number of paragraphs to generate. Default is 2.
  - **Response**:
    - Example:
      ```json
      {
        "text": "Lorem ipsum dolor sit amet. Consectetur adipiscing elit. Sed do eiusmod tempor incididunt.\n\nLorem ipsum dolor sit amet. Consectetur adipiscing elit. Sed do eiusmod tempor incididunt."
      }
      ```

## Example Requests

### 1. Random Words
To generate 5 random words:
```
http://127.0.0.1:5000/generate?length=5&type=word
```

### 2. Random Sentences
To generate 3 random sentences:
```
http://127.0.0.1:5000/generate?length=3&type=sentence
```

### 3. Random Paragraphs
To generate 2 random paragraphs:
```
http://127.0.0.1:5000/generate?length=2&type=paragraph
```

### 4. Random Words (Using `/generate/words` route)
To generate 5 random words using the specific `/generate/words` endpoint:
```
http://127.0.0.1:5000/generate/words?length=5
```

### 5. Random Sentences (Using `/generate/sentences` route)
To generate 3 random sentences using the specific `/generate/sentences` endpoint:
```
http://127.0.0.1:5000/generate/sentences?length=3
```

### 6. Random Paragraphs (Using `/generate/paragraphs` route)
To generate 2 random paragraphs using the specific `/generate/paragraphs` endpoint:
```
http://127.0.0.1:5000/generate/paragraphs?length=2
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Happy coding! If you have any questions, feel free to open an issue or submit a pull request.
```

### What's New:
- The section under **Generate Random Text** has been added to clarify how to use the `/generate` route for random words, sentences, and paragraphs.
- Each type of text generation (`word`, `sentence`, and `paragraph`) is described along with the example URLs and the expected response format.
