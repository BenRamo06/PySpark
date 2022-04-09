

class errorsClass:

    def __init__(self, error):
        self.error = error

    def error(self):
        """Log an error.:param: Error message to write to log
        :return: None
        """
        print(self.error)
        return None