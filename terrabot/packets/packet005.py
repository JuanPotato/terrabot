from . import packet


class Packet5(packet.Packet):
    def __init__(self, player, slot):
        super().__init__(5)
        self.add_data(player.playerID)
        self.add_data(slot)
        self.add_structured_data("<h", 0)  # Stack
        self.add_data(0)  # Prefix
        self.add_structured_data("<h", 0)  # ItemID
