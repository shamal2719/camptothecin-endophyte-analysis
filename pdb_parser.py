def parse_pdb(path):
    atoms = []
    with open(path) as f:
        for line in f:
            if line.startswith("ATOM") or line.startswith("HETATM"):
                atoms.append({
                    'atom_name': line[12:16].strip(),
                    'residue_name': line[17:20].strip(),
                    'chain': line[21].strip(),
                    'residue_number': int(line[22:26]),
                    'x': float(line[30:38]),
                    'y': float(line[38:46]),
                    'z': float(line[46:54])
                })
    return {'atoms': atoms}
