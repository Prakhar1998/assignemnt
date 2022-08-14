class DataStream:

    def __init__(self):
        self.datadict: dict = {}

    def should_output_data_str(self, time_stamp: int, data_string: str) -> bool:
        if data_string in self.datadict.keys():
            if time_stamp - self.datadict[data_string] > 5:
                self.datadict[data_string] = time_stamp
                return True
            else:
                return False
        else:
            self.datadict[data_string] = time_stamp
            return True


data_stream = DataStream()
print(data_stream.should_output_data_str(0, "hello"))
print(data_stream.should_output_data_str(0, 'world'))
print(data_stream.should_output_data_str(6, "hello"))
print(data_stream.should_output_data_str(7, "hello"))
print(data_stream.should_output_data_str(8, "world"))
