import web
from gaesessions import get_current_session

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
        session = get_current_session()
        if session['login'] != 1:
            raise web.seeother('/login', absolute = True)
        return web.ctx.render.sequencing(session['privilege'])
