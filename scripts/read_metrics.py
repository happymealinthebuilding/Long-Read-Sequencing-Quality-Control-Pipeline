import gzip
import pandas as pd
from Bio import SeqIO
import sys

input_fastq = sys.argv[1]
output_file = sys.argv[2]

records = []

with gzip.open(input_fastq, "rt") as handle:
    for record in SeqIO.parse(handle, "fastq"):

        seq = record.seq
        qualities = record.letter_annotations["phred_quality"]

        length = len(seq)

        gc = (seq.count("G") + seq.count("C")) / length * 100

        mean_q = sum(qualities) / len(qualities)

        records.append({
            "read_id": record.id,
            "read_length": length,
            "gc_content": gc,
            "mean_quality": mean_q
        })

df = pd.DataFrame(records)

df.to_csv(output_file, index=False)

print("Processed reads:", len(df))