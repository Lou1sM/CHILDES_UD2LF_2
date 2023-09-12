"""Fix examples where a PUNCT node is the head."""


def process_form(form):
    words = form.split('\n')
    roots = [w for w in words if w.split()[6] == '0' and w.split()[7] == 'root']
    if len(roots) == 0: # then looks for ones with HEAD 0 or labelled root, rather than both
        roots = [w for w in words if w.split()[6] == '0' or w.split()[7] == 'root']
        if len(roots) != 1:
            print(f'Num maybe roots: {len(roots)}')
    root = roots[0]
    root_id = root.split()[0]
    processed_words = []
    # if there is only one potential root, then give it both HEAD=0 and 'root'
    for w in words[:-1]:
        if w.split()[0] == root_id:
            w = '\t'.join(['0' if i==6 else 'root' if i==7 else x for i,x in enumerate(w.split())])
        processed_words.append(w)
    # sentence-final punct should always have root as its HEAD
    punct = words[-1]
    if punct.split()[3] != 'PUNCT':
        print(form)
        return form
    new_punct = '\t'.join([root_id if i==6 else x for i,x in enumerate(punct.split())])+'\n'
    processed_words.append(new_punct)
    return '\n'.join(processed_words)


with open('conll/full_hagar/hagar.all.udv1.conllu') as f:
    d = f.read()
with open('conll/full_hagar/hagar.all.udv1.conllu.current','w') as f:
    for i,form in enumerate(d.split('\n\n')):
        if form == '':
            continue
        f.write(process_form(form)+'\n')
