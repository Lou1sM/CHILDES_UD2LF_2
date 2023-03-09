import re
import sys


corpus = sys.argv[1]


with open(f'conll/full_{corpus}/{corpus}.all.conll.txt') as f:
    d = f.readlines()

MORPHO_TO_UD_MORPHO = {'':'',
                        'ZERO':'ZERO',
                        'PAST':'Tense=Past',
                        'PASTP':'Tense=Past|Aspect=Perf',
                        'PRES':'Tense=Pres',
                        'PRESP':'Tense=Pres|Aspect=Perf',
                        'PL':'Number=Plur',
                        '3S':'Number=Sing|Person=3',
                        '1S':'Number=Sing|Person=1'}
all_morphos = []
all_combinations = []
def process_line(line):
    if line == '\n' or '<quotation' in line:
        return line
    cols = line.split()
    if cols[1] in ['?','.','!']:
        return line
    if not len(cols) == 10:
        print(line)
        cols = cols[:2] + ['-s'] + cols[2:]
    assert ('|' in cols[1]) == (corpus == 'adam')
    if corpus == 'adam':
        pos, lemma_morpho = cols[1].split('|')
        lemma_morpho = re.sub(r'_\d{1,2}$','',lemma_morpho)
        lemma, _, morpho = lemma_morpho.partition('-')
    elif corpus == 'hagar':
        lemma = cols[1]
        pos = cols[4]
        morpho = ''
    #lemma_morpho = lemma_morpho[:-2] # remove trailing e.g. _2
    if not pos.replace(';',':') == cols[4]:
        print(pos,cols[4])
    if '-' in morpho:
        breakpoint()
    all_morphos.append(morpho)
    if '_' in lemma:
        all_combinations.append(lemma)
    #try:
        #ud_morpho = MORPHO_TO_UD_MORPHO[morpho]
    #except KeyError:
        #breakpoint()
    ud_morpho = '_' if morpho == '' else morpho
    if ud_morpho != '_': print(ud_morpho)
    assert cols[5] == '_'
    return '\t'.join([cols[0],cols[2],lemma,cols[3],cols[4],ud_morpho,cols[6],cols[7],cols[8],cols[9]])+'\n'

with open(f'conll/full_{corpus}/{corpus}.all.udv1.conllu','w') as f:
    for in_line in d:
        converted = process_line(in_line)
        f.write(converted)

compounds_and_counts = [(k,all_combinations.count(k)) for k in set(all_combinations)]
with open(f'compounds_{corpus}.txt','w') as f:
    f.write('COMPOUND' + ' '*14 + 'COUNT\n')
    for compound,count in sorted(compounds_and_counts,key=lambda x:-x[1]):
        f.write(compound + ' '*(22-len(compound)) + str(count) + '\n')
