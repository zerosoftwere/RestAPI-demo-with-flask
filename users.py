from abc import ABCMeta, abstractmethod

class UserDOA(metaclass=ABCMeta):
    """Interface for User Objects to connect to data sources"""
    @abstractmethod
    def find_all(self):
        """Returns a list of all users from the database"""
        pass

    @abstractmethod
    def find_one(self, user_id):
        """Finds a user with the given ID from the database"""
        pass

    @abstractmethod
    def create(self, username, password):
        """Creates and store a new user to the database"""
        pass

    @abstractmethod
    def update(self, user_id, username, password):
        """Updates user properties"""
        pass

    @abstractmethod
    def remove(self, user_id):
        """Delete the user with given id if found from the database"""
        pass


class MockUserDAO(UserDOA):
    """Performs mock crud operation for User class"""
    count = 0
    users = [
        {'id': count, 'username': 'xero', 'password': 'verysecure'}
    ]

    def find_all(self):
        return MockUserDAO.users

    def find_one(self, user_id):
        user = [user for user in MockUserDAO.users if user['id'] == user_id]
        if user:
            return user[0]
        return None

    def update(self, user_id, username, password):
        user = self.find_one(user_id)
        if user:
            user['password'] = password
            return True
        return False

    def create(self, username, password):
        MockUserDAO.count += 1
        user = {'id': MockUserDAO.count, 'username': username, 'password': password}
        MockUserDAO.users.append(user)

    def remove(self, user_id):
        if not self.find_one(user_id):
            return False
        MockUserDAO.users = list(filter(lambda user: user['id'] != user_id, MockUserDAO.users))
        return True
