This repository contains syntactic and semantic annotations of child-directed speech in English and Hebrew. The syntactic annotations are dependency trees following version 1 of the [Universal Dependencies](https://universaldependencies.org/) (UD) framework, and the semantic annotations are logical forms (LFs) automatically derived from the UD trees by a rule-based conversion procedure.

The source data comes from the [CHILDES database](https://childes.talkbank.org/):
- the Adam corpus (collected by [Brown](https://childes.talkbank.org/access/Eng-NA/Brown.html)) consists of transcribed interactions, in English, between parents and a child of age-range 2;3-3;11
- the Hagar corpus (collected by [Berman](https://childes.talkbank.org/access/Other/Hebrew/BermanLong.html)) consists of transcribed interactions, in Hebrew, between parents and a child of age-range 1;7-3;3

Annotations in this repo cover only the adult utterances—most of the ones in the Adam dataset, and all of the Hagar dataset. UD trees cover 17233 utterances for Adam and 24166 utterances for Hagar. After our conversion to LFs, there are 13593 utterances for Adam and 15916 for Hagar.

| Example UD tree | Corresponding LF |
|-----------------|------------------|
<img width="281" alt="image" src="https://github.com/Lou1sM/CHILDES_UD2LF_2/assets/985263/b3a23c0d-b1f4-4d45-bb7a-0731deaf8dbc"> | <img width="338" alt="image" src="https://github.com/Lou1sM/CHILDES_UD2LF_2/assets/985263/748c8f52-3a5c-4efd-a2b5-da4ced746c32">


The repo consists of the following directories:

* _conll_: manually annotated UD files in the CoNLL-U format. Errors flagged by [the UD validator](https://github.com/UniversalDependencies/tools/tree/r1.4) have been corrected.
   - Formally validated and manually checked Adam trees are in the file: [adam.all.udv1.conllu.final](conll/full_adam/adam.all.udv1.conllu.final)
   - Formally validated Hagar trees are in the file: [hagar.all.udv1.conllu.current](conll/full_hagar/hagar.all.udv1.conllu.current)
* _LF_files_: the converted LFs in free text format.
   - Full data: [Adam](LF_files/full_adam), [Hagar](LF_files/full_hagar)
* _src_: the source files for the converter.
* _fixes_for_validator_: code and notes about slight changes to make the UD annotations consistent with the automatic validator.



Details about both the annotation and the conversion efforts can be found in:

[Cross-linguistically Consistent Semantic and Syntactic Annotation of Child-directed Speech](https://arxiv.org/abs/2109.10952)  
Ida Szubert, Omri Abend, Nathan Schneider, Samuel Gibbon, Louis Mahon, Sharon Goldwater, Mark Steedman  
To appear in *Language Resources and Evaluation*.
