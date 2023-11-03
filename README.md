# Asynchronous Data Retrieval Project

## Overview
This project provides a solution for asynchronous data retrieval from multiple sources using FastAPI and SQLite. The primary goal is to create a single access point to retrieve data from three different data sources asynchronously, combine the results, and return them sorted by ID.


### Asynchronous Data Retrieval

1. **Data Sources**
   - There are three data sources, each represented as a simple table with an "id" and a "name" field.

   - Example Table Structure:
     ```sql
     CREATE TABLE data_1 (
         id INT PRIMARY KEY,
         name VARCHAR(255)
     );
     ```

   - ID Distribution Across Sources:
     - 1st source: IDs 1-10, 31-40
     - 2nd source: IDs 11-20, 41-50
     - 3rd source: IDs 21-30, 51-60

2. **Common Access Point**
   - There is a single common access point to these data sources through a Flask/FastAPI application.

   - Example Result Format:
     ```json
     [
         {"id": 1, "name": "Test 1"},
         {"id": 2, "name": "Test 2"}
     ]
     ```

3. **Asynchronous Data Retrieval**
   - The access point makes asynchronous requests to all data sources and waits for the results from all of them.

4. **Data Aggregation**
   - Upon receiving the results from all sources, the application returns the data sorted by ID (data from all sources).

5. **Error Handling**
   - Errors from any of the sources are ignored and interpreted as missing data.

   - A timeout, set to 2 seconds, is considered an error.

6. **Unit Tests**
   - Comprehensive unit tests are provided to cover all added logic.

   - Mocks are used for database connections to ensure testability.

7. **Use of ORM and Raw SQL**
   - The project demonstrates the use of both Object-Relational Mapping (ORM) and raw SQL for database interaction.

8. **Documentation and Typing Annotations**
   - The code includes comments, docstrings, and typing annotations for improved clarity and maintainability.

## Usage

TODO
