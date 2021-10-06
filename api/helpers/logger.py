# For test purpose only
class DataLogger:
    def __init__(self, path):
        self.path = path

    def log(self, data):
        if type(data) is not list:
            data = [data]
        f = open(self.path, 'a')
        out = '\n'.join(list(map(lambda x: str(x), data)))
        f.write(f'--------------------------------------------\n{out}\n')
        f.close()
