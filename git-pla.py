
import subprocess

def git(cmd, *args):
    return subprocess.Popen(['git',cmd]+list(args), stdout=subprocess.PIPE).communicate()[0].decode()

def leaf(tree, pos):
    while True:
        if len(pos) == 0:
            return tree
        else:
            tree = tree[pos[0]]
            pos = pos[1:]

def printtree(tree):
    tosee = []
    pos = ['']
    while True:
        subtree = leaf(tree, pos)
        for child in subtree.keys():
            tosee.append(pos+[child])
        print(('*'*len(pos)) + ' ' + pos[-1])
        if len(tosee) == 0:
            return
        pos = tosee.pop(0)

# Get a rev-list for each branch

branches = [x.strip() for x in git('branch').strip().split('\n')]
for branch in branches:
    if branch.startswith('* '):
        head = branch.lstrip('* ')
branches[branches.index('* '+head)] = head

# Build a tree (ignoring merges)

# in case there are branches with no common commits, start with a blank node
tree = {'':{}}

for branch in branches:
    revlist = []
    for rev in reversed(git('rev-list','--format=%d','HEAD').split('commit ')):
        if rev == '':
            continue
        lst = rev.split('\n')
        r = lst[0][0:5]
        if len(lst) > 1 and len(lst[1]) > 0:
            r += ' ' + lst[1].strip()
        revlist.append(r)
    pos = ['']
    for rev in revlist:
        leaf(tree, pos)[rev] = {}
        pos.append(rev)

# Pretty print

printtree(tree)
