import sys

from lib.huffman_decoder import HuffmanDecoder
from lib.huffman_encoder import HuffmanEncoder

def calculate_compression_ratio(original, compressed):
  return len(compressed) / len(original) * 100

def get_filename_wo_ext(filename):
  ext_start = filename.find('.')
  return sys.argv[2][:ext_start] if ext_start != -1 else sys.argv[2]

if __name__ == '__main__':
  if len(sys.argv) < 3:
    print("Usage: huffman.py [OPTIONS] <inputfile> <outputfile>\nuse -d to decode, -e to encode")
    sys.exit()
    
  if sys.argv[1] == '-e':
    """Handle compression"""
    default_output_file = get_filename_wo_ext(sys.argv[2]) + ".huff"
    if len(sys.argv) < 4:
      print(f'No output file specified, output will be to "{default_output_file}"')
      
    inputfile_path = sys.argv[2]
    try:
      outputfile_path = sys.argv[3]
    except IndexError:
      outputfile_path = default_output_file
    
    try:
      with open(inputfile_path, 'r', encoding='utf-8') as inputfile:
        # TODO: implement incremental reading from disk (not all at once into memory)
        original_text = inputfile.read()
        huffman_encoder = HuffmanEncoder(original_text)
        
        compressed_bytes = huffman_encoder.encode()
        print(f"Compression Finished.\nCompression Ratio: {calculate_compression_ratio(original_text, compressed_bytes)}")
    except FileNotFoundError:
      print("The input file specified does not exist")
      sys.exit()
      
    with open(outputfile_path, 'wb') as outputfile:
      outputfile.write(compressed_bytes)
    
    print(f"Compressed file contents written to {outputfile_path}")
    
    
  elif sys.argv[1] == '-d':
    """Handle decompression"""
    default_output_file = get_filename_wo_ext(sys.argv[2]) + ".txt"
    if len(sys.argv) < 4:
      print(f'No output file specified, default output is "{default_output_file}"')
      
    inputfile_path = sys.argv[2]
    try:
      outputfile_path = sys.argv[3]
    except IndexError:
      outputfile_path = default_output_file
    
    try:
      with open(inputfile_path, 'rb') as inputfile:
        # TODO: implement incremental reading from disk (not all at once into memory)
        compressed_text = inputfile.read()
        huffman_decoder = HuffmanDecoder(compressed_text)
        
        original_text = huffman_decoder.decode()
      print("File successfully decompressed.")
    except FileNotFoundError:
      print("The input file specified does not exist")
      sys.exit()
      
    with open(outputfile_path, 'w', encoding='utf-8') as outputfile:
      outputfile.write(original_text)
    
    print(f"Original file contents written to {outputfile_path}")
    
  
  
      
    
    