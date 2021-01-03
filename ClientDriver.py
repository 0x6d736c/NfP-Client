from random import randint
import bencode

version_number = "0001" #Current NfP Client version number. Updated 3 January, 2021

class ClientDriver:
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

    @staticmethod
    def decode_torrent(file_path):
        """Extracts the torrent information from a .torrent file.
        
        Returns:
            An ordered dictionary of decoded bencoding of the inputted .torrent file."""

        #Open specified file in binary read mode. Read-in data from file. Decode it using bencode library.
        with open(file_path, "rb") as torrent_file:
            torrent_data = torrent_file.read()
            decoded_data = bencode.decode(torrent_data)

        return decoded_data


x = ClientDriver.decode_torrent("ubuntu-20.10-desktop-amd64.iso.torrent")
print(x["announce"])