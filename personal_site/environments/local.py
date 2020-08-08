
## Wagtail
INSTALLED_APPS = INSTALLED_APPS + [
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',

    'modelcluster',
    'taggit',]

MIDDLEWARE = MIDDLEWARE + ['wagtail.contrib.redirects.middleware.RedirectMiddleware',]

WAGTAIL_SITE_NAME = 'Personal Website'
WAGTAILEMBEDS_RESPONSIVE_HTML = True

## wagtail-metadata

INSTALLED_APPS = INSTALLED_APPS + [
    'wagtailmetadata',
]

## wagtail-blocks
INSTALLED_APPS = INSTALLED_APPS +[
    'wagtailfontawesome',
    'wagtail_blocks',
]

##django-tz-detect
INSTALLED_APPS = INSTALLED_APPS +[
        'tz_detect',
]

MIDDLEWARE = MIDDLEWARE + ['tz_detect.middleware.TimezoneMiddleware',]

## wagtail code block
INSTALLED_APPS = INSTALLED_APPS + ['wagtailcodeblock',]
WAGTAIL_CODE_BLOCK_THEME = 'twilight'
WAGTAIL_CODE_BLOCK_LANGUAGES = (
    ('abap', 'ABAP'),
    ('abnf', 'Augmented Backus–Naur form'),
    ('actionscript', 'ActionScript'),
    ('ada', 'Ada'),
    ('antlr4', 'ANTLR4'),
    ('apacheconf', 'Apache Configuration'),
    ('apl', 'APL'),
    ('applescript', 'AppleScript'),
    ('aql', 'AQL'),
    ('arduino', 'Arduino'),
    ('arff', 'ARFF'),
    ('asciidoc', 'AsciiDoc'),
    ('asm6502', '6502 Assembly'),
    ('aspnet', 'ASP.NET (C#)'),
    ('autohotkey', 'AutoHotkey'),
    ('autoit', 'AutoIt'),
    ('bash', 'Bash + Shell'),
    ('basic', 'BASIC'),
    ('batch', 'Batch'),
    ('bison', 'Bison'),
    ('bnf', 'Backus–Naur form + Routing Backus–Naur form'),
    ('brainfuck', 'Brainfuck'),
    ('bro', 'Bro'),
    ('c', 'C'),
    ('clike', 'C-like'),
    ('cmake', 'CMake'),
    ('csharp', 'C#'),
    ('cpp', 'C++'),
    ('cil', 'CIL'),
    ('coffeescript', 'CoffeeScript'),
    ('clojure', 'Clojure'),
    ('crystal', 'Crystal'),
    ('csp', 'Content-Security-Policy'),
    ('css', 'CSS'),
    ('css-extras', 'CSS Extras'),
    ('d', 'D'),
    ('dart', 'Dart'),
    ('diff', 'Diff'),
    ('django', 'Django/Jinja2'),
    ('dns-zone-file', 'DNS Zone File'),
    ('docker', 'Docker'),
    ('ebnf', 'Extended Backus–Naur form'),
    ('eiffel', 'Eiffel'),
    ('ejs', 'EJS'),
    ('elixir', 'Elixir'),
    ('elm', 'Elm'),
    ('erb', 'ERB'),
    ('erlang', 'Erlang'),
    ('etlua', 'Embedded LUA Templating'),
    ('fsharp', 'F#'),
    ('flow', 'Flow'),
    ('fortran', 'Fortran'),
    ('ftl', 'Freemarker Template Language'),
    ('gcode', 'G-code'),
    ('gdscript', 'GDScript'),
    ('gedcom', 'GEDCOM'),
    ('gherkin', 'Gherkin'),
    ('git', 'Git'),
    ('glsl', 'GLSL'),
    ('gml', 'GameMaker Language'),
    ('go', 'Go'),
    ('graphql', 'GraphQL'),
    ('groovy', 'Groovy'),
    ('haml', 'Haml'),
    ('handlebars', 'Handlebars'),
    ('haskell', 'Haskell'),
    ('haxe', 'Haxe'),
    ('hcl', 'HCL'),
    ('http', 'HTTP'),
    ('hpkp', 'HTTP Public-Key-Pins'),
    ('hsts', 'HTTP Strict-Transport-Security'),
    ('ichigojam', 'IchigoJam'),
    ('icon', 'Icon'),
    ('inform7', 'Inform 7'),
    ('ini', 'Ini'),
    ('io', 'Io'),
    ('j', 'J'),
    ('java', 'Java'),
    ('javadoc', 'JavaDoc'),
    ('javadoclike', 'JavaDoc-like'),
    ('javascript', 'JavaScript'),
    ('javastacktrace', 'Java stack trace'),
    ('jolie', 'Jolie'),
    ('jq', 'JQ'),
    ('jsdoc', 'JSDoc'),
    ('js-extras', 'JS Extras'),
    ('js-templates', 'JS Templates'),
    ('json', 'JSON'),
    ('jsonp', 'JSONP'),
    ('json5', 'JSON5'),
    ('julia', 'Julia'),
    ('keyman', 'Keyman'),
    ('kotlin', 'Kotlin'),
    ('latex', 'LaTeX'),
    ('less', 'Less'),
    ('lilypond', 'Lilypond'),
    ('liquid', 'Liquid'),
    ('lisp', 'Lisp'),
    ('livescript', 'LiveScript'),
    ('lolcode', 'LOLCODE'),
    ('lua', 'Lua'),
    ('makefile', 'Makefile'),
    ('markdown', 'Markdown'),
    ('markup', 'Markup + HTML + XML + SVG + MathML'),
    ('markup-templating', 'Markup templating'),
    ('matlab', 'MATLAB'),
    ('mel', 'MEL'),
    ('mizar', 'Mizar'),
    ('monkey', 'Monkey'),
    ('n1ql', 'N1QL'),
    ('n4js', 'N4JS'),
    ('nand2tetris-hdl', 'Nand To Tetris HDL'),
    ('nasm', 'NASM'),
    ('nginx', 'nginx'),
    ('nim', 'Nim'),
    ('nix', 'Nix'),
    ('nsis', 'NSIS'),
    ('objectivec', 'Objective-C'),
    ('ocaml', 'OCaml'),
    ('opencl', 'OpenCL'),
    ('oz', 'Oz'),
    ('parigp', 'PARI/GP'),
    ('parser', 'Parser'),
    ('pascal', 'Pascal + Object Pascal'),
    ('pascaligo', 'Pascaligo'),
    ('pcaxis', 'PC Axis'),
    ('perl', 'Perl'),
    ('php', 'PHP'),
    ('phpdoc', 'PHPDoc'),
    ('php-extras', 'PHP Extras'),
    ('plsql', 'PL/SQL'),
    ('powershell', 'PowerShell'),
    ('processing', 'Processing'),
    ('prolog', 'Prolog'),
    ('properties', '.properties'),
    ('protobuf', 'Protocol Buffers'),
    ('pug', 'Pug'),
    ('puppet', 'Puppet'),
    ('pure', 'Pure'),
    ('python', 'Python'),
    ('q', 'Q (kdb+ database)'),
    ('qore', 'Qore'),
    ('r', 'R'),
    ('jsx', 'React JSX'),
    ('tsx', 'React TSX'),
    ('renpy', 'Ren\'py'),
    ('reason', 'Reason'),
    ('regex', 'Regex'),
    ('rest', 'reST (reStructuredText)'),
    ('rip', 'Rip'),
    ('roboconf', 'Roboconf'),
    ('robot-framework', 'Robot Framework'),
    ('ruby', 'Ruby'),
    ('rust', 'Rust'),
    ('sas', 'SAS'),
    ('sass', 'Sass (Sass)'),
    ('scss', 'Sass (Scss)'),
    ('scala', 'Scala'),
    ('scheme', 'Scheme'),
    ('shell-session', 'Shell Session'),
    ('smalltalk', 'Smalltalk'),
    ('smarty', 'Smarty'),
    ('solidity', 'Solidity (Ethereum)'),
    ('sparql', 'SPARQL'),
    ('splunk-spl', 'Splunk SPL'),
    ('sqf', 'SQF: Status Quo Function (Arma 3)'),
    ('sql', 'SQL'),
    ('soy', 'Soy (Closure Template)'),
    ('stylus', 'Stylus'),
    ('swift', 'Swift'),
    ('tap', 'TAP'),
    ('tcl', 'Tcl'),
    ('textile', 'Textile'),
    ('toml', 'TOML'),
    ('tt2', 'Template Toolkit 2'),
    ('twig', 'Twig'),
    ('typescript', 'TypeScript'),
    ('t4-cs', 'T4 Text Templates (C#)'),
    ('t4-vb', 'T4 Text Templates (VB)'),
    ('t4-templating', 'T4 templating'),
    ('vala', 'Vala'),
    ('vbnet', 'VB.Net'),
    ('velocity', 'Velocity'),
    ('verilog', 'Verilog'),
    ('vhdl', 'VHDL'),
    ('vim', 'vim'),
    ('visual-basic', 'Visual Basic'),
    ('wasm', 'WebAssembly'),
    ('wiki', 'Wiki markup'),
    ('xeora', 'Xeora + XeoraCube'),
    ('xojo', 'Xojo (REALbasic)'),
    ('xquery', 'XQuery'),
    ('yaml', 'YAML'),
    ('zig', 'Zig'),
)

## django-taggit-template-tags2
INSTALLED_APPS += ['taggit_templatetags2']

## custom apps

INSTALLED_APPS += ['website']
TEMPLATES[0]["OPTIONS"]["context_processors"] += ["website.template_processors.debug_mode_processor.debug_mode_processor"]

# font awesome
INSTALLED_APPS += ['fontawesome_5',]

# sitemap
INSTALLED_APPS += ['django.contrib.sitemaps','wagtail.contrib.modeladmin','robots']


# API
INSTALLED_APPS += ['wagtail.api.v2','rest_framework']



## x-frame-options
# allow embeding own content on site
X_FRAME_OPTIONS = 'SAMEORIGIN'
