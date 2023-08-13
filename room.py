class Room():
    """
    name: Name of the room
    people: People in the room
    connection: Rooms connected to the room, aka traversable areas by the player
    """
    def __init__(self, name, people = [], connection = []):
        self.name = name
        self.people = people
        self.connection = connection
