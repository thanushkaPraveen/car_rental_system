#sql_statement.py

CREATE_USER_TYPE_TABLE  = """
CREATE TABLE IF NOT EXISTS UserType (
  user_type_id INT AUTO_INCREMENT PRIMARY KEY,
  user_type VARCHAR(45) NOT NULL,
  is_active TINYINT(1) DEFAULT 1,
  create_at INT NOT NULL,
  updated_at INT NOT NULL
);
"""

CREATE_USER_TABLE  = """
CREATE TABLE IF NOT EXISTS User (
  user_id INT AUTO_INCREMENT PRIMARY KEY,
  user_type_id INT NOT NULL,
  user_name VARCHAR(45) NOT NULL,
  user_email VARCHAR(45) NOT NULL,
  user_phone_number VARCHAR(45) NOT NULL,
  user_password VARCHAR(255) NOT NULL,
  is_active TINYINT(1) DEFAULT 1,
  create_at INT NULL,
  updated_at INT NULL,
    CONSTRAINT fk_user_type FOREIGN KEY (user_type_id) REFERENCES UserType(user_type_id)
);
"""

CREATE_CAR_TYPE_TABLE  = """
CREATE TABLE IF NOT EXISTS CarType (
  car_type_id INT AUTO_INCREMENT PRIMARY KEY,
  car_type VARCHAR(45) NOT NULL,
  is_active TINYINT(1) DEFAULT 1,
  create_at INT NOT NULL,
  updated_at INT NOT NULL
);
"""

CREATE_CAR_BRAND_MODEL_TABLE  = """
CREATE TABLE IF NOT EXISTS CarBrandModel (
  car_brand_model_id INT AUTO_INCREMENT PRIMARY KEY,
  car_type_id INT NOT NULL,
  brand_name VARCHAR(45) NOT NULL,
  model_name VARCHAR(45) NOT NULL,
  is_active TINYINT(1) DEFAULT 1,
  create_at INT NULL,
  updated_at INT NULL,
    CONSTRAINT fk_car_type FOREIGN KEY (car_type_id) REFERENCES CarType(car_type_id)
);
"""

CREATE_CAR_STATUS_TABLE  = """
CREATE TABLE IF NOT EXISTS CarStatus (
  car_status_Id INT AUTO_INCREMENT PRIMARY KEY,
  car_status_type VARCHAR(45) NOT NULL,
  is_active TINYINT(1) DEFAULT 1,
  create_at INT NULL,
  updated_at INT NULL
);
"""

CREATE_CAR_TABLE  = """
CREATE TABLE IF NOT EXISTS Car (
  car_Id INT AUTO_INCREMENT PRIMARY KEY,
  car_brand_model_id INT NOT NULL,
  car_status_Id INT NOT NULL,
  number_plate VARCHAR(45) NOT NULL,
  model_name VARCHAR(45) NULL,
  daily_rate VARCHAR(45) NOT NULL,
  year VARCHAR(45) NOT NULL,
  mileage VARCHAR(45) NOT NULL,
  min_rental_period VARCHAR(45) NOT NULL,
  max_rental_period VARCHAR(45) NOT NULL,
  is_active TINYINT(1) DEFAULT 1,
  create_at INT NULL,
  updated_at INT NULL,
    CONSTRAINT fk_car_brand FOREIGN KEY (car_brand_model_id) REFERENCES CarBrandModel(car_brand_model_id),
    CONSTRAINT fk_car_status FOREIGN KEY (car_status_Id) REFERENCES CarStatus(car_status_Id)
);
"""

CREATE_BOOKING_STATUS_TABLE  = """
CREATE TABLE IF NOT EXISTS BookingStatus (
  booking_status_id INT AUTO_INCREMENT PRIMARY KEY,
  booking_status_type VARCHAR(45) NOT NULL,
  is_active TINYINT(1) DEFAULT 1,
  create_at INT NULL,
  updated_at INT NULL
);
"""

CREATE_BOOKING_TABLE  = """
CREATE TABLE IF NOT EXISTS Booking (
  booking_id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT NOT NULL,
  car_id INT NOT NULL,
  booking_status_id INT NOT NULL,
  start_date INT NOT NULL,
  end_date INT NOT NULL,
  total_amount DOUBLE NOT NULL,
  note VARCHAR(45) NOT NULL,
  is_active TINYINT(1) DEFAULT 1,
  create_at INT NULL,
  updated_at INT NULL,
    CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES User(user_id),
    CONSTRAINT fk_car FOREIGN KEY (car_id) REFERENCES Car(car_id),
    CONSTRAINT fk_booking_status FOREIGN KEY (booking_status_id) REFERENCES BookingStatus(booking_status_id)
);
"""

