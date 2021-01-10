# sample: this represents the
# programming of my remote [1, 0, 0, 1]
# this is a sample building's worth of data:

# { fl1: [
#     [1, 0, 0, 0],
#     [1, 0, 0, 1],
# ],
# fl2: [
#     [1, 1, 0, 0],
#     [1, 0, 0, 0]
# ]
# }


class CodeCalculator(object):
    """given an input of 1.)
     number of fans and 2.) number of floors
     it should return a list of consecutive codes
     mapped to individual fans that will not collide.

     todo: when refactoring, create floor and building 
     as iterable objects. This approach is a little more on
     the functional programming side."""

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

    def remove_floor_level_collisions(self, building_codes):
        """helper method to ensure two codes
        will not collide. Takes dictionary of codes as an array
        and returns updated dictionary"""
        # todo figure out how best to encapsulate
        # this functionality so the caller doesn't need to
        # care about order of codes
        pass

    def calculate_floor(self):
        """Returns an ordered list of
        consecutive fan codes"""

        floor = []

        while len(floor) < self.fans:
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

        return floor

    def calculate_building(self):
        """returns a dictionary of codes. Each
        dict entry corresponds with a floor"""

        building_codes = dict((f"fl{key}", self.calculate_floor())
                              for key in range(1, self.floors + 1))

        self.remove_floor_level_collisions(building_codes=building_codes)
        return building_codes
