import hashlib
import os

def get_source_signature(file_path):
    if not os.path.exists(file_path):
        return 0
    with open(file_path, 'rb') as f:
        content = f.read()
    # 10-bit integer from content hash
    return int(hashlib.md5(content).hexdigest(), 16) % 1024

def archive_and_encode():
    sources = [
        "archived_sources/monster_dims_partial.txt",
        "archived_sources/BIBLIOGRAPHY.md",
        "archived_sources/fractran_snippet.py",
        "archived_sources/lean_modular_form.lean"
    ]
    
    signatures = {}
    for src in sources:
        sig = get_source_signature(src)
        signatures[os.path.basename(src)] = sig
        
    print("### Source Ingestion: Holomorphic Signatures")
    print("| Source | Signature (10-bit Hash) |")
    print("| :--- | :--- |")
    for name, sig in signatures.items():
        print(f"| {name} | {sig} |")
        
    # Generate Python code to be injected into master_tree_encoding.py
    print("\n# Add this to master_tree_encoding.py:")
    print(f"ARCHIVE_SIGNATURES = {signatures}")

if __name__ == "__main__":
    archive_and_encode()