CREATE_ADDITIONAL_SERVICE_TABLE  = """
CREATE TABLE IF NOT EXISTS AdditionalServices (
  additional_services_id INT AUTO_INCREMENT PRIMARY KEY,
  services_description VARCHAR(255) NULL,
  services_amount DOUBLE NOT NULL,
  is_active TINYINT(1) DEFAULT 1,
  create_at INT NULL,
  updated_at INT NULL
);
"""

CREATE_BOOKING_ADDITIONAL_SERVICE_TABLE  = """
CREATE TABLE IF NOT EXISTS BookingAdditionalServices (
  booking_additional_charge_id INT AUTO_INCREMENT PRIMARY KEY,
  booking_id INT NOT NULL,
  additional_services_id INT NOT NULL,
  is_active TINYINT(1) DEFAULT 1,
  create_at INT NULL,
  updated_at INT NULL,
    CONSTRAINT fk_booking FOREIGN KEY (booking_id) REFERENCES Booking(booking_id),
    CONSTRAINT fk_additional_services FOREIGN KEY (additional_services_id) REFERENCES AdditionalServices(additional_services_id)
);
"""
CREATE_INVOICE_TABLE  = """
CREATE TABLE IF NOT EXISTS Invoice (
  invoice_id INT AUTO_INCREMENT PRIMARY KEY,
  booking_id INT NOT NULL,
  user_id INT NOT NULL,
  amount DOUBLE NOT NULL,
  payment_method VARCHAR(45) NULL,
  payment_date INT NULL,
  is_paid TINYINT(1) DEFAULT 0,
  is_active TINYINT(1) DEFAULT 1,
  create_at INT NULL,
  updated_at INT NULL,
    CONSTRAINT fk_booking_invoice FOREIGN KEY (booking_id) REFERENCES Booking(booking_id),
    CONSTRAINT fk_user_invoice FOREIGN KEY (user_id) REFERENCES User(user_id)
);
"""

# UserType Table
INSERT_USER_TYPE = "INSERT INTO UserType (user_type, is_active, create_at, updated_at) VALUES (%s, %s, %s, %s)"
UPDATE_USER_TYPE = "UPDATE UserType SET user_type = %s, is_active = %s, updated_at = %s WHERE user_type_id = %s"
DELETE_USER_TYPE = "DELETE FROM UserType WHERE user_type_id = %s"
SELECT_ALL_USER_TYPES = "SELECT * FROM UserType"
SELECT_ALL_BY_USER_TYPES_ID = "SELECT * FROM UserType WHERE user_type_id = %s"

# User Table
INSERT_USER = "INSERT INTO User (user_type_id, user_name, user_email, user_phone_number, user_password, is_active, create_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
UPDATE_USER = "UPDATE User SET user_name = %s, user_email = %s, user_phone_number = %s, user_password = %s, is_active = %s, updated_at = %s WHERE user_id = %s"
DELETE_USER = "DELETE FROM User WHERE user_id = %s"
SELECT_ALL_USERS = "SELECT * FROM User"
SELECT_USER_BY_ID = "SELECT * FROM User WHERE user_id = %s"
SELECT_USERS_BY_USER_TYPE_ID = "SELECT * FROM User WHERE user_type_id = %s"
FIND_USER_BY_EMAIL = "SELECT * FROM User WHERE user_email = %s"
FIND_USER_BY_EMAIL_AND_PASSWORD = "SELECT * FROM User WHERE user_email = %s AND user_password = %s"
FIND_USER_BY_USER_TYPE = "SELECT User.user_id, User.user_name, User.user_email, User.user_phone_number FROM User JOIN UserType ON User.user_type_id = UserType.user_type_id WHERE UserType.user_type =%s AND User.is_active=1;"
FIND_USER_BY_BOOKING_ID = "SELECT User.user_id, User.user_name, User.user_email, User.user_phone_number FROM User JOIN Booking ON User.user_id = Booking.user_id WHERE Booking.booking_id =%s AND User.is_active=1;;"

