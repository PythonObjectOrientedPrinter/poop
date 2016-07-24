class Gcode:
    def __init__(self, filepath):
        self.curr_line = 0
        self.filepath = filepath
        self.lines_of_gcodes = 0
        self.done_lines = 0
        with open(filepath) as f:
            for line in f:
                self.lines_of_gcodes += 1

    def next_line(self):
        pass

    def has_work(self):
        if self.done_lines >= self.lines_of_gcodes:
            return False

        self.done_lines += 1
        return True
