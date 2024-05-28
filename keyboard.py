# Low-level keyboard input module
#
# Based on the work done by the creators of the Dictation Toolbox
# https://github.com/dictation-toolbox/dragonfly-scripts
#
# and _multiedit-en.py found at:
# http://dragonfly-modules.googlecode.com/svn/trunk/command-modules/documentation/mod-_multiedit.html
#
# Modifications by: Tony Grosinger
#
# Licensed under LGPL

try:
    from aenea import *
except:
    from dragonfly import *

try:
    from dragonfly.actions.keyboard import keyboard
    from dragonfly.actions.typeables import typeables
    if 'semicolon' not in typeables:
        typeables["semicolon"] = keyboard.get_typeable(char=';')
except:
    pass

from words import handle_word

release = Key("shift:up, ctrl:up, alt:up")


def cancel_and_sleep(text=None, text2=None):
    """Used to cancel an ongoing dictation and puts microphone to sleep.

    This method notifies the user that the dictation was in fact canceled,
     a message in the Natlink feedback window.
    Then the the microphone is put to sleep.
    Example:
    "'random mumbling go to sleep'" => Microphone sleep.

    """
    try:
        from natlink import setMicState
        setMicState("sleeping")
        print("* Dictation canceled. Going to sleep. *")
    except:
        pass


# For repeating of characters.
specialCharMap = {
    "(pipe)": "|",
    "(dash|minus|hyphen)": "-",
    "dot": ".",
    "comma": ",",
    "backslash": "\\",
    "underscore": "_",
    "(star|asterisk)": "*",
    "colon": ":",
    "(semicolon|semi colon)": ";",
    "at symbol": "@",
    "[double] quote": '"',
    "single quote": "'",
    "hash": "#",
    "dollar": "$",
    "percent": "%",
    "ampersand": "&",
    "slash": "/",
    "equals [sign]": "=",
    "plus sign": "+",
    "space": " ",

    "exclamation [mark]": "!",
    "question": "?",
    "caret": "^",
    # some other symbols I haven't imported yet, lazy sorry
    # 'ampersand': Key('ampersand'),
    # 'apostrophe': Key('apostrophe'),
    # 'asterisk': Key('asterisk'),
    # 'at': Key('at'),
    # 'backslash': Key('backslash'),
    # 'backtick': Key('backtick'),
    # 'bar': Key('bar'),
    # 'caret': Key('caret'),
    # 'colon': Key('colon'),
    # 'comma': Key('comma'),
    # 'dollar': Key('dollar'),
    # #'(dot|period)': Key('dot'),
    # 'double quote': Key('dquote'),
    # 'equal': Key('equal'),
    # 'bang': Key('exclamation'),
    # 'hash': Key('hash'),
    # 'hyphen': Key('hyphen'),
    # 'minus': Key('minus'),
    # 'percent': Key('percent'),
    # 'plus': Key('plus'),
    # 'question': Key('question'),
    # # Getting Invalid key name: 'semicolon'
    # #'semicolon': Key('semicolon'),
    # 'slash': Key('slash'),
    # '[single] quote': Key('squote'),
    # 'tilde': Key('tilde'),
    # 'underscore | score': Key('underscore'),
}

# Modifiers for the press-command.
modifierMap = {
    "alt": "a",
    "angry": "a",
    "control": "c",
    "shift": "s",
    "super": "w",
}

# Modifiers for the press-command, if only the modifier is pressed.
singleModifierMap = {
    "alt": "alt",
    "angry": "alt",
    "control": "ctrl",
    "shift": "shift",
    "super": "win",
}

