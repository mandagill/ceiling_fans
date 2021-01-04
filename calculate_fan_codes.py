# sample: this represents the
# programming of my remote [1, 0, 0, 1]
# this is a sample building's worth of data:

# { fl1: [
#     [1, 0, 0, 0],
#     [1, 0, 0, 1],
# ],
# fl2: [
# [1, 1, 0, 0],
# [1, 0, 0, 0]
# ]
# }


class CodeCalculator(object):
    """given an input of 1.)
     number of fans and 2.) number of floors
     it should return a list of consecutive codes
     mapped to individual fans that will not collide."""

    SEED = [0, 0, 0, 0]

    def __init__(self, fans, floors):
        self.fans = fans
        self.floors = floors

    def switch_bit(self, bit):
        """helper method to make it easier to 
        change the value for any given fan 
        code in an array"""
        if bit == 0:
            return 1
        else:
            return 0

    def calculate_floor(self):
        """Returns an ordered list of
        consecutive fan codes"""

        floor = []

        # using len() to help protect against out of index errors
        while len(floor) != self.fans:
            print(f"this is the value of self.fans: {self.fans}")
            try:
                floor[-1]
            except IndexError:
                floor.append(self.SEED)

            # pull out the most recently added code array
            last_code = floor[-1]
            next_code = last_code.copy()
            # algorithm is pretty rudimentary now,
            # it only checks the last bit in the fan code
            next_code[-1] = self.switch_bit(last_code[-1])
            floor.append(next_code)

    # add some kind of increment counter
        return floor

    def calculate_building(self):
        """returns a dictionary of codes. Each
        dict entry corresponds with a floor"""
        # todo add validation that the fan above
        # and below won't collide
        pass