# CarType Table
INSERT_CAR_TYPE = "INSERT INTO CarType (car_type, is_active, create_at, updated_at) VALUES (%s, %s, %s, %s)"
UPDATE_CAR_TYPE = "UPDATE CarType SET car_type = %s, is_active = %s, updated_at = %s WHERE car_type_id = %s"
DELETE_CAR_TYPE = "DELETE FROM CarType WHERE car_type_id = %s"
SELECT_ALL_CAR_TYPES = "SELECT * FROM CarType"
SELECT_CAR_TYPE_BY_ID = "SELECT * FROM CarType WHERE car_type_id = %s"

# CarBrandModel Table
INSERT_CAR_BRAND_MODEL = "INSERT INTO CarBrandModel (car_type_id, brand_name, model_name, is_active, create_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s)"
UPDATE_CAR_BRAND_MODEL = "UPDATE CarBrandModel SET brand_name = %s, model_name = %s, is_active = %s, updated_at = %s WHERE car_brand_model_id = %s"
DELETE_CAR_BRAND_MODEL = "DELETE FROM CarBrandModel WHERE car_brand_model_id = %s"
SELECT_ALL_CAR_BRAND_MODELS = "SELECT * FROM CarBrandModel"
SELECT_CAR_BRAND_MODEL_BY_ID = "SELECT * FROM CarBrandModel WHERE car_brand_model_id = %s"
SELECT_CAR_BRAND_MODELS_BY_CAR_TYPE_ID = "SELECT * FROM CarBrandModel WHERE car_type_id = %s"
SELECT_CAR_BRANDS_WITH_TYPE = """SELECT CarBrandModel.car_brand_model_id AS index_id, CarType.car_type AS car_type, CarBrandModel.brand_name AS brand_name, CarBrandModel.model_name AS model_name FROM CarBrandModel JOIN CarType ON CarBrandModel.car_type_id = CarType.car_type_id WHERE CarBrandModel.is_active = 1 AND CarType.is_active = 1;"""

# CarStatus Table
INSERT_CAR_STATUS = "INSERT INTO CarStatus (car_status_type, is_active, create_at, updated_at) VALUES (%s, %s, %s, %s)"
UPDATE_CAR_STATUS = "UPDATE CarStatus SET car_status_type = %s, is_active = %s, updated_at = %s WHERE car_status_id = %s"
DELETE_CAR_STATUS = "DELETE FROM CarStatus WHERE car_status_id = %s"
SELECT_ALL_CAR_STATUSES = "SELECT * FROM CarStatus"
SELECT_CAR_STATUS_BY_ID = "SELECT * FROM CarStatus WHERE car_status_id = %s"

