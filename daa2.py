import heapq

class node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


# Step 1: Build frequency dictionary
def build_frequency_dict(text):
    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1
    return freq


# Step 2: Build Huffman Tree
def build_huffman_tree(freq_dict):
    heap = [node(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]  # root node


# Step 3: Generate Huffman Codes
def generate_codes(root, current_code="", codes={}):
    if root is None:
        return

    if root.char is not None:
        codes[root.char] = current_code

    generate_codes(root.left, current_code + "0", codes)
    generate_codes(root.right, current_code + "1", codes)

    return codes

# Step 4: Encode the text
def huffman_encoding(text):
    return ''.join(codes[ch] for ch in text)

# Step 5: Decode the text
def huffman_decoding(encoded_text, root):
    decoded_text = ""
    current_node = root

    for bit in encoded_text:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decoded_text += current_node.char
            current_node = root

    return decoded_text


text = input("Enter the text to be encoded: ")
freq = build_frequency_dict(text)
huffman_tree_root = build_huffman_tree(freq)
codes = generate_codes(huffman_tree_root)
encoded_text = huffman_encoding(text)   

print("Huffman Codes:", codes)
print("Encoded text:", encoded_text)
decoded_text = huffman_decoding(encoded_text, huffman_tree_root)