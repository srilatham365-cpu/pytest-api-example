# Petstore API Testing

A simple API testing project using pytest to test a Flask-based Petstore API.

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the API server:**
   ```bash
   python app.py
   ```
   The API will be available at `http://localhost:5000` with Swagger UI.

3. **Run the tests:**
   ```bash
   pytest -v --html=report.html
   ```
   This generates an HTML test report in `report.html`.

## What's Tested

- Pet schema validation
- Finding pets by status (available, sold, pending)
- 404 error handling for non-existent pets
- Order creation and status updates via PATCH

## Project Structure

- `app.py` - Flask API server
- `test_pet.py` - Pet-related API tests
- `test_store.py` - Store/order-related API tests
- `api_helpers.py` - Helper functions for API requests
- `schemas.py` - JSON schemas for validation