# Car Table
INSERT_CAR = "INSERT INTO Car (car_brand_model_id, car_status_id, number_plate, model_name, daily_rate, year, mileage, min_rental_period, max_rental_period, is_active, create_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
UPDATE_CAR = "UPDATE Car SET car_brand_model_id = %s, car_status_id = %s, number_plate = %s, model_name = %s, daily_rate = %s, year = %s, mileage = %s, min_rental_period = %s, max_rental_period = %s, is_active = %s, updated_at = %s WHERE car_id = %s"
DELETE_CAR = "DELETE FROM Car WHERE car_id = %s"
SELECT_ALL_CARS = "SELECT * FROM Car"
SELECT_CAR_BY_ID = "SELECT * FROM Car WHERE car_id = %s"
SELECT_CARS_BY_BRAND_MODEL_ID = "SELECT * FROM Car WHERE car_brand_model_id = %s"
SELECT_CARS_BY_STATUS_ID = "SELECT * FROM Car WHERE car_status_id = %s"
FIND_CAR_BY_NUMBER_PLATE = "SELECT * FROM Car WHERE number_plate = %s"
SELECT_ALL_CARS_WITH_DETAILS = "SELECT Car.car_Id, Car.number_plate, Car.model_name, Car.daily_rate, Car.year, Car.mileage, Car.min_rental_period, Car.max_rental_period, Car.is_active AS car_is_active, Car.create_at AS car_created_at, Car.updated_at AS car_updated_at, CarBrandModel.brand_name, CarBrandModel.model_name AS brand_model_name, CarType.car_type, CarStatus.car_status_type, Car.car_brand_model_id, Car.car_status_Id FROM Car INNER JOIN CarBrandModel ON Car.car_brand_model_id = CarBrandModel.car_brand_model_id INNER JOIN CarType ON CarBrandModel.car_type_id = CarType.car_type_id INNER JOIN CarStatus ON Car.car_status_Id = CarStatus.car_status_Id WHERE Car.is_active = 1"
SELECT_AVAILABLE_CARS_WITH_DETAILS = "SELECT Car.car_Id, Car.number_plate, Car.model_name, Car.daily_rate, Car.year, Car.mileage, Car.min_rental_period, Car.max_rental_period, Car.is_active AS car_is_active, Car.create_at AS car_created_at, Car.updated_at AS car_updated_at, CarBrandModel.brand_name, CarBrandModel.model_name AS brand_model_name, CarType.car_type, CarStatus.car_status_type, Car.car_brand_model_id, Car.car_status_Id FROM Car INNER JOIN CarBrandModel ON Car.car_brand_model_id = CarBrandModel.car_brand_model_id INNER JOIN CarType ON CarBrandModel.car_type_id = CarType.car_type_id INNER JOIN CarStatus ON Car.car_status_Id = CarStatus.car_status_Id WHERE Car.car_status_Id = 1 AND Car.is_active = 1"
SELECT_UNAVAILABLE_CARS_WITH_DETAILS = "SELECT Car.car_Id, Car.number_plate, Car.model_name, Car.daily_rate, Car.year, Car.mileage, Car.min_rental_period, Car.max_rental_period, Car.is_active AS car_is_active, Car.create_at AS car_created_at, Car.updated_at AS car_updated_at, CarBrandModel.brand_name, CarBrandModel.model_name AS brand_model_name, CarType.car_type, CarStatus.car_status_type, Car.car_brand_model_id, Car.car_status_Id FROM Car INNER JOIN CarBrandModel ON Car.car_brand_model_id = CarBrandModel.car_brand_model_id INNER JOIN CarType ON CarBrandModel.car_type_id = CarType.car_type_id INNER JOIN CarStatus ON Car.car_status_Id = CarStatus.car_status_Id WHERE Car.car_status_Id = 2 AND Car.is_active = 1"

# BookingStatus Table
INSERT_BOOKING_STATUS = "INSERT INTO BookingStatus (booking_status_type, is_active, create_at, updated_at) VALUES (%s, %s, %s, %s)"
UPDATE_BOOKING_STATUS = "UPDATE BookingStatus SET booking_status_type = %s, is_active = %s, updated_at = %s WHERE booking_status_id = %s"
DELETE_BOOKING_STATUS = "DELETE FROM BookingStatus WHERE booking_status_id = %s"
SELECT_ALL_BOOKING_STATUSES = "SELECT * FROM BookingStatus"
SELECT_BOOKING_STATUS_BY_ID = "SELECT * FROM BookingStatus WHERE booking_status_id = %s"

