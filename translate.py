#! /usr/bin/env python3

import sys

def translate_sequence(rna_sequence, genetic_code): 
    return genetic_code[rna_sequence]
    """Translates a sequence of RNA into a sequence of amino acids.
    Translates `rna_sequence` into string of amino acids, according to the
    `genetic_code` given as a dict. Translation begins at the first position of
    the `rna_sequence` and continues until the first stop codon is encountered
    or the end of `rna_sequence` is reached.

    If `rna_sequence` is less than 3 bases long, or starts with a stop codon,
    an empty string is returned.
    """
def translate(rna_sequence):
    translation = ''
    for n in range(0, len(rna_sequence) - (len(rna_sequence) % 3), 3):
        translation += translate_sequence(rna_sequence[n:n+3])
    return translation

def translate_in_frame(rna_sequence, framenum):
    return translate(rna_sequence[framenum-1:])

def print_translation_in_frame(rna_sequence, framenum, prefix):
        print(prefix,
              framenum,
              ' ' * framenum,
              translate_in_frame(rna_sequence, framenum),
              sep='')

def print_translations(rna_sequence, prefix=''):
    print('\n' ,' ' * (len(prefix) + 2), rna_sequence, sep='')
    for framenum in range(1,4):
        print_translation_in_frame(rna_sequence, framenum, prefix)

print_translations('ATGCGT')

def translate_with_open_reading_frame(rna_sequence, framenum):
    open = False
    translation = ""
    seqlength = len(rna_sequence) - (framenum - 1)
    for n in range(frame-1, seqlength - (seqlength % 3), 3):
        codon = translate_sequence(rna_sequence[n:n+3])
        open = (open or codon =="M") and not (codon == "---")
        translation += codon if open else "---"
    return translation

def print_translate_with_open_reading_frame(rna_sequence, framenum, prefix):
    print(prefix,
          framenum,
          ' ' * framenum,
          translate_with_open_reading_frame(rna_sequence, framenum),
          sep='')
        
def print_translations_with_open_reading_frames(rna_sequence, prefix=''):
    print('\n', ' ' * (len(prefix) + 2), rna_sequence, sep='')
    for frame in range(1,4):
        print_translate_with_open_reading_frame(rna_sequence, frame, prefix)

def get_all_translations(rna_sequence, genetic_code):
    return (translate_sequence(rna_sequence[n:n+3])
            for n in range(0, len(rna_sequence), 3))  
    """Get a list of all amino acid sequences encoded by an RNA sequence.

    All three reading frames of `rna_sequence` are scanned from 'left' to
    'right', and the generation of a sequence of amino acids is started
    whenever the start codon 'AUG' is found. The `rna_sequence` is assumed to
    be in the correct orientation (i.e., no reverse and/or complement of the
    sequence is explored).

    The function returns a list of all possible amino acid sequences that
    are encoded by `rna_sequence`.

    If no amino acids can be translated from `rna_sequence`, an empty list is
    returned.
    """

def get_reverse(sequence):
    rna_seq[::-1]
    """Reverse orientation of `sequence`.

    Returns a string with `sequence` in the reverse order.

    If `sequence` is empty, an empty string is returned.
    """

def get_complement(sequence):
    if 'A' in rna_seq:
        return('T')
    elif 'T' in rna_seq:
        return('A')
    elif 'G' in rna_seq:
        return('C')
    elif 'C' in rna_seq:
        return('G')
    else:
        exit     
    """Get the complement of `sequence`.

    Returns a string with the complementary sequence of `sequence`.

    If `sequence` is empty, an empty string is returned.
    """

def reverse_and_complement(sequence):
    get_reverse(get_complement(rna_seq))
    """Get the reversed and complemented form of `sequence`.

    Returns a string that is the reversed and complemented sequence
    of `sequence`.

    If `sequence` is empty, an empty string is returned.
    """

def get_longest_peptide(rna_sequence, genetic_code):
    get_all_translations(rna_seq)
    get_all_translations(reverse_and_complement(rna_seq))
    """Get the longest peptide encoded by an RNA sequence.

    Explore six reading frames of `rna_sequence` (three reading frames of the
    current orientation, and the reversed and complemented form) and return (as
    a string) the longest sequence of amino acids that it encodes, according to
    the `genetic_code`.

    If no amino acids can be translated from `rna_sequence` nor its reverse and
    complement, an empty list is returned.
    """


if __name__ == '__main__':
    genetic_code = {'GUC': 'V', 'ACC': 'T', 'GUA': 'V', 'GUG': 'V', 'ACU': 'T', 'AAC': 'N', 'CCU': 'P', 'UGG': 'W', 'AGC': 'S', 'AUC': 'I', 'CAU': 'H', 'AAU': 'N', 'AGU': 'S', 'GUU': 'V', 'CAC': 'H', 'ACG': 'T', 'CCG': 'P', 'CCA': 'P', 'ACA': 'T', 'CCC': 'P', 'UGU': 'C', 'GGU': 'G', 'UCU': 'S', 'GCG': 'A', 'UGC': 'C', 'CAG': 'Q', 'GAU': 'D', 'UAU': 'Y', 'CGG': 'R', 'UCG': 'S', 'AGG': 'R', 'GGG': 'G', 'UCC': 'S', 'UCA': 'S', 'UAA': '*', 'GGA': 'G', 'UAC': 'Y', 'GAC': 'D', 'UAG': '*', 'AUA': 'I', 'GCA': 'A', 'CUU': 'L', 'GGC': 'G', 'AUG': 'M', 'CUG': 'L', 'GAG': 'E', 'CUC': 'L', 'AGA': 'R', 'CUA': 'L', 'GCC': 'A', 'AAA': 'K', 'AAG': 'K', 'CAA': 'Q', 'UUU': 'F', 'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'GCU': 'A', 'GAA': 'E', 'AUU': 'I', 'UUG': 'L', 'UUA': 'L', 'UGA': '*', 'UUC': 'F'}
    rna_seq = ("AUG"
            "UAC"
            "UGG"
            "CAC"
            "GCU"
            "ACU"
            "GCU"
            "CCA"
            "UAU"
            "ACU"
            "CAC"
            "CAG"
            "AAU"
            "AUC"
            "AGU"
            "ACA"
            "GCG")
    longest_peptide = get_longest_peptide(rna_sequence = rna_seq,
            genetic_code = genetic_code)
    assert isinstance(longest_peptide, str), "Oops: the longest peptide is {0}, not a string".format(longest_peptide)
    message = "The longest peptide encoded by\n\t'{0}'\nis\n\t'{1}'\n".format(
            rna_seq,
            longest_peptide)
    sys.stdout.write(message)
    if longest_peptide == "MYWHATAPYTHQNISTA":
        sys.stdout.write("Indeed.\n")
