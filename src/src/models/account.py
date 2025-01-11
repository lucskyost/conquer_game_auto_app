
class Account:
    def __init__(self, username="", password="", group="", server="", level="", gold="", status=False):
        self._username = username
        self._password = password
        self._group = group
        self._server = server
        self._level = level
        self._gold = gold
        self._status = status
        self._is_run = False
        self._auto_file_1 = ""
        self._auto_file_2 = ""

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def group(self):
        return self._group

    @group.setter
    def group(self, value):
        self._group = value

    @property
    def server(self):
        return self._server

    @server.setter
    def server(self, value):
        self._server = value

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value

    @property
    def gold(self):
        return self._gold

    @gold.setter
    def gold(self, value):
        self._gold = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def is_run(self):
        return self._is_run

    @is_run.setter
    def is_run(self, value):
        self._is_run = value

    @property
    def auto_file_1(self):
        return self._auto_file_1

    @auto_file_1.setter
    def auto_file_1(self, value):
        self._auto_file_1 = value
        
    @property
    def auto_file_2(self):
        return self._auto_file_2

    @auto_file_2.setter
    def auto_file_2(self, value):
        self._auto_file_2 = value

    def __str__(self):
        return f"Username: {self._username}, Password: {self._password}, Group: {self._group}, Server: {self._server}, Level: {self._level}, Gold: {self._gold}, Status: {self._status}, Is Run: {self._is_run}, Auto File 1: {self._auto_file_1}, Auto File 2: {self._auto_file_2}"
