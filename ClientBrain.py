from random import randint
version_number = "0001" #Current NfP Client version number. Updated 3 January, 2021

class ClientBrain:
    @staticmethod
    def generate_id():
        """Generates a peer-to-peer identification number for BitTorrent tracking in the Azureus style.
        
        Format: -NFXXXX-YYYYYYYYYYYY
            Where: 
                - NF is the NfP identifier.
                - XXXX is the NfP version number. (e.g. 0001)
                - Y is a number, 0-9, randomly generated.

        Returns:
            A string containing the P2P ID number for use with the NfP client."""

        number_suffix = "".join([str(randint(0, 9)) for number in range(12)])   #Generate string of numbers to append to ID
        
        return f"-NF{version_number}-{number_suffix}"   #Returns a string with a randomly generated ID.