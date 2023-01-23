from dataclasses import dataclass
from heapq import heapify, heappop, heappush
from bitarray import frozenbitarray

@dataclass(order=True, frozen=True)
class HuffmanNode():
  prob: float
  values: str
  left: object = None
  right: object = None
  
  def merge(self, other):
      return HuffmanNode(self.prob + other.prob, self.values + other.values, self, other)
    
class HuffmanTree():
  """Builds a Huffman Tree from a dictionary of chars to their counts in the original data.

      Args:
          char_counts (dict): char : count dict
  """
  def __init__(self, char_counts):
    self.msg_len = sum(count for count in char_counts.values())
    self.char_counts = char_counts
    self.probability_map = self._generate_probabilities()
    self.root = self._build_huffman_tree()
    
  def _generate_probabilities(self):
      return {x : count / self.msg_len for x, count in self.char_counts.items()}
  
  def _build_huffman_tree(self):
      self._generate_probabilities()
      heap = [HuffmanNode(prob, val) for val, prob in self.probability_map.items()]
      heapify(heap)
      
      while len(heap) > 1:
          min1 = heappop(heap)
          min2 = heappop(heap)
          merged = min1.merge(min2)
          heappush(heap, merged)
      
      return heappop(heap)
  
  def create_char_map(self) -> dict[str:object]:
    """Creates and returns a dictionary mapping characters to their bit encoding.
    """
    char_map = {}
    def traverse(node, bits):
        if node.left is None and node.right is None:
            # leaf node
            char_map[node.values] = bits
            return
        if node.left is not None:
            traverse(node.left, bits + frozenbitarray('0'))
        if node.right is not None:
            traverse(node.right, bits + frozenbitarray('1'))
    traverse(self.root, frozenbitarray(''))
    return char_map
            
  def create_reverse_char_map(self):
    """Creates and returns a dictionary mapping bit encodings to characters
    """
    reverse_char_map = {}
    def traverse(node, bits):
        if node.left is None and node.right is None:
            # leaf node
            reverse_char_map[bits] = node.values
            return
        if node.left is not None:
            traverse(node.left, bits + frozenbitarray('0'))
        if node.right is not None:
            traverse(node.right, bits + frozenbitarray('1'))
    
    traverse(self.root, frozenbitarray(''))
    return reverse_char_map