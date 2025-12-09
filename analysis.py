import os
from pdb_parser import parse_pdb

DATA_DIR = "data"

def analyze_structure(pdb_path):
    pdb_data = parse_pdb(pdb_path)
    num_atoms = len(pdb_data['atoms'])
    num_residues = len(set([a['residue_number'] for a in pdb_data['atoms']]))
    print(f"File: {pdb_path}")
    print(f"Total atoms: {num_atoms}")
    print(f"Total residues: {num_residues}")

def main():
    for file in os.listdir(DATA_DIR):
        if file.endswith(".pdb"):
            analyze_structure(os.path.join(DATA_DIR, file))

if __name__ == "__main__":
    main()
