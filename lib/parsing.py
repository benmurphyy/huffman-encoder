class MultipleCharacterException(Exception):
  """
  Raised when trying to encode more than 1 character.
  """
  pass
    
class InvalidByteStringException(Exception):
  """
  Raised when attempting to decode a byte string of length that is not 4 bytes.
  """
  pass
    
def encode_to_4_byte_utf8(s: str) -> bytes:
  """Encodes a character to utf-8 left adjusted to 4 bytes.
  """
  if len(s) > 1:
      raise MultipleCharacterException
  return s.encode('utf-8').ljust(4, b'\x00')

def decode_4_byte_utf8(s: bytes) -> str:
  """Decodes a 4 byte utf-8 char to its represented character
  """
  if len(s) != 4:
      raise InvalidByteStringException
  try:
    return s.rstrip(b'\x00').decode('utf-8')
  except UnicodeDecodeError:
    print(s)
    print(s.rstrip(b'\x00'))
    raise UnicodeDecodeError

def _test_encoder():
  assert 'A' == decode_4_byte_utf8(encode_to_4_byte_utf8('A'))
  
if __name__ == '__main__':
  try: 
    _test_encoder()
    print("All tests complete")
  except AssertionError:
    print("There is a problem with encoding and decoding")
  
