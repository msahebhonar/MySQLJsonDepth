# MySQLJsonDepth
This project demonstrates the process of generating and storing deeply nested JSON structures in MySQL 8 using SQLAlchemy and Python. It explores the capabilities of MySQL's JSON column type, testing the practical depth and limits of nested JSON storage.

## Example Nested JSON Structure:
```json
{
  "level_0": {
    "level_1": {
      "level_2": {
        ...
      }
    }
  }
}
```

## Setup and Installation
1. Clone the Repository:
    ```shell
    https://github.com/msahebhonar/MySQLJsonDepth.git
    ```

2. Start the MySQL Database:
    ```shell
    docker compose up -d
    ```

3. Install Python Dependencies:
    ```python
    pip install -r requirements.txt
    ```

4. Run the Project
    ```python
    python -m app.main
    ```
