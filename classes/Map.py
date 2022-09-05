class Room:
    number: int
    previous_room: int
    # todo: next_room has to be checked somehow
    treasure: bool
    has_enemy: bool
    boss: bool

    def __init__(self, previous_room: int):
        self.previous_room = previous_room
        self.number = previous_room + 1

    def display_info(self) -> str:
        """Returns a string to display the current and previous corresponding room numbers."""
        return f"Current room: No{self.number}. Previous room: No{self.previous_room}."


class Map:

    """

    How to represent the map ?

        Option 1: In 2D, top-down view
            Room1 -> Room2 -> Fork(Room3 -> Room4, Room5)

            Room1 -> Room2 -> Room3 -> Room5
                                |
                              Room4

            class Room:
                # see above

        Option 2: layouts
            rooms(5) -> A, B, C, D, E

        Option 3: procedurally generated
            def spawn_next_room(vars):
                self.dict["next_room"] = next_room()

    """

    data: dict
    rooms: dict

    def __init__(self):
        self.data = {}
        self.rooms = {}

    def add_next_room(self) -> None:
        """Add a new room to the Map. The new room index increases incrementally from the last one found."""

        if not list(self.rooms.keys()):
            next_room_key = "room" + str(0)
            self.rooms[next_room_key] = Room(0)
        else:
            next_room_key = "room" + str(len(list(self.rooms.keys())))
            number_of_existing_rooms = len(list(self.rooms.keys()))
            self.rooms[next_room_key] = Room(number_of_existing_rooms)

        # print(next_room.display_info())
