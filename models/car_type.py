import time

from database.sql_statement import *


class CarType:
    def __init__(self, car_type, is_active=1, car_type_id=None):
        self.car_type = car_type
        self.is_active = is_active
        self.car_type_id = car_type_id # Will be set after insertion in the database

    @staticmethod
    def insert(db, car_type):
        sql = INSERT_CAR_TYPE
        values = (car_type.car_type, car_type.is_active, int(time.time()), int(time.time()))
        added_id = db.add_to_database(sql, values)
        car_type.car_type_id = added_id
        return car_type

    @staticmethod
    def update(db, car_type):
        sql = UPDATE_CAR_TYPE
        values = (car_type.car_type, car_type.is_active, int(time.time()), car_type.car_type_id)
        db.update_database(sql, values)
        print(f"CarType with ID {car_type.car_type_id} updated.")

    @staticmethod
    def deactivate(db, car_type):
        sql = UPDATE_CAR_TYPE
        is_active = 0
        values = (car_type.car_type, is_active, int(time.time()), car_type.car_type_id)
        db.update_database(sql, values)
        print(f"CarType with ID {car_type.car_type_id} deactivated.")

    @staticmethod
    def delete(db, car_type):
        sql = DELETE_CAR_TYPE
        values = (car_type.car_type_id,)
        db.delete_from_database(sql, values)
        print(f"CarType with ID {car_type.car_type_id} deleted.")

    @staticmethod
    def select(db, car_type=None):
        sql = SELECT_ALL_CAR_TYPES if car_type is None else SELECT_CAR_TYPE_BY_ID
        values = (car_type.car_type_id,) if car_type else None
        rows = db.select_from_database(sql, values)

        # Create a list to hold CarType objects
        car_types = []
        for row in rows:
            # Assuming `row` is a tuple in the format: (car_type_id, car_type, is_active, ...)
            car_type_obj = CarType(
                car_type=row[1],  # Assuming `car_type` is the second column
                is_active=row[2],  # Assuming `is_active` is the third column
                car_type_id=row[0]  # Assuming `car_type_id` is the first column
            )
            car_types.append(car_type_obj)

        return car_types

