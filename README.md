# Camptothecin Endophyte Protein Structure Analysis  
This repository includes Python and SQL scripts for analyzing proteins involved in the camptothecin (CPT) biosynthetic pathway in endophytic fungi.

## Contents
- `analysis.py` – workflow for loading PDB files, computing simple structural stats.
- `pdb_parser.py` – minimal custom PDB parser (no external libraries needed).
- `database.sql` – schema + example queries for storing protein & structural data.

## How to Use
1. Place your PDB files in the `data/` directory.
2. Run `analysis.py` to extract residue counts and atom-level stats.
3. Use SQL queries to store results in your database.
