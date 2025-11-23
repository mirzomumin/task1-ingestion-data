# Data Ingestion Project

This project demonstrates a simple ETL (Extract, Transform, Load) pipeline. It reads data from an invalid JSON file, processes it, and loads it into a MySQL database using Python and Docker.

## Project Structure

-   `main.py`: The main script that reads, formats, and inserts the book data into the database.
-   `db.py`: Handles the database connection and creates the `books` table if it doesn't exist.
-   `task1_d.json`: The raw data file containing book information.
-   `docker-compose.yaml`: Defines the multi-container Docker application with a MySQL database service.
-   `requirements.txt`: Lists the Python dependencies for the project.
-   `.env.example`: An example file for the environment variables.
-   `.env`: A file (that you will create) to store your environment variables securely.

## Prerequisites

-   [Python](https://www.python.org/downloads/)
-   [Docker](https://docs.docker.com/get-docker/)
-   [Docker Compose](https://docs.docker.com/compose/install/)

## How to Run

1.  **Clone the repository** (or ensure you have all the project files in one directory).

2.  **Create an environment file**:
    Create a file named `.env` in the root of the project directory. Copy the contents below and replace the placeholder values with your desired database credentials.

    ```env
    # .env

    # MySQL settings
    # Use 'localhost' since the Python scripts run on the host machine
    DB_HOST=localhost
    DB_NAME=book_db
    DB_USER=user
    DB_PASS=password
    DB_ROOT_PASS=rootpassword
    DB_PORT=3306
    ```

3.  **Install Python dependencies**:
    It's recommended to use a virtual environment. Then, install the required packages.

    ```bash
    # Create and activate a virtual environment (optional but recommended)
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

    # Install dependencies
    pip install -r requirements.txt
    ```

4.  **Start the database service**:
    Open your terminal in the project's root directory and run the following command to start the MySQL container in the background.

    ```bash
    docker compose up --build -d
    ```

    This command will:
    -   Pull the MySQL image if not present.
    -   Build and start the `db` (MySQL) container.
    -   Wait a few moments for the database to initialize.

5.  **Create the database table**:
    Run the `db.py` script to connect to the database and create the `books` table.

    ```bash
    python db.py
    ```

6.  **Load the data**:
    Run the `main.py` script to read the JSON file, transform the data, and load it into the `books` table.

    ```bash
    python main.py
    ```

7.  **Verify the data** (Optional):
    You can connect to the database using a client of your choice (like DBeaver, TablePlus, or the `mysql` CLI) with the credentials you set in the `.env` file (using port `3306` on `localhost`) to verify that the `books` table has been created and populated.

8.  **Shut down the services**:
    To stop and remove the container, run:

    ```bash
    docker compose down
    ```
