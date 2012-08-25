from web.template import CompiledTemplate, ForLoop, TemplateResult


# coding: utf-8
def admin(error_code):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    extend_([u'\n'])
    extend_([u'\n'])
    extend_([u'\n'])
    extend_([u'\n'])
    extend_([u'<div id="container">\n'])
    extend_([u'    <div id="top">\n'])
    extend_([u'        <h1>Administration</h1>\n'])
    extend_([u'    </div>\n'])
    extend_([u'\n'])
    extend_([u'    <div id="content">\n'])
    if error_code == 1:
        extend_(['        ', u'<h2 class="error">That user has already been created</h1><br />\n'])
    extend_([u'        <form method="post" action="/admin/Add_User">\n'])
    extend_([u'            <h2>New Username: <input type="text" name="username" /></h2>\n'])
    extend_([u'            <h2>New Password: <input type="password" name="password" /></h2>\n'])
    extend_([u'            <h2>Privilege: </h2>\n'])
    extend_([u'            <input type="radio" name="privilege" value="1" checked/>Can see no. c + no. g <br />\n'])
    extend_([u'            <input type="radio" name="privilege" value="0" />Can not see no. c + no. g <br /> \n'])
    extend_([u'            <br />\n'])
    extend_([u'            <input type="submit" value="New User" />\n'])
    extend_([u'        </form>\n'])
    extend_([u'    </div>\n'])
    extend_([u'</div>\n'])

    return self

admin = CompiledTemplate(admin, 'templates\\admin.html')
join_ = admin._join; escape_ = admin._escape

# coding: utf-8
def base (content):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<!DOCTYPE HTML>\n'])
    extend_([u'<html>\n'])
    extend_([u'    <head>\n'])
    extend_([u'        <title>Sequencing</title>\n'])
    extend_([u'        <link rel="stylesheet" type="text/css" href="/static/site.css"/>\n'])
    extend_([u'        <script type="text/javascript" src="static/libs/jquery-1.8.0.min.js"></script>\n'])
    extend_([u'    </head>\n'])
    extend_([u'    <body>\n'])
    extend_([u'        ', escape_(content, False), u'\n'])
    extend_([u'    </body>\n'])
    extend_([u'</html>\n'])

    return self

base = CompiledTemplate(base, 'templates\\base.html')
join_ = base._join; escape_ = base._escape

# coding: utf-8
def index():
    __lineoffset__ = -5
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])

    return self

index = CompiledTemplate(index, 'templates\\index.html')
join_ = index._join; escape_ = index._escape

# coding: utf-8
def login(error_code):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<div id="container">\n'])
    extend_([u'    <div id="top">\n'])
    extend_([u'        <h1>Test Page</h1>\n'])
    extend_([u'    </div>\n'])
    extend_([u'    <div id="content">\n'])
    if error_code == 1:
        extend_(['        ', u'<h2 class="error">That is not a valid login</h2><br />\n'])
    elif error_code == 2:
        extend_(['        ', u'<h2 class="error">That is an incorrect password</h2><br />\n'])
    extend_([u'        <form method="post" action="login">\n'])
    extend_([u'            <h2>Username: <input type="text" name="username" /></h2>\n'])
    extend_([u'            <h2>Password: <input type="password" name="password" /></h2>\n'])
    extend_([u'            <input type="submit" value="Login" />\n'])
    extend_([u'        </form>\n'])
    extend_([u'    </div>\n'])
    extend_([u'</div>\n'])

    return self

login = CompiledTemplate(login, 'templates\\login.html')
join_ = login._join; escape_ = login._escape

# coding: utf-8
def sequencing (privilege):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    __lineoffset__ -= 3
    def create_output(label, name):
        self = TemplateResult(); extend_ = self.extend
        extend_([u'<h4 class="output">', escape_(label, False), u' = <span id="', escape_(name, False), u'"></span></h4>\n'])
        extend_([u'\n'])
        return self
    __lineoffset__ -= 3
    def create_pos_tracker(position_for, id):
        self = TemplateResult(); extend_ = self.extend
        extend_([u'<p>Position in ', escape_(position_for, False), u': <span id="pos_', escape_(id, False), u'"></span></p>\n'])
        extend_([u'\n'])
        return self
    __lineoffset__ -= 3
    def create_input(name, constraints, id):
        self = TemplateResult(); extend_ = self.extend
        extend_([u'<h3>', escape_(name, False), u' [', escape_(constraints, False), u']</h3>\n'])
        extend_([u'<textarea class="tracked" cols="50" rows="10" id="', escape_(id, False), u'"></textarea> <br />\n'])
        extend_([escape_(create_pos_tracker(name, id), False), u'\n'])
        extend_([u'\n'])
        return self
    extend_([u'<script type="text/javascript" src="static/output.js"></script>\n'])
    extend_([u'<div id="app">\n'])
    extend_([u'    <div id="top">\n'])
    extend_([u'        <h1>Input Sequences</h1>\n'])
    extend_([u'        <span id="error_message"></span>\n'])
    extend_([u'    </div>\n'])
    extend_([u'    <div id="left">\n'])
    extend_([u'        ', escape_(create_input("Sequence 1", "minimum = 100, maximum = 20000", "seq1"), False), u'\n'])
    extend_([u'        ', escape_(create_input("Sequence 2", "minimum = 15, maximum = 17000", "seq2"), False), u'\n'])
    extend_([u'        <input type="submit" value="Go" id="submit_button" />\n'])
    extend_([u'    </div>\n'])
    extend_([u'\n'])
    extend_([u'    <div id="right">\n'])
    extend_([u'        <h2>Output</h2> \n'])
    extend_([u'        <br />\n'])
    extend_([u'        ', escape_(create_output("Length of Sequence 1", "seq1_len"), False), u'\n'])
    extend_([u'        ', escape_(create_output("Length of Sequence 2", "seq2_len"), False), u'\n'])
    if privilege == 1:
        extend_(['        ', escape_(create_output("No. Cs + No. Gs", "cg_occurrence"), False), u'\n'])
    extend_([u'        <br />\n'])
    extend_([u'        <div id="output_seq">\n'])
    extend_([u'            <h4>Output Sequence: </h4>\n'])
    extend_([u'            <div id="output_text">\n'])
    extend_([u'                <textarea class="readonly tracked" id="output_textarea" cols="50" rows="10" placeholder="Output sequence will go here"></textarea>\n'])
    extend_([u'                ', escape_(create_pos_tracker("Output Sequence", "output_textarea"), False), u'\n'])
    extend_([u'            </div>\n'])
    extend_([u'        </div>\n'])
    extend_([u'        \n'])
    extend_([u'    </div>\n'])
    extend_([u'</div>\n'])

    return self

sequencing = CompiledTemplate(sequencing, 'templates\\sequencing.html')
join_ = sequencing._join; escape_ = sequencing._escape

