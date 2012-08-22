import web

urls = (
    '', 'Sequencing',
)
sequencing = web.application(urls, locals())

"""
Sequencing takes 3 arguments - error_code, output, privilege level

Error_codes are :
    - 0 = nothing is wrong
    - 1 = no seq1 is entered
    - 2 = no seq2 is entered

Output is structured in an array like this:
    - output[0] = length of seq 1
    - output[1] = length of seq 2
    - output[2] = no. gs + no. cs

Privilege levels determine the output seen:
    0 - does not see no. gs + no. cs
    1 - does see no. gs + no. cs
"""

def count_occurrences(char, seq):
    return seq.count(char)

class Sequencing():
    def GET(self):
        if web.ctx.session.login != 1:
            raise web.seeother('/login', absolute = True)
        return web.ctx.render.sequencing(web.ctx.session.privilege)
    def POST(self):
        i = web.input()

        seq1 = i.seq1
        seq2 = i.seq2

        if(seq1 == ""):
            return web.ctx.render.sequencing(web.ctx.session.privilege)
        elif(seq2 == ""):
            return web.ctx.render.sequencing(web.ctx.session.privilege)

        len1 = len(seq1)
        len2 = len(seq2)

        seq1_num_c = count_occurrences('c', seq1)
        seq1_num_g = count_occurrences('g', seq1)

        output = [len1, len2, seq1_num_c + seq1_num_g]
        return web.ctx.render.sequencing(web.ctx.session.privilege)

