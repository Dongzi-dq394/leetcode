class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.record = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message not in self.record:
            self.record[message] = timestamp
            return True
        else:
            if timestamp-self.record[message]>=10:
                self.record[message] = timestamp
                return True
            return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)