# Booking Table
INSERT_BOOKING = "INSERT INTO Booking (user_id, car_id, booking_status_id, start_date, end_date, total_amount, note, is_active, create_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
UPDATE_BOOKING = "UPDATE Booking SET user_id = %s, car_id = %s, booking_status_id = %s, start_date = %s, end_date = %s, total_amount = %s, note = %s, is_active = %s, updated_at = %s WHERE booking_id = %s"
DELETE_BOOKING = "DELETE FROM Booking WHERE booking_id = %s"
SELECT_ALL_BOOKINGS = "SELECT * FROM Booking"
SELECT_BOOKING_BY_ID = "SELECT * FROM Booking WHERE booking_id = %s"
SELECT_BOOKINGS_BY_USER_ID = "SELECT * FROM Booking WHERE user_id = %s"
SELECT_BOOKINGS_BY_CAR_ID = "SELECT * FROM Booking WHERE car_id = %s"
SELECT_BOOKINGS_BY_STATUS_ID = "SELECT * FROM Booking WHERE booking_status_id = %s"
SELECT_BOOKINGS_AND_DETAILS_BY_USER_ID = "SELECT Booking.booking_id, Booking.start_date, Booking.end_date, Booking.total_amount, Booking.note, Car.number_plate, Car.model_name, Car.daily_rate, Car.year, BookingStatus.booking_status_type, User.user_name, User.user_email FROM Booking INNER JOIN Car ON Booking.car_id = Car.car_id INNER JOIN BookingStatus ON Booking.booking_status_id = BookingStatus.booking_status_id INNER JOIN User ON Booking.user_id = User.user_id WHERE Booking.user_id = %s AND Booking.is_active = 1;"
SELECT_ALL_BOOKINGS_ORDER_BY_ASC = "SELECT Booking.booking_id, Booking.start_date, Booking.end_date, Booking.total_amount, Booking.note, Car.number_plate, Car.model_name, Car.daily_rate, Car.year, BookingStatus.booking_status_type, User.user_name, User.user_email FROM Booking INNER JOIN Car ON Booking.car_id = Car.car_id INNER JOIN BookingStatus ON Booking.booking_status_id = BookingStatus.booking_status_id INNER JOIN User ON Booking.user_id = User.user_id WHERE Booking.is_active = 1 ORDER BY Booking.updated_at ASC;"
SELECT_ALL_PENDING_BOOKINGS_ORDER_BY_ASC = "SELECT Booking.booking_id, Booking.start_date, Booking.end_date, Booking.total_amount, Booking.note, Car.number_plate, Car.model_name, Car.daily_rate, Car.year, BookingStatus.booking_status_type, User.user_name, User.user_email FROM Booking INNER JOIN Car ON Booking.car_id = Car.car_id INNER JOIN BookingStatus ON Booking.booking_status_id = BookingStatus.booking_status_id INNER JOIN User ON Booking.user_id = User.user_id WHERE Booking.is_active = 1 ORDER BY Booking.updated_at ASC;"
SELECT_BOOKING_BY_BOOKING_ID = "SELECT Booking.booking_id, Booking.start_date, Booking.end_date, Booking.total_amount, Booking.note, Car.number_plate, Car.model_name, Car.daily_rate, Car.year, BookingStatus.booking_status_type, User.user_name, User.user_email FROM Booking INNER JOIN Car ON Booking.car_id = Car.car_id INNER JOIN BookingStatus ON Booking.booking_status_id = BookingStatus.booking_status_id INNER JOIN User ON Booking.user_id = User.user_id WHERE Booking.is_active = 1 AND Booking.booking_status_id = 2 AND Booking.booking_id = %s ORDER BY Booking.updated_at ASC;"
SELECT_ADDITIONAL_SERVICES_BY_BOOKING_ID = "SELECT Booking.booking_id, Booking.start_date, Booking.end_date, Booking.total_amount, Booking.note, BookingAdditionalServices.additional_services_id, BookingAdditionalServices.is_active, AdditionalServices.services_description, AdditionalServices.services_amount, AdditionalServices.is_active FROM Booking INNER JOIN BookingAdditionalServices ON Booking.booking_id = BookingAdditionalServices.booking_id INNER JOIN AdditionalServices ON BookingAdditionalServices.additional_services_id = AdditionalServices.additional_services_id WHERE Booking.is_active = 1 AND BookingAdditionalServices.is_active = 1  AND AdditionalServices.is_active = 1 AND Booking.booking_id = %s ORDER BY Booking.updated_at ASC;"


# AdditionalServices Table
INSERT_ADDITIONAL_SERVICE = "INSERT INTO AdditionalServices (services_description, services_amount, is_active, create_at, updated_at) VALUES (%s, %s, %s, %s, %s)"
UPDATE_ADDITIONAL_SERVICE = "UPDATE AdditionalServices SET services_description = %s, services_amount = %s, is_active = %s, updated_at = %s WHERE additional_services_id = %s"
DELETE_ADDITIONAL_SERVICE = "DELETE FROM AdditionalServices WHERE additional_services_id = %s"
SELECT_ALL_ADDITIONAL_SERVICES = "SELECT * FROM AdditionalServices"
SELECT_ADDITIONAL_SERVICE_BY_ID = "SELECT * FROM AdditionalServices WHERE additional_services_id = %s"

# BookingAdditionalServices Table
INSERT_BOOKING_ADDITIONAL_SERVICE = "INSERT INTO BookingAdditionalServices (booking_id, additional_services_id, is_active, create_at, updated_at) VALUES (%s, %s, %s, %s, %s)"
UPDATE_BOOKING_ADDITIONAL_SERVICE = "UPDATE BookingAdditionalServices SET is_active = %s, updated_at = %s WHERE booking_additional_charge_id = %s"
DELETE_BOOKING_ADDITIONAL_SERVICE = "DELETE FROM BookingAdditionalServices WHERE booking_additional_charge_id = %s"
SELECT_ALL_BOOKING_ADDITIONAL_SERVICES = "SELECT * FROM BookingAdditionalServices"
SELECT_BOOKING_ADDITIONAL_SERVICE_BY_ID = "SELECT * FROM BookingAdditionalServices WHERE booking_additional_charge_id = %s"
SELECT_ALL_ADDITIONAL_SERVICES_BY_BOOKING_ID = "SELECT * FROM BookingAdditionalServices WHERE booking_id = %s"

