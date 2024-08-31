## Availability API

**A simple Availability API mock project built with Flask to check property availability and check the currrent time on shortlet.app.**

This project demonstrates API development and containerization using Docker.

### Prerequisites

- **Python 3.10 or later**
- **Docker**
- **Git**

### Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/DanAletor/Availability-API.git
   ```

2. **Install Dependencies**

   ```bash
   cd Availability-API
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Run the Application**

   ```bash
   python app.py
   ```

   The API will be accessible at `http://localhost:5000/api/availability`.

4. **Run with Docker**

   ```bash
   sudo docker buildx build -t availability-api .
   sudo docker run -p 5000:5000 availability-api
   ```

   Access the API at `http://localhost:5000/api/availability?start_date=2024-09-10&end_date=2024-09-20`.

## Preview Page

The Availability API includes a preview page to test the API functionality. This page allows users to input start and end dates and view available properties.

### Accessing the Preview Page

1. Run the application (see instructions above).
2. Visit `http://localhost:5000` in your web browser.
3. Enter the start and end dates to check property availability.

The preview page dynamically fetches data from the Availability API and displays it.
