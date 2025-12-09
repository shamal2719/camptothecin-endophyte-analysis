-- Database schema for Camptothecin-related protein analysis

CREATE TABLE Proteins (
    ProteinID INTEGER PRIMARY KEY,
    Name TEXT,
    Organism TEXT,
    Function TEXT
);

CREATE TABLE Structures (
    StructureID INTEGER PRIMARY KEY,
    ProteinID INTEGER,
    PDB_ID TEXT,
    AtomCount INTEGER,
    ResidueCount INTEGER,
    FOREIGN KEY (ProteinID) REFERENCES Proteins(ProteinID)
);

-- Example query: Find proteins involved in CPT biosynthesis
SELECT Name, Organism
FROM Proteins
WHERE Function LIKE '%camptothecin%';
