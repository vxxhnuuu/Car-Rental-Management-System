# Car Rental Management System

## Overview
The Car Rental Management System is a web application built using Flask and MySQL that allows users to rent cars, manage rentals, and view available cars. The system provides functionalities for both customers and administrators, ensuring an efficient car rental experience.

## Features
- **User Authentication**: Users can log in to the system.
- **Car Management**: Administrators can add new cars to the inventory.
- **Available Cars**: Users can view cars that are currently available for rent.
- **Rental Process**: Users can rent cars and provide their details for the rental.
- **Return Car**: Users can return rented cars, making them available for others.

## Technologies Used
- **Flask**: Web framework for building the application.
- **MySQL**: Database for storing user and car information.
- **dotenv**: For managing environment variables.

## Installation

### Prerequisites
- Python 3.x
- MySQL Server
- pip

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/vxxhnuuu/Car-Rental-Management-System.git
   cd Car-Rental-Management-System
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

5. Set up the environment variables:
   Create a `.env` file in the root directory and add the following:
   ```env
   DB_HOST=localhost
   DB_USER=root
   DB_PASSWORD=your_password_here
   DB_NAME=car_rental_management_system
   ```

6. Set up the MySQL database:
   - Create a database named `car_rental_management_system`.
   - Create the necessary tables as per the project requirements.

## Usage
- Run the application:
  ```bash
  python app.py
  ```
- Open your browser and go to `http://127.0.0.1:5000` to access the application.

## Directory Structure
```
Car-Rental-Management-System/
├── app.py
├── requirements.txt
├── .env
├── routes/
│   ├── __init__.py
│   ├── auth.py
│   ├── car.py
│   ├── rental.py
├── templates/
│   ├── login.html
│   ├── index.html
│   ├── add_car.html
│   ├── available_car.html
│   ├── rent.html
│   ├── return.html
└── static/
    └── styles.css
```

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Thanks to the Flask community for their support and documentation.
- MySQL for the robust database management.
