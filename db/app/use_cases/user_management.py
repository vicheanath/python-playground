import logging

class UserManagement:
    def __init__(self, database):
        self.database = database
        self.logger = logging.getLogger(__name__)

    def create_user(self, user_data):
        # Business logic for creating a user
        self.logger.info("Creating user: %s", user_data)
        return self.database.create_user(user_data)

    def get_user(self, user_id):
        # Business logic for retrieving a user
        self.logger.info("Retrieving user with ID: %s", user_id)
        return self.database.get_user(user_id)

    def update_user(self, user_id, updated_data):
        # Business logic for updating a user
        self.logger.info("Updating user with ID %s: %s", user_id, updated_data)
        return self.database.update_user(user_id, updated_data)

    def delete_user(self, user_id):
        # Business logic for deleting a user
        self.logger.info("Deleting user with ID: %s", user_id)
        return self.database.delete_user(user_id)