# Invoice Table
INSERT_INVOICE = "INSERT INTO Invoice (booking_id, user_id, amount, payment_method, payment_date, is_paid, is_active, create_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
UPDATE_INVOICE = "UPDATE Invoice SET booking_id = %s, user_id = %s, amount = %s, payment_method = %s, payment_date = %s, is_paid = %s, is_active = %s, updated_at = %s WHERE invoice_id = %s"
DELETE_INVOICE = "DELETE FROM Invoice WHERE invoice_id = %s"
SELECT_ALL_INVOICES = "SELECT * FROM Invoice"
SELECT_ALL_INVOICES_WITH_USERS = "SELECT Invoice.invoice_id, Invoice.booking_id, User.user_name, User.user_email, Invoice.amount, Invoice.payment_method, Invoice.payment_date, Invoice.is_paid FROM Invoice INNER JOIN User ON User.user_id = Invoice.user_id;"
SELECT_INVOICE_BY_ID = "SELECT * FROM Invoice WHERE invoice_id = %s"
SELECT_INVOICES_BY_USER_ID = "SELECT * FROM Invoice WHERE user_id = %s"
SELECT_INVOICES_BY_BOOKING_ID = "SELECT * FROM Invoice WHERE booking_id = %s"
SELECT_ALL_USER_INVOICES = """SELECT Invoice.invoice_id, Invoice.booking_id, Invoice.user_id, Invoice.amount, Invoice.payment_method, Invoice.payment_date, Invoice.is_paid, Invoice.is_active, Booking.start_date, Booking.end_date, Car.number_plate, Car.daily_rate, User.user_name, User.user_email, User.user_phone_number FROM Invoice JOIN Booking ON Invoice.booking_id = Booking.booking_id JOIN Car ON Booking.car_id = Car.car_id JOIN User ON Invoice.user_id = User.user_id WHERE Invoice.is_active = 1;"""
SELECT_ALL_INVOICES_FOR_USER = """SELECT Invoice.invoice_id, Invoice.booking_id, Invoice.user_id, Invoice.amount, Invoice.payment_method, Invoice.payment_date, Invoice.is_paid, Invoice.is_active, Booking.start_date, Booking.end_date, Car.number_plate, Car.daily_rate, User.user_name, User.user_email, User.user_phone_number FROM Invoice JOIN Booking ON Invoice.booking_id = Booking.booking_id JOIN Car ON Booking.car_id = Car.car_id JOIN User ON Invoice.user_id = User.user_id WHERE Invoice.user_id = %s AND Invoice.is_active = 1;"""
SELECT_ALL_INVOICES_FOR_ALL = """SELECT Invoice.invoice_id, Invoice.booking_id, Invoice.user_id, Invoice.amount, Invoice.payment_method, Invoice.payment_date, Invoice.is_paid, Invoice.is_active, Booking.start_date, Booking.end_date, Car.number_plate, Car.daily_rate, User.user_name, User.user_email, User.user_phone_number FROM Invoice JOIN Booking ON Invoice.booking_id = Booking.booking_id JOIN Car ON Booking.car_id = Car.car_id JOIN User ON Invoice.user_id = User.user_id WHERE Invoice.is_active = 1;"""
SELECT_ALL_INVOICES_FOR_PAYMENT = """SELECT Invoice.invoice_id, Invoice.booking_id, Invoice.user_id, Invoice.amount, Invoice.payment_method, Invoice.payment_date, Invoice.is_paid, Invoice.is_active, Booking.start_date, Booking.end_date, Car.number_plate, Car.daily_rate, User.user_name, User.user_email, User.user_phone_number FROM Invoice JOIN Booking ON Invoice.booking_id = Booking.booking_id JOIN Car ON Booking.car_id = Car.car_id JOIN User ON Invoice.user_id = User.user_id WHERE Invoice.is_active = 1 AND Invoice.invoice_id=%s;"""

CREATE_DB = "CREATE DATABASE IF NOT EXISTS"
DEFAULT_OB_NAME = "MSE800_270599091"

