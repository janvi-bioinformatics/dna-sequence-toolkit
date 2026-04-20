"""
DNA Sequence Analysis Toolkit
Author: Janvi

Features:
- Base counting
- GC content
- DNA → RNA
- Reverse complement
- ATG position finder
- DNA → Protein
- Mutation finder
"""

# ---------------- FUNCTIONS ---------------- #

def is_valid(seq):
    for base in seq:
        if base not in "ATGC":
            return False
    return True


def dna_count(seq):
    count = {}
    for base in seq:
        if base in count:
            count[base] += 1
        else:
            count[base] = 1
    return count


def gc_content(seq):
    gc = seq.count("G") + seq.count("C")
    return (gc / len(seq)) * 100


def dna_to_rna(seq):
    return seq.replace("T", "U")


def reverse_complement(seq):
    comp = {"A": "T", "T": "A", "G": "C", "C": "G"}
    return "".join(comp[base] for base in reversed(seq))


def atg_positions(seq):
    positions = []
    for i in range(len(seq) - 2):
        if seq[i:i+3] == "ATG":
            positions.append(i)
    return positions


def dna_to_protein(seq):
    codon_table = {
        "ATA":"I","ATC":"I","ATT":"I","ATG":"M",
        "ACA":"T","ACC":"T","ACG":"T","ACT":"T",
        "AAC":"N","AAT":"N","AAA":"K","AAG":"K",
        "AGC":"S","AGT":"S","AGA":"R","AGG":"R",
        "CTA":"L","CTC":"L","CTG":"L","CTT":"L",
        "CCA":"P","CCC":"P","CCG":"P","CCT":"P",
        "CAC":"H","CAT":"H","CAA":"Q","CAG":"Q",
        "CGA":"R","CGC":"R","CGG":"R","CGT":"R",
        "GTA":"V","GTC":"V","GTG":"V","GTT":"V",
        "GCA":"A","GCC":"A","GCG":"A","GCT":"A",
        "GAC":"D","GAT":"D","GAA":"E","GAG":"E",
        "GGA":"G","GGC":"G","GGG":"G","GGT":"G",
        "TCA":"S","TCC":"S","TCG":"S","TCT":"S",
        "TTC":"F","TTT":"F","TTA":"L","TTG":"L",
        "TAC":"Y","TAT":"Y","TAA":"_","TAG":"_",
        "TGC":"C","TGT":"C","TGA":"_","TGG":"W"
    }

    protein = ""
    for i in range(0, len(seq) - 2, 3):
        codon = seq[i:i+3]
        protein += codon_table.get(codon, "?")
    return protein


def mutation_finder(seq1, seq2):
    mutations = []
    for i in range(min(len(seq1), len(seq2))):
        if seq1[i] != seq2[i]:
            mutations.append((i, seq1[i], seq2[i]))
    return mutations


# ---------------- MENU ---------------- #

def menu():
    print("\nDNA Toolkit")
    print("1. Base Count")
    print("2. GC Content")
    print("3. DNA to RNA")
    print("4. Reverse Complement")
    print("5. ATG Position Finder")
    print("6. DNA to Protein")
    print("7. Mutation Finder")
    print("8. Exit")


# ---------------- MAIN PROGRAM ---------------- #

while True:
    menu()
    choice = input("Choose option: ")

    if choice == "1":
        seq = input("Enter DNA sequence: ").upper()
        if is_valid(seq):
            print("Base Count:", dna_count(seq))
        else:
            print("Invalid DNA sequence!")

    elif choice == "2":
        seq = input("Enter DNA sequence: ").upper()
        if is_valid(seq):
            print("GC Content:", gc_content(seq))
        else:
            print("Invalid DNA sequence!")

    elif choice == "3":
        seq = input("Enter DNA sequence: ").upper()
        if is_valid(seq):
            print("RNA:", dna_to_rna(seq))
        else:
            print("Invalid DNA sequence!")

    elif choice == "4":
        seq = input("Enter DNA sequence: ").upper()
        if is_valid(seq):
            print("Reverse Complement:", reverse_complement(seq))
        else:
            print("Invalid DNA sequence!")

    elif choice == "5":
        seq = input("Enter DNA sequence: ").upper()
        if is_valid(seq):
            print("ATG Positions:", atg_positions(seq))
        else:
            print("Invalid DNA sequence!")

    elif choice == "6":
        seq = input("Enter DNA sequence: ").upper()
        if is_valid(seq):
            print("Protein:", dna_to_protein(seq))
        else:
            print("Invalid DNA sequence!")

    elif choice == "7":
        seq1 = input("Enter first DNA sequence: ").upper()
        seq2 = input("Enter second DNA sequence: ").upper()

        if is_valid(seq1) and is_valid(seq2):
            print("Mutations:", mutation_finder(seq1, seq2))
        else:
            print("Invalid DNA sequence!")

    elif choice == "8":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
