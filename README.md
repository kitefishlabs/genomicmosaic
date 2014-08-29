genomicmosaic
=============

Use genetic algorithms (GAs) to tile fragments of sound files. genomicmosaic is a framework for specifying and evolving parameters for the following chain of sub-processes:

genomicmosaic is a framework for the construction of sound sequences out of tiles or segments of existing digitized sound recordings or samples (mosaic). It is also a simple framework for evolving sound designs using this rigorous, constrained approach (genomic).

- Source audio files are collected into a pool.
- A target sound file is selected.
- Sound files are analyzed and raw data stored to disc.
- Parameters for the following are seeded:
  - segmentation algorithm
  - anaysis data weighting/filtering
  - segment constraints (i.e., minimum acceptable length, windowing, etc.)
  - matching factors (relax or tighten limits on accuracy of segment-to-target similarity scores)
  - GA metaparameters (pop. size, mut. rate, etc.)
- Parameters are evolved through mutation, 2-point crossover, deterministic crowding---or elitist?---replacement for shorter target sounds.
- Results for each run are stored along with their parameters. Exemplars can be selected by a human operator and rerun with different (and longer!) target and/or source sounds.

Goals
-----

1. Novel, engaging sounds compsed of tiles (fragments) of other sounds.
2. Reproducability.
3. Scalability (1000's of sounds in a source pool, long target sounds, huge numbers of tiling operations.)

Process
-------

genomicmosaic is owned by all its authors and contributors. This is an open source project licensed under the LGPLv3. This is an experiment in growing a project using the [C4.1 process](http://http://rfc.zeromq.org/spec:22). If you are interested in contributing, please read about the process and get in touch.
