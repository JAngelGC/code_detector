import hashlib

def compute_hash(kgram):
    """
    Compute a simple hash for a k-gram using SHA-1.
    """
    return int(hashlib.sha1(kgram.encode()).hexdigest(), 16)

def winnowing(text, k=5, w=4):
    """
    Perform the winnowing algorithm on the given text.
    
    Args:
        text (str): The input text.
        k (int): The length of k-grams.
        w (int): The size of the sliding window.
    
    Returns:
        list of tuples: A list of (fingerprint, position) tuples.
    """
    n = len(text)
    kgrams = [text[i:i+k] for i in range(n - k + 1)]
    hashes = [compute_hash(kgram) for kgram in kgrams]

    fingerprints = []
    min_hash_pos = -1

    for i in range(len(hashes) - w + 1):
        window = hashes[i:i + w]
        min_hash = min(window)
        min_pos = window.index(min_hash) + i
        
        if min_pos != min_hash_pos:
            fingerprints.append((min_hash, min_pos))
            min_hash_pos = min_pos

    return fingerprints

# Example usage
text = "The quick brown fox jumps over the lazy dog"
fingerprints = winnowing(text, k=5, w=4)
print("Fingerprints:", fingerprints)
