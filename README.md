This repository includes the files both of the Universal Dependency (UD) parses, and the result of converting them to logical form (LFs) as meaning representations, for two corpora of child-directed speech. The Adam CHILDES corpus consists of transcribed interactions, in English, between parents and a child of age-range 2;3-3;11. The Hagar CHILDES corpus consists of transcribed interactions, in Hebrew, between parents and a child of age-range 1;7-3;3. Our annotations in this repo include only the parent utterances, of which there are 17233 utterances for Adam and 24166 utterances for Hagar. After our conversion to LFs, there are 13593 for Adam and 15916 for Hagar.

The repo consists of the following directories:

* _conll_: manually annotated UD files in the conllu (UD-V1) format. These files have passed the tests of [this automatic validator](https://github.com/UniversalDependencies/tools/tree/r1.4).
* _LF_files_: the converted LFs in free text format.
* _src_: the source files for the converter.
* _fixes_for_validator_: code and notes about slight changes to make the UD annotations consistent with the automatic validator.


Details about both the annotation and the coversion efforts can be found in:


[Cross-linguistically Consistent Semantic and Syntactic Annotation of Child-directed Speech](https://arxiv.org/abs/2109.10952)<br>
Ida Szubert, Omri Abend, Nathan Schneider, Samuel Gibbon, Louis Mahon, Sharon Goldwater, Mark Steedman

