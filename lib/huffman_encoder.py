from collections import Counter
from bitarray import bitarray

from .huffman_tree import HuffmanTree
from .parsing import encode_to_4_byte_utf8

class HuffmanEncoder():
  """Creates an encoder uses huffman encoding to compress a string.
  """
  def __init__(self, original: str):
      self.original = original
      self.char_counts = dict(Counter(self.original))
      self.huffman_tree = HuffmanTree(self.char_counts)
      self.char_map = self.huffman_tree.create_char_map()
      
  def _create_header(self, num_of_compressed_bits) -> bytes:
      """Creates the header information for the compressed file.
      """
      # number of unique chars in original file
      header = len(self.char_map).to_bytes(4, 'big', signed=False)
      # each character followed by their counts
      for char, count in self.char_counts.items():
          header += encode_to_4_byte_utf8(char)
          header += count.to_bytes(4, 'big', signed=False)
      # compressed size of file in bits
      header += num_of_compressed_bits.to_bytes(8, 'big', signed=False)
      return header
      
  def encode(self) -> bytes:
      """Encodes the original text. 
      Returns a byte string.
      """
      compressed = bitarray()
      for char in self.original:
          compressed += self.char_map[char]
      return self._create_header(len(compressed)) + compressed.tobytes()
  
