from pprint import pprint
import re


with open('conll/full_adam/adam.all.udv1.conllu') as f:
    d = f.readlines()

remainders = []
def process(line):
    if line == '\n':
        return line
    word_id,form,lemma,*rest = line.split('\t')
    if rest[3] == '0' and rest[4] not in ('root','root:promoted'):
        rest[4] = 'root'
    if rest[0] == 'PUNCT':
        rest[4] = 'punct'
        #print('\t'.join([word_id,form,lemma]+rest))
    line = '\t'.join([word_id,form,lemma]+rest)
    word_id = int(word_id)
    if '_' not in lemma:
        return line
    modified_line = line.replace(lemma,lemma.split('_')[0])
    if lemma in ('have_to','has_to'):
        new_line = f'{word_id+1}\tto\tto\tPART\tinf\t_\t{word_id+2}\tmark\t_\t_\n'
        return modified_line+new_line
    elif lemma == 'thank_you':
        new_line = f'{word_id+1}\tyou\tyou\tPRON\tpro;per\t_\t{word_id}\tobj\t_\t_\n'
        return modified_line+new_line
    elif lemma[0].isupper():
        second_name = lemma.split('_')[1] # second part of the name
        new_line = f'{word_id+1}\t{second_name}\t{second_name}\tPROPN\tn:prop\t_\t{word_id}\tflat\t_\t_\n'
        return modified_line+new_line
    elif lemma == 'out_of':
        new_line = f'{word_id+1}\tof\tof\tADP\tprep\t_\t{word_id}\tfixed\t_\t_\n'
        return modified_line+new_line
    elif lemma in ('cock_a_doodle_doo','dum_dum','night_night','rock_a_bye','ups_a_daisy'):
        new_lemma = lemma.replace('_','-')
        modified_line = line.replace(lemma,new_lemma)
        return modified_line
    else:
        remainders.append(lemma)
        return line
    #orig_line = '\t'.join([word_id,form,lemma]+rest)
    #return new_line+orig_line

def fix_possible_id_overlaps(form):
    if form == '':
        return form
    while True:
        ids = [x.split()[0] for x in form.split('\n')]
        if ids == [str(x) for x in range(1,len(ids)+1)]:
            return form
        possible_ids = sorted([int(x) for x in set(ids) if ids.count(x) == 2])
        duplicate_id = possible_ids[0]
        if len(possible_ids) > 1:
            print(possible_ids,duplicate_id)
        lines = form.split('\n')
        out_lines = []
        for i,line in enumerate(lines):
            if i != duplicate_id-1:
                for j in reversed(range(duplicate_id,len(ids))):
                    #line = line.replace(f'{i}',f'{i+1}').replace('4S','3S').replace('2S','1S')
                    line = re.sub(fr'\b{j}',f'{j+1}',line)
            out_lines.append(line)
        form = '\n'.join(out_lines)

split_lines_ = ''.join([process(x) for x in d])
split_lines_list = []
for i,form in enumerate(split_lines_.split('\n\n')):
    split_lines_list.append(fix_possible_id_overlaps(form))
split_lines = '\n\n'.join(split_lines_list)
with open('conll/full_adam/adam.all.udv1.conllu.final','w') as f:
    for line in split_lines.split('\n'):
        f.write(line+'\n')
pprint(sorted([(x,remainders.count(x)) for x in set(remainders)],key=lambda x:-x[1]))
with open('leftover_compounds.txt','w') as f:
    for x in sorted(list(set(remainders))):
        f.write(x+'\n')