letterMap = {
    "(alpha|arch)": "a",
    "(bravo|brav) ": "b",
    "(charlie) ": "c",
    "(delta)": "d",
    "(echo)": "e",
    "(foxtrot|fox) ": "f",
    "(golf) ": "g",
    "(hotel) ": "h",
    "(india|indigo) ": "i",
    "(juliet|julia) ": "j",
    "(kilo) ": "k",
    "(lima) ": "l",
    "(mike) ": "m",
    "(november) ": "n",
    "Oscar": "o",
    "(papa|poppa) ": "p",
    "(quebec) ": "q",
    "(romeo) ": "r",
    "(sierra) ": "s",
    "(tango) ": "t",
    "(uniform) ": "u",
    "(victor) ": "v",
    "(whiskey) ": "w",
    "(x-ray) ": "x",
    "(yankee) ": "y",
    "(zulu) ": "z",
}
#letterMap = {
    #"(alpha|arch)": "a",
    #"(bravo|brav) ": "b",
    #"(charlie|turley|char) ": "c",
    #"(delta|del) ": "d",
    #"(echo|eck) ": "e",
    #"(foxtrot|fox) ": "f",
    #"(golf|gang) ": "g",
    #"(hotel) ": "h",
    #"(india|indigo|ish) ": "i",
    #"(juliet|julia) ": "j",
    #"(kilo) ": "k",
    #"(lima|lion|line|lie) ": "l",
    #"(mike) ": "m",
    #"(november|noy) ": "n",
    #"(Oscar|osh) ": "o",
    #"(papa|poppa|pom) ": "p",
    #"(quebec|quiche|queen) ": "q",
    #"(romeo|ree) ": "r",
    #"(sierra|soy) ": "s",
    #"(tango|tay) ": "t",
    #"(uniform|umm) ": "u",
    #"(victor|van) ": "v",
    #"(whiskey|wes) ": "w",
    #"(x-ray) ": "x",
    #"(yankee|yaa) ": "y",
    #"(zulu) ": "z",
#}


# generate uppercase versions of every letter
upperLetterMap = {}
for letter in letterMap:
    upperLetterMap["(upper|sky) " + letter] = letterMap[letter].upper()
letterMap.update(upperLetterMap)

numberMap = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

controlKeyMap = {
    "left": "left",
    "right": "right",
    "up": "up",
    "down": "down",
    "page up": "pgup",
    "page down": "pgdown",
    "home": "home",
    "end": "end",
    "space": "space",
    "(enter|return)": "enter",
    "escape": "escape",
    "tab": "tab",
    "backs": "backspace"
}

# F1 to F12. (do these actually work?)
functionKeyMap = {
    'F one': 'f1',
    'F two': 'f2',
    'F three': 'f3',
    'F four': 'f4',
    'F five': 'f5',
    'F six': 'f6',
    'F seven': 'f7',
    'F eight': 'f8',
    'F nine': 'f9',
    'F ten': 'f10',
    'F eleven': 'f11',
    'F twelve': 'f12',
}

pressKeyMap = {}
pressKeyMap.update(letterMap)
pressKeyMap.update(numberMap)
pressKeyMap.update(controlKeyMap)
pressKeyMap.update(functionKeyMap)



