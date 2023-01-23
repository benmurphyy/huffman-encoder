# Huffman Encoder and Decoder  
Simple huffman encoder and decoder for files encoded in 'utf-8' (most text files).  
I built this after watching an interesting video on Huffman encoding [here](https://www.youtube.com/watch?v=B3y0RsVCyrw) which I found really cool and interesting, so I wanted to write my own version of a simple Huffman encoder and decoder.

## Usage:  
### Encode a file:
`python huffman.py -e <inputfile> [outputfile]`
outputfile name is optional, default will be inputfile name followed by ".huff"  
### Decode a file:
`python huffman.py -d <inputfile> [outputfile]`
outputfile name is optional, default will be inputfile name followed by ".txt"