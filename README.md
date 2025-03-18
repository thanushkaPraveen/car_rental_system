
# README.md

        Thanushka Praveen Wickramarachchchi
        Student ID: 270599091

        College: Yoobee College
        Programme: Master of Software Engineering
        Course: MSE800 Professional Software Engineering
        Assignment 1: Object-Oriented Programming
        Assignment Type: Individual Project

        Date: 03-02-2025

## Car Rental System

### Project Overview

The Car Rental System automates the rental process for a fictional car rental company. By eliminating manual paperwork, it reduces errors and enhances customer satisfaction with a seamless digital experience.

### Key Objectives

- **Streamline rental management**
- **Enhance interaction between customers and administrators**
- **Provide innovative features to offer a competitive edge**


-- API - and new -- 

Python backend implementation for the car rental management system with RESTful API endpoints.

## Features

### Core Functionality
  - Secure login system
  - Admin authentication (admin@admin.com)

- **Booking Management**:
  - Car availability checking
  - Booking creation with additional services
  - Booking status updates (Pending/Confirmed/Cancelled)
  - Comprehensive booking history

- **Invoice System**:
  - Automatic invoice generation
  - Payment status tracking
  - Multi-user invoice management

- **New in v2.0.0**:
  - Enhanced security with JWT tokens
  - Rate limiting implementation
  - Improved request validation
  - Additional services management
  - Database optimization

## Changelog (v2.0.0)

### Added
- Additional services endpoints
- Email notification system

### Changed
- Improved database schema design
- RESTful endpoint structure
- Enhanced error handling
- Optimized SQL queries

### Fixed
- Date validation issues
- Concurrent booking conflicts
- Database connection pooling
- Invoice calculation errors

## Installation

1. **Clone repository**:
   ```bash
   git clone https://github.com/thanushkaPraveen/car_rental_system.git
   cd car-rental-api
   git checkout tags/v2.0.0
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Setup**:
   ```bash
   cp .env.example .env
   # Update .env with your configurations
   ```

4. **Database Migration**:
   ```bash
   alembic upgrade head
   ```

5. **Run Server**:
   ```bash
   gunicorn --bind 0.0.0.0:8000 main:app
   ```

## API Documentation


Key Endpoints:
```http
POST /api/v1/user/register
POST /api/v1/user/login
GET /api/v1/booking/get-all-cars
POST /api/v1/booking/create-a-booking
POST /api/v1/admin/update-booking-status
POST /api/v1/invoice/get-all-invoices
```
`

## Security Notes
- Change default admin credentials
- Implement rate limiting
- Validate all user inputs
- Store passwords using bcrypt