grammarCfg = Config("multi edit")
grammarCfg.cmd = Section("Language section")
grammarCfg.cmd.map = Item(
    {
        # Mouse
        # "yep":  Key("c-f9"), mouse click from AutoHotkey script
        "yep": Mouse("left"),
        "yeah": Mouse("left:2"),
        "triple": Mouse("left:3"),
        "middle yep": Mouse("middle"),
        "are yeah": Mouse("right"),
        "drag": Mouse("left:down"),
        "drop": Mouse("left:up"),
        "pointer": Key("f11"), # enables pointer control in enable viacam

        # temporary fixes for vscode scrolling
        "roll up [<n>]": Key("c-up:%(n)d"),
        "roll down [<n>]": Key("c-down:%(n)d"),
        "rowley": Key("c-down:20"),
        "rosey" : Key("c-up:20"),

        # Navigation keys.
        "sauce [<n>]": Key("up:%(n)d"),
        "dunce [<n>]": Key("down:%(n)d"),
        "left [<n>]": Key("left:%(n)d"),
        "right [<n>]": Key("right:%(n)d"),
        "(page up|moss) [<n>]": Key("pgup:%(n)d"),
        "(lis|page down) [<n>]": Key("pgdown:%(n)d"),
        "undo [<n>]": Key("c-z:%(n)d"),
        "redo [<n>]": Key("c-y:%(n)d"),
        "file save": Key("c-s"),
        #"up <n> (page|pages)": Key("pgup:%(n)d"),
        #"down <n> (page|pages)": Key("pgdown:%(n)d"),
        #"left <n> (word|words)": Key("c-left/3:%(n)d/10"),
        #"right <n> (word|words)": Key("c-right/3:%(n)d/10"),
        "(homer|home)": Key("home"),
        "(sequel|end)": Key("end"),
        "(topper)": Key("c-home/3"),
        "(bottom)": Key("c-end/3"),
        # Functional keys.
        "space": release + Key("space"),
        "space [<n>]": release + Key("space:%(n)d"),
        "enter [<n>]": release + Key("enter:%(n)d"),
        "tab [<n>]": Key("tab:%(n)d"),
        "delete [<n>]": Key("del/3:%(n)d"),
        "delete [this] line": Key("home, s-end, del"),  # @IgnorePep8
        "backs [<n>]": release + Key("backspace:%(n)d"),
        "application key": release + Key("apps/3"),

        # Window Switching
        # I use numbered win keys for window switching with the following
        # modifications to the taskbar in Windows 10:
        #     1. From windows settings app: Uncombined taskbar buttons
        #     2. From windows settings app: Vertical taskbar on the right side
        #     3. From windows settings app: Small taskbar buttons
        #     4. Windhawk mod: "Disable grouping on the taskbar". This prevents
        #        the thumbnail preview pop up when you press a windows key plus
        #        a number
        #     5. Taskbar size minimized using drag-to-resize

        # Win key switching with numbers
        "win key": release + Key("win/3"),
        "switch one": release + Key("w-1/3"),
        "switch two": release + Key("w-2/3"),
        "switch three": release + Key("w-3/3"),
        "switch four": release + Key("w-4/3"),
        "switch five": release + Key("w-5/3"),
        "switch six": release + Key("w-6/3"),
        "switch seven": release + Key("w-7/3"),
        "switch eight": release + Key("w-8/3"),
        "switch nine": release + Key("w-9/3"),
        # Negative numbered win keys
        # Allows switching by counting from the end of the taskbar buttons.
        "switch minus [one]": release + Key("w-b/3, s-tab/3, end, enter"),
        "switch minus two": release + Key("w-b/3, s-tab/3, end, up, enter"),
        "switch minus three": release + Key("w-b/3, s-tab/3, end, up:2, enter"),
        "switch minus four": release + Key("w-b/3, s-tab/3, end, up:3, enter"),
        "switch minus five": release + Key("w-b/3, s-tab/3, end, up:4, enter"),
        "switch minus six": release + Key("w-b/3, s-tab/3, end, up:5, enter"),
        "switch minus seven": release + Key("w-b/3, s-tab/3, end, up:6, enter"),
        "switch minus eight": release + Key("w-b/3, s-tab/3, end, up:7, enter"),

        "win left": release + Key("w-left/3"),
        "win right": release + Key("w-right/3"),
        "win up": release + Key("w-up/3"),
        "win down": release + Key("w-down/3"),

        "language input": Key("w-space"),
        "(system tray|sys tray)": release + Key("w-b/3"),
        "switchback": release + Key("a-tab/3"),
        "context menu": Key("s-f10"),

        # Window resizing
        "resize [from] bottom": release + Key("a-space/5, s, down"),
        "resize [from] top": release + Key("a-space/5, s, up"),
        "resize [from] left": release + Key("a-space/5, s, left"),
        "resize [from] right": release + Key("a-space/5, s, right"),

        "force close": release + Key("a-f4/3"),

        # Visual studio code
        "pane increase [<n>]": release + Key("cs-i/3:%(n)d"),
        "pane decrease [<n>]": release + Key("cs-o/3:%(n)d"),
        "show preview": Key("c-k/3, v"),
        "show files": Key("cs-e"),
        "hide left": Key("c-b"),
        "commander": Key("cs-p"),
        "move panel right": Key("cs-9"),
        "move panel bottom": Key("cs-3"),
        "keyboard shortcuts": Key("c-k/3, c-s"),
        "clarify": Key("c-k/3, c-i"),
        "(focus terminal|shell)": Key("c-backtick"),

        "flash": Key("f2"),
        "focus": Key("f6"),
        # "paste [that]": Function(paste_command),
        # "copy [that]": Function(copy_command),
        "cut [that]": release + Key("c-x/3"),
        "copy [that]": release + Key("c-c/3"),
        "paste [that]": release + Key("c-v/3"),
        "select all": release + Key("c-a/3"),
        "[(hold|press)] alt": Key("alt:down/3"),
        "[(hold|press)] angry": Key("alt:down/3"),
        "release alt": Key("alt:up"),
        "[(hold|press)] shift": Key("shift:down/3"),
        "release shift": Key("shift:up"),
        "[(hold|press)] control": Key("ctrl:down/3"),
        "release control": Key("ctrl:up"),
        "release [all]": release,
        "press [key] <pressKey>": Key("%(pressKey)s"),
        # Closures.
        #"angle brackets": Key("langle, rangle, left/3"),
        #"[square] brackets": Key("lbracket, rbracket, left/3"),
        #"[curly] braces": Key("lbrace, rbrace, left/3"),
        #"(parens|parentheses)": Key("lparen, rparen, left/3"),
        #"quotes": Key("dquote/3, dquote/3, left/3"),
        #"backticks": Key("backtick:2, left"),
        #"single quotes": Key("squote, squote, left/3"),
        "tilde": Text("~"),
        "(backquote|backtick)": Key("backtick"),
        # Shorthand multiple characters.
        "double <char>": Text("%(char)s%(char)s"),
        "triple <char>": Text("%(char)s%(char)s%(char)s"),
        "double escape": Key("escape, escape"),  # Exiting menus.
        # Punctuation and separation characters, for quick editing.
        "colon [<n>]": Key("colon/2:%(n)d"),
        "(semicolon|semi colon) [<n>]": Key("semicolon/2:%(n)d"),
        "comma [<n>]": Key("comma/2:%(n)d"),
        #"(dot|period|dit|point)": Key("dot"),  # cannot be followed by a repeat count
        "(period|point)": Key("dot"),  # cannot be followed by a repeat count
        "(dash|hyphen|minus) [<n>]": Key("hyphen/2:%(n)d"),
        "underscore [<n>]": Key("underscore/2:%(n)d"),
        "<letters>": Text("%(letters)s"),
        "<char>": Text("%(char)s"),
        "<modifierSingle> <letters>": Key("%(modifierSingle)s:down") + Text("%(letters)s") + Key("%(modifierSingle)s:up"),
        "<modifierSingle> <char>": Key("%(modifierSingle)s:down") + Text("%(char)s") + Key("%(modifierSingle)s:up"),

        'langle [<n>]': Key('langle:%(n)d'),
        'lace [<n>]':   Key('lbrace:%(n)d'),
        '(lack|lair) [<n>]':   Key('lbracket:%(n)d'),
        #'(laip|len) [<n>]':   Key('lparen:%(n)d'),
        'len [<n>]':    Key('lparen:%(n)d'),
        'rangle [<n>]': Key('rangle:%(n)d'),
        'race [<n>]':   Key('rbrace:%(n)d'),
        '(rack|rare) [<n>]':   Key('rbracket:%(n)d'),
        #'(raip|ren|wren) [<n>]':   Key('rparen:%(n)d'),
        '(ren|wren) [<n>]':   Key('rparen:%(n)d'),

        "cancel [<n>]": Key("escape:%(n)d"),
        # "act [<n>]": Key("escape:%(n)d"),
        "calm [<n>]": Key("comma:%(n)d"),
        'tunnel': Key('space,bar,space'),
        # 'care':        Key('home'),
        # '(doll|dole)': Key('end'),
        'chuck [<n>]':       Key('del:%(n)d'),
        # 'scratch [<n>]':     Key('backspace:%(n)d'),
        #"visual": Key("v"),
        "visual line": Key("s-v"),
        "visual block": Key("c-v"),
        "doc save": Key("c-s"),
        "arrow": Text("->"),

        # 'gope [<n>]':  Key('pgup:%(n)d'),
        # 'drop [<n>]':  Key('pgdown:%(n)d'),

        # 'lope [<n>]':  Key('c-left:%(n)d'),
        'blush [<n>]': Key('c-left:%(n)d'),
        # '(yope|rope) [<n>]':  Key('c-right:%(n)d'),
        'jump [<n>]': Key('c-right:%(n)d'),
        #'(hill scratch|hatch) [<n>]': Key('c-backspace:%(n)d'),
        'scratch [<n>]': Key('c-backspace:%(n)d'),
        'dear [<n>]': Key('c-delete:%(n)d'),


        'hexadecimal': Text("0x"),
        'suspend': Key('c-z'),

        'word <text>': Function(handle_word),
        'number <num>': Text("%(num)d"),
        'change <text> to <text2>': Key("home, slash") + Text("%(text)s") + Key("enter, c, e") + Text("%(text2)s") + Key("escape"),

        # Microphone sleep/cancel started dictation.
        "[<text>] (go to sleep|cancel and sleep) [<text2>]": Function(cancel_and_sleep),  # @IgnorePep8
    },
    namespace={
        "Key": Key,
        "Text": Text,
    }
)


class KeystrokeRule(MappingRule):
    exported = False
    mapping = grammarCfg.cmd.map
    extras = [
        IntegerRef("n", 1, 100),
        IntegerRef("num", 0, 1000000),
        Dictation("text"),
        Dictation("text2"),
        Choice("char", specialCharMap),
        Choice("letters", letterMap),
        Choice("modifier1", modifierMap),
        Choice("modifier2", modifierMap),
        Choice("modifierSingle", singleModifierMap),
        Choice("pressKey", pressKeyMap),
    ]
    defaults = {
        "n": 1,
    }

