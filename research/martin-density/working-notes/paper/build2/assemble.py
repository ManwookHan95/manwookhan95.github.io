import os,sys
base='/tmp/claude-0/-home-user-manwookhan95-github-io/ec871029-cb65-5b86-9917-5095aaba7b7b/scratchpad/ctx/paper/'
src=open(base+'build2/edited.tex').read() if os.path.exists(base+'build2/edited.tex') else open(base+'build2/orig.tex').read()
parts=[p for p in sys.argv[1:]]
ins=''.join(open(base+'newparts/'+p).read() for p in parts)
marker=r'\section{Status of the density problem}'
assert marker in src
out=src.replace(marker, ins+'\n'+marker)
open(base+'build2/martin_density_note.tex','w').write(out)