## Contributors
- [Thanushka praveen](https://github.com/thanushkaPraveen)
- [Kanishka] (https://github.com/Nirman92)
- [Vindya] (https://github.com/Vindya-Su)

## Report Issues
[GitHub Issues](https://github.com/your-username/car-rental-api/issues)


-- OLD -- 

### System Workflow

![System Workflow](docs/images/work_flow.png)

---

## Features

### Admin Features

#### Manage Customers
- **View Customers:** Display details of all registered users.
- **Delete Customers:** Remove customer records from the system.
- **View Invoices:** Access invoice history for specific customers.

#### Manage Cars
- **View All Cars:** Display a list of all cars in the system.
- **View Available Cars:** Filter and display cars currently available for rent.
- **View Booked Cars:** Filter and display cars that are already booked.
- **Add Car:** Add a new car to the inventory with details (e.g., make, model, mileage, year, etc.).
- **Edit Car:** Update details of existing cars.
- **Delete Car:** Remove a car from the inventory.

#### Manage Bookings
- **View All Bookings:** Display a list of all customer bookings.
- **Approve/Reject Bookings:** Process pending booking requests.
- **Return to Home:** Navigate back to the main admin dashboard.

#### Manage Services
- **View All Services:** Display additional services offered.
- **Requested Services:** Review and manage services requested by customers.
- **Return to Home:** Navigate back to the main admin dashboard.

#### Invoices and Payments
- **View Invoices:** Access all generated invoices (both pending and paid).
- **Return to Home:** Navigate back to the main admin dashboard.

#### Logout
- **Secure Logout:** Safely log out of the system and navigate to the first page.

### User Features

#### User Login/Register
- Users can create an account or log in to access the system.

#### Make a Booking
- **View Cars:** Users can view all available cars.
- **Select Car:** Choose a car for booking.
- **Specify Rental Duration:** Enter a rental period within the admin-set date range (minimum 1 day, maximum 30 days).
- **Input Start Date:** Provide the booking start date (format: YYYY-MM-DD).
- **Add Services:** Include additional services to the booking.
- **Review Booking:** Confirm booking details and total cost before proceeding.

#### Booking History
- Users can access and review their previous bookings.

#### Manage Invoices
- **View Invoices:** Access pending invoices and complete payments.
- **Access Paid Invoices:** View past invoices for reference.

#### Logout
- **Secure Logout:** Safely log out of the system and navigate to the first page.

---

## Technologies Used

- **Programming Language:** Python
- **Database:** MySQL
- **IDE:** PyCharm CE
- **Libraries/Frameworks:**
  - `mysql-connector-python`: For database operations
  - `bcrypt`: For secure password hashing
  - `datetime`: For managing date and time fields
  - `tabulate`: For tabular data display in CLI
  - `Flask`: For web application development
  - `requests`: For handling API calls
  - `openai`: For AI-powered features
  - `httpx`: For asynchronous HTTP requests
  - `aiohttp`: For efficient networking operations
  - `Jinja2`: For templating support
  - `Werkzeug`: For secure application handling
  - `twilio`: For SMS notifications
  - `yagmail`: For email automation

---

## System Requirements

- **Python:** 3.8 or higher
- **MySQL:** 8.0 or higher
- **IDE:** PyCharm CE or equivalent
- **Internet connection:** For downloading dependencies

---

## Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/thanushkaPraveen/car_rental_system.git
cd car_rental_system
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies

All dependencies are listed in `requirements.txt`. Install them using:

```bash
pip install -r requirements.txt
```

### 4. Set Up the Database

Install MySQL and set configurations and set your [configfile.ini](config.ini) file.

```bash
[mysql]
host = [localhost]
user = [root]
password = [password]
```

### 4. Set Up Payment Front-end implementation

- Install Apache by using [Apache](https://httpd.apache.org/docs/2.4/install.html).
- Install php by using [php.net](https://www.php.net/manual/en/install.php).
- Place your PHP files inside `/usr/local/var/www/` (macOS) `/var/www/html/` (Linux) or `/htdocs`(Windows/XAMPP)
- Copy the folder([carrentalsystem-frontend](carrentalsystem-frontend)) and contents to your host 
`./htdocs/carrentalsystem-frontend` folder.

### 5. Run the Application

To start the application, use:

```bash
python main.py
```

## Usage Instructions

### Admin Usage

#### Login
- Enter admin credentials to access the dashboard.

#### Manage Customers
- View customer records, delete customers, or view their invoices.

#### Manage Cars
- Add, edit, delete cars, or view car statuses.


#### Manage Bookings
- Approve or reject booking requests.

#### View Invoices
- Track pending and paid invoices.

### Customer Usage

#### Register/Login
- New customers can register, while returning customers can log in to their accounts.

#### Book a Car
- Browse available cars, select the rental duration, and add additional services.

#### View Booking History
- Access previous booking details, including car information, dates, and rental history.

#### Pay Invoices
- Settle pending invoices securely through the payment interface.

---

## Database Structure

### Database Schema

#### UserType
**Purpose:** Defines roles for users, such as Admin and Customer.

**Columns:**
- `user_type_id` (Primary Key): Unique identifier for user types.
- `user_type`: Name of the user type.
- `is_active`: Indicates if the record is active (1 = Active, 0 = Inactive).
- `create_at` and `updated_at`: Timestamps for record creation and modification.

#### User
**Purpose:** Stores information about system users.

**Columns:**
- `user_id` (Primary Key): Unique identifier for users.
- `user_type_id` (Foreign Key): Links to `UserType(user_type_id)`.
- `user_name`, `user_email`, `user_phone_number`, `user_password`: User details with hashed password
- `is_active`: Indicates if the user is active (1 = Active, 0 = Inactive).
- `create_at` and `updated_at`: Timestamps for record creation and modification.

#### CarType
**Purpose:** Maintains categories of cars (e.g., Sedan, SUV).

**Columns:**
- `car_type_id` (Primary Key): Unique identifier for car types.
- `car_type`: Name of the car type.
- `is_active`: Indicates if the record is active.
- `create_at` and `updated_at`: Timestamps for record creation and modification.

#### CarBrandModel
**Purpose:** Stores brand and model details of cars.

**Columns:**
- `car_brand_model_id` (Primary Key): Unique identifier for brand and model entries.
- `car_type_id` (Foreign Key): Links to `CarType(car_type_id)`.
- `brand_name`, `model_name`: Details of car brands and models.
- `is_active`: Indicates if the record is active.
- `create_at` and `updated_at`: Timestamps for record creation and modification.

#### CarStatus
**Purpose:** Tracks the status of cars (e.g., Available, Rented).

**Columns:**
- `car_status_id` (Primary Key): Unique identifier for car statuses.
- `car_status_type`: Status type.
- `is_active`: Indicates if the record is active.
- `create_at` and `updated_at`: Timestamps for record creation and modification.

#### Car
**Purpose:** Stores car inventory information.

**Columns:**
- `car_id` (Primary Key): Unique identifier for cars.
- `car_brand_model_id` (Foreign Key): Links to `CarBrandModel(car_brand_model_id)`.
- `car_status_id` (Foreign Key): Links to `CarStatus(car_status_id)`.
- Other details: `number_plate`, `model_name`, `daily_rate`, `year`, `mileage`, `min_rental_period`, `max_rental_period`.
- `is_active`: Indicates if the record is active.
- `create_at` and `updated_at`: Timestamps for record creation and modification.

#### BookingStatus
**Purpose:** Tracks the status of bookings (e.g., Pending, Confirmed).

**Columns:**
- `booking_status_id` (Primary Key): Unique identifier for booking statuses.
- `booking_status_type`: Status type.
- `is_active`: Indicates if the record is active.
- `create_at` and `updated_at`: Timestamps for record creation and modification.

#### Booking
**Purpose:** Manages customer bookings.

**Columns:**
- `booking_id` (Primary Key): Unique identifier for bookings.
- `user_id` (Foreign Key): Links to `User(user_id)`.
- `car_id` (Foreign Key): Links to `Car(car_id)`.
- `booking_status_id` (Foreign Key): Links to `BookingStatus(booking_status_id)`.
- Other details: `start_date`, `end_date`, `total_amount`, `note`.
- `is_active`: Indicates if the record is active.
- `create_at` and `updated_at`: Timestamps for record creation and modification.

#### AdditionalServices
**Purpose:** Tracks optional services for bookings (e.g., GPS, child seat).

**Columns:**
- `additional_services_id` (Primary Key): Unique identifier for additional services.
- `services_description`, `services_amount`: Service details.
- `is_active`: Indicates if the record is active.
- `create_at` and `updated_at`: Timestamps for record creation and modification.

#### BookingAdditionalServices
**Purpose:** Links additional services to bookings.

**Columns:**
- `booking_additional_charge_id` (Primary Key): Unique identifier for booking additional charges.
- `booking_id` (Foreign Key): Links to `Booking(booking_id)`.
- `additional_services_id` (Foreign Key): Links to `AdditionalServices(additional_services_id)`.
- `is_active`: Indicates if the record is active.
- `create_at` and `updated_at`: Timestamps for record creation and modification.

#### Invoice
**Purpose:** Manages payment records.

**Columns:**
- `invoice_id` (Primary Key): Unique identifier for invoices.
- `booking_id` (Foreign Key): Links to `Booking(booking_id)`.
- `user_id` (Foreign Key): Links to `User(user_id)`.
- Other details: `amount`, `payment_method`, `payment_date`, `is_paid`.
- `is_active`: Indicates if the record is active.
- `create_at` and `updated_at`: Timestamps for record creation and modification.

### Entity Relationship Diagram

![ERD Diagram](docs/images/entity_relationship_diagram.png)

### Relationships Between Tables

- **Users ↔ Booking:** One user can have many bookings.
- **Cars ↔ Booking:** One car can have multiple bookings.
- **Booking ↔ Invoice:** Each booking can have one associated invoice.
- **Users ↔ Invoice:** One user can have multiple invoices.
- **UserType ↔ Users:** One user type can be associated with multiple users.
- **CarType ↔ CarBrandModel:** One car type can be associated with multiple car brands and models.
- **CarBrandModel ↔ Cars:** One car brand/model can have multiple cars.
- **CarStatus ↔ Cars:** One car status can be associated with multiple cars.
- **BookingStatus ↔ Booking:** One booking status can be associated with multiple bookings.
- **Booking ↔ BookingAdditionalServices:** One booking can have multiple additional services.
- **AdditionalServices ↔ BookingAdditionalServices:** One additional service can be associated with multiple bookings.

### Database Screenshots

**NOTE:** All database-related queries can be checked in the `sql_statement` file.

---

## Architecture Patterns

- **MVC:** Model-View-Controller (MVC) Architecture.
- **Model:** Data & Business Logic - The Model represents the data, business logic, and rules of the application. It 
communicates with the database and processes the data.
- **View:** User Interface (UI) - The View is responsible for displaying data and rendering the user interface. It 
interacts with the Model indirectly through the Controller.
- **Controller:** Controller (C) - Handles User Interaction - The Controller acts as a mediator between the Model and 
the View. It processes user input, retrieves data from the Model, and updates the View accordingly.

---

## Design Patterns

- **Factory Pattern:** Used for dynamically creating database connection instances.
- **Singleton Pattern:** Ensures that only one database connection instance exists at any given time.
- **Observer Pattern:** Facilitates notification of users about booking status changes (e.g., via email).

---

## Future Enhancements

- **AI-Powered Recommendations:** Suggest cars to users based on their preferences.
- **Mobile Integration:** Develop a Flutter-based mobile application.
- **Dynamic Pricing:** Implement surge pricing during high-demand periods.
- **Real-Time Notifications:** Use APIs for updates and reminders.
- **Dynamic Search:** Add filters for price range, car type, mileage, and availability.
- **Multi-language Support:** Offer a language selector.
- **Multi-currency Support:** Enable payments in different currencies.

---

## Testing and Debugging

### Testing

- **Integration Testing:** Ensures end-to-end workflows function correctly.
- **Manual Testing:** Verifies CLI functionality for various inputs.

### Debugging

- **Logging:** Use logging for database operations and exception handling.
- **Configuration Validation:** Validate configurations before deployment.

---

## Contributing

We welcome contributions to improve this project. Follow these steps to contribute:

1. **Fork the repository.**
2. **Create a feature branch:**
   ```bash
   git checkout -b feature-name
   ```
3. **Commit your changes:**
   ```bash
   git commit -m "Add feature-name"
   ```
4. **Push to the branch:**
   ```bash
   git push origin feature-name
   ```
5. **Open a Pull Request.**

---

##Documentation

**README.md**: A comprehensive guide containing setup instructions, usage details, and system information.  

**README.pdf**: A detailed guide with complete information, including screenshots, setup instructions, usage details, and system specifications.  

**System Document**: This document provides a detailed explanation of the system’s design and architecture using UML diagrams. It includes:  
- **Class Diagram** – Illustrates system structure and relationships.  
- **Use Case Diagram** – Defines user interactions.  
- **Sequence Diagram** – Depicts the flow of operations.  

These diagrams ensure a clear understanding of system functionality and interactions.  

**Maintenance and Support**: This document outlines a structured approach to software maintenance, versioning, and backward compatibility. It ensures software stability, regular updates, and long-term support.  

 Note: All PDF-related files for this project 
              are maintained using the LaTeX Overleaf tool.
---

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

---

## Credits

- **Developer:** Thansushka Praveen Wickramarachchi
- **Contact:** [270599091@yoobeestudent.ac.nz](mailto:270599091@yoobeestudent.ac.nz)
- **GitHub:** [https://github.com/thanushkaPraveen](https://github.com/thanushkaPraveen)

---

## Acknowledgments

Special thanks to **Yoobee College** for guidance and resources in software development.




