import subprocess as proc
def runcmd(c):
    output = proc.getoutput(c)
    print(output)

runcmd('ls')

runcmd('ls')

output = proc.getoutput(c)


