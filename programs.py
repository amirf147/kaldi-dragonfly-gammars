# commands for controlling various programs

try:
    from aenea import *
except:
    from dragonfly import *

gitcommand_array = [
    'add',
    'branch',
    'checkout',
    'clone',
    'commit',
    'diff',
    'fetch',
    'init',
    'log',
    'merge',
    'pull',
    'push',
    'rebase',
    'reset',
    'show',
    'stash',
    'status',
    'tag',
]
gitcommand = {}
for command in gitcommand_array:
    gitcommand[command] = command

class ProgramsRule(MappingRule):
    mapping = {
        "vim save": Key("escape, colon, w, enter"),
        "vim quit": Key("escape, colon, q, enter"),
        "vim really quit": Key("escape, colon, q, exclamation, enter"),
        "vim save and quit": Key("escape, colon, w, q, enter"),
        "vim split": Text(":sp "),
        "vim vertical split": Text(":vs "),
        "vim tab new": Text(":tabnew "),
        "vim tab close": Text(":tabclose\n"),

        "vim open source": Text(":vs %<.c\n"),
        "vim open source plus": Text(":vs %<.cpp\n"),
        "vim open header": Text(":vs %<.h\n") + Key('c-w, c-w'),
        "vim next [tab] [<n>]": Text(':tabnext +%(n)d\n'),
        "vim previous [tab] [<n>]": Text(':tabprevious %(n)d\n'),
        "vim (switch|toggle|swap)": Key('c-w, c-w'),
        "vim rotate": Key('c-w, r'),
        "vim try that": Key('escape, colon, w, enter, a-tab/5, up, enter'),

        'screen': Key('c-a'),
        'screen switch': Key('c-a, c-a'),
        'screen scroll': Key('c-a, lbracket'),

        "just execute": Key("backspace, enter"),
        "command (git|get)": Text("git "),
        "command (git|get) <gitcommand>": Text("git %(gitcommand)s "),
        "command vim": Text("vim "),
        #"command C D": Text("cd "),
        #"command list": Text("ls "),
        "command make": Text("make "),
        "command make clean": Text("make clean "),
        #"command cat": Text("cat "),
        "command (grep|grip)": Text("grep "),
        #"command background": Text("bg "),
        #"command foreground": Text("fg "),

        # web browser
        'address bar': Key('a-d'),
        'refresh page': Key('f5'),
        'really refresh page': Key('s-f5'),
        'go back [<n>]': Key('a-left:%(n)d'),
        'go forward [<n>]': Key('a-right:%(n)d'),
        'tab over [<n>]': Key('c-pgup:%(n)d'),
        'tab under [<n>]': Key('c-pgdown:%(n)d'),
        'tab new': Key('c-t'),
        'tab close': Key('c-w'),
        
        # tab selection with numbers
        "page first": Key("c-1"),
        "page second": Key("c-2"),
        "page third": Key("c-3"),
        "page fourth": Key("c-4"),
        "page fifth": Key("c-5"),
        "page sixth": Key("c-6"),
        "page seventh": Key("c-7"),
        "page eighth": Key("c-8"),
        "page (last|ninth|minus [one])": Key("c-9"),

        # tab selection with negative numbers
        "page minus two": Key("c-9, c-pgup"),
        "page minus three": Key("c-9, c-pgup:2"),
        "page minus four": Key("c-9, c-pgup:3"),
        "page minus five": Key("c-9, c-pgup:4"),
        "page minus six": Key("c-9, c-pgup:5"),
        "page minus seven": Key("c-9, c-pgup:6"),
        "page minus eight": Key("c-9, c-pgup:7"),
        "page minus nine": Key("c-9, c-pgup:8"),

        # Xfce-like desktop environment commands
        '(desk|desktop) left [<n>]': Key('ca-left:%(n)d'),
        '(desk|desktop) right [<n>]': Key('ca-right:%(n)d'),
        '(desk|desktop) up [<n>]': Key('ca-up:%(n)d'),
        '(desk|desktop) down [<n>]': Key('ca-down:%(n)d'),
        '(desk|desktop) (top|upper) [<n>]': Key('c-f1, ca-left, ca-right:%(n)d'),
        '(desk|desktop) (bottom|lower) [<n>]': Key('c-f1, ca-down, ca-left, ca-right:%(n)d'),
        'switch window [<n>]': Key('a-tab:%(n)d'),
        'really close window': Key('a-f4'),
        'maximize window': Key('a-f10'),
        'minimize window': Key('a-f9'),
        'open new terminal': Key('ca-m'),
        'copy this image': Key('c-c/10,ca-right/10,c-v/10,ca-left'),
        'image go up': Key('a-up'),
        'read elf': Text('readelf -Wa '),
        'object dump': Text('objdump -d '),
        'code standard': Text('std::'),
        'code vector': Text('vector'),
        'code map': Text('map'),
        'code list': Text('map'),
        'code string': Text('string'),
        'standard string': Text('std::string'),
        'standard vector': Text('std::vector'),
        'standard map': Text('std::map'),
        'standard list': Text('std::list'),
        'const': Text('const '),
    }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 100),
        Choice('gitcommand', gitcommand),
    ]
    defaults = {
        "n": 1,
    }
