# Todo List API

## Overview

This is a simple Todo List API built using Flask. It allows users to add tasks to a todo list and retrieve the current list of todos via HTTP requests. This project serves as a foundational backend service and will later evolve into the "Product Inventory API" in a larger e-commerce project.

## Technologies Used

- Python
- Flask
- Postman (for API testing)

## Features

- **GET /todos**: Retrieve the list of current todos in JSON format.
- **POST /todos**: Add a new todo item by sending a JSON payload.

## Postman Collection

The included Postman collection (`New Collection.postman_collection.json`) contains preconfigured requests for the API endpoints to help you quickly test the API functionality.

### How to use the Postman Collection:

1. Download or clone this repository.
2. Open Postman.
3. Click **Import**.
4. Choose the `New Collection.postman_collection.json` file from this repository.
5. Send requests and see responses to test the API.

## Setup and Run

1. **Install Python** (if not installed):
   Download from [python.org](https://www.python.org/downloads/).

2. **Install Flask**:
   ```bash
   pip install flask
