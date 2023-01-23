from .parsing import decode_4_byte_utf8
from .huffman_tree import HuffmanTree
from bitarray import frozenbitarray, bitarray

class HuffmanDecoder():
  def __init__(self, compressed: bytes):
    self.compressed = compressed
    self.num_chars, self.char_counts, self.compressed_msg_len, self.header_length = self._process_header(compressed)
    self.huffman_tree = HuffmanTree(self.char_counts)
    self.reverse_char_map = self.huffman_tree.create_reverse_char_map()
    
  def _process_header(self, compressed: bytes) -> tuple[int, dict[str:int], int, int]:
    """
    Unpacks the header of compressed text.
    """
    num_chars = int.from_bytes(compressed[0:4], byteorder='big', signed=False)

    char_counts = {}
    start_of_char_counts = 4 
    end_of_char_counts = 4 + num_chars * 8
    for i in range(start_of_char_counts, end_of_char_counts, 8):
      #print(compressed[i:i + 4])
      char = decode_4_byte_utf8(compressed[i:i + 4])
      count = int.from_bytes(compressed[i + 4: i + 8], byteorder='big', signed=False)
      char_counts[char] = count
    
    compressed_unpadded_size = int.from_bytes(compressed[end_of_char_counts: end_of_char_counts + 8], byteorder='big', signed=False)
    header_length = end_of_char_counts + 8
    return num_chars, char_counts, compressed_unpadded_size, header_length
        
  def decode(self) -> str:
    bits = bitarray()
    bits.frombytes(self.compressed[self.header_length:])

    original = ''
    curr = frozenbitarray('')
    for i in range(self.compressed_msg_len):
      curr = curr + bits[i:i+1]
      if curr in self.reverse_char_map:
        original += self.reverse_char_map[curr]
        curr = frozenbitarray('')
    return original
    