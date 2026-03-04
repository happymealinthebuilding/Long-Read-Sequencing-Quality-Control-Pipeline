# Long-Read Sequencing Quality Control Pipeline

![Snakemake](https://img.shields.io/badge/workflow-snakemake-blue)
![Python](https://img.shields.io/badge/python-3.10-green)
![License](https://img.shields.io/badge/license-MIT-orange)

## Overview

This repository contains a **reproducible bioinformatics pipeline** designed to perform **quality control (QC) and exploratory analysis of long-read sequencing data**.

The project was developed as part of a **bioinformatics internship assessment**, where the goal was to analyze raw sequencing reads and provide a clear, interpretable summary of the dataset before proceeding with downstream analysis such as genome alignment.

The pipeline processes a **FASTQ file containing long-read sequencing data**, calculates important statistics for each read, generates visualizations of key metrics, and produces a concise report describing the quality of the dataset.

The workflow is implemented using **Snakemake**, ensuring the analysis is **automated, reproducible, and modular**.

---

# Dataset

The dataset analyzed in this project comes from a publicly available Oxford Nanopore sequencing dataset hosted on Figshare.

Dataset source:  
https://figshare.com/articles/dataset/ONT_FASTQ_files/7554293?file=14039333

File used:
VREC1013.fastq.gz

Format:
FASTQ (compressed .gz)

File size:
~1.72 GB

MD5 checksum:
57c1e337d2d7e332edc11eea028cdfe7

_Due to GitHub file size limitations, the raw FASTQ file is **not included in this repository**._

---

# Project Goals

The main objectives of this project were:

- Build a **reproducible workflow** using Snakemake
- Perform **quality control of long-read sequencing data**
- Calculate per-read statistics including:
  - GC content
  - Read length
  - Mean read quality score
- Generate **visualizations of read statistics**
- Provide a **clear summary suitable for non-technical researchers**

---

# Pipeline Overview

The workflow processes a FASTQ file and produces quality metrics and visual summaries of the dataset.

Pipeline steps:

FASTQ Input  
│  
├── calculate_metrics (Python script)  
│       Computes GC content, read length, and mean quality  
│  
├── plot_metrics  
│       Generates distribution plots and summary statistics  
│  
└── nanoplot_qc  
        Performs long-read QC using NanoPlot  

A Directed Acyclic Graph (DAG) of the pipeline can be generated with:

snakemake --dag | dot -Tpng > dag.png

---

# Metrics Calculated

For each sequencing read, the pipeline calculates:

| Metric | Description |
|------|------|
| Read Length | Total number of bases in a read |
| GC Content | Percentage of G and C nucleotides |
| Mean Read Quality | Average Phred quality score |

These metrics help evaluate the **overall sequencing performance and data quality**.

---

# Key Results

Summary statistics of the dataset:

| Metric | Value |
|------|------|
Total reads | ~314,149  
Total bases | ~1.85 Gb  
Mean read length | ~5,893 bp  
Median read length | ~2,057 bp  
Read length N50 | ~15,909 bp  
Mean read quality | ~8.7  
Median read quality | ~9.4  

Approximately **34% of reads have quality scores above Q10**, which is typical for raw Oxford Nanopore sequencing data.

---

# Visualizations

The pipeline generates several plots to visualize the dataset characteristics.

### GC Content Distribution

![GC Distribution](results/gc_distribution.png)

The GC content distribution is centered around **50–52%**, suggesting balanced nucleotide composition and no major bias in base representation.

---

### Read Length Distribution

![Length Distribution](results/length_distribution.png)

The read length distribution shows the typical long-read pattern:

- many shorter reads
- fewer extremely long reads

Some reads exceed **100,000 bases**, which is consistent with Oxford Nanopore sequencing.

---

### Mean Read Quality Distribution

![Quality Distribution](results/quality_distribution.png)

The quality distribution peaks around **Q9–Q12**, which falls within the expected range for raw Nanopore sequencing data.

---

# NanoPlot Quality Control

The pipeline also runs **NanoPlot**, a specialized QC tool for long-read sequencing datasets.

NanoPlot provides additional analyses including:

- read length histograms
- quality vs length plots
- sequencing yield statistics

These outputs help confirm the overall characteristics of the dataset.

---

# Installation

Clone the repository:

git clone https://github.com/happymealinthebuilding/14th-Massive-Bioinformatics-Assessment.git  
cd 14th-Massive-Bioinformatics-Assessment

Create the Conda environment:

conda env create -f envs/environment.yml  
conda activate bioinfo_assessment

---

# Running the Pipeline

Place the FASTQ file inside the `data` directory:

data/VREC1013.fastq.gz

Then run:

snakemake --cores 1 -s workflow/Snakefile

This will automatically execute the entire workflow.

---

# Output Files

The pipeline produces the following outputs:

results/

read_metrics.csv  
summary_statistics.csv  
gc_distribution.png  
length_distribution.png  
quality_distribution.png  

nanoplot/

NanoPlot-report.html  
additional QC plots  

---

# Interpretation of Results

The analysis suggests that the sequencing dataset has **typical characteristics of Oxford Nanopore long-read data**:

- GC content distribution appears normal
- Read lengths include many long reads with some exceeding 100 kb
- Quality scores fall within expected ranges for Nanopore sequencing

Overall, the dataset appears **suitable for downstream genomic analysis**.

---

# Recommended Next Steps

Based on the quality assessment, the following steps are recommended:

1. Align the reads to a reference genome
2. Perform genome assembly or structural variant analysis
3. Apply additional filtering if higher quality thresholds are required

---

# Reproducibility

This pipeline ensures reproducibility by:

- using **Snakemake workflow management**
- defining dependencies via **Conda environment**
- keeping scripts modular and version-controlled

---

# Author

Azra Tuncay

Bioinformatics Pipeline Project