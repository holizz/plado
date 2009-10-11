
import subprocess

def git(cmd, *args):
    return subprocess.Popen(['git',cmd]+list(args), stdout=subprocess.PIPE).communicate()[0].decode()

def nicename(sha):
    r = ' '.join(git('rev-list','--no-walk','--format=%d',sha).strip().split())
    if len(r) == 0: return None
    else:           return r

def leaf(tree, pos):
    if len(pos) == 0: return tree
    else:             return leaf(tree[pos[0]], pos[1:])

def printtree(tree, depth=1):
    for name, child in tree.items():
        print(('*'*depth) + ' ' + name)
        printtree(child,depth+1)

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
    revlist = git('rev-list',branch).split()
    pos = ['']
    for rev in revlist:
        r = nicename(rev)
        leaf(tree, pos)[r] = {}
        pos.append(r)

# Pretty print

printtree(tree)
