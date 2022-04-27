import re

    # markdown formatting is as follows: 
    # **bold**
    # *italics*

    # we need to figure out how to do this:
    # **bold** -> [b]bold[/b]
    # *italics* -> [i]italics[/i]

    # candidate is a string

    # the following needs tinkering to deal with edge cases

    # '/(\*\*|__)(.*?)\1/' => '[b]\2[/b]',            // bold
    # '/(\*|_)(.*?)\1/' => '[i]\2[/i]',                       // emphasis

def process_bold(candidate):
    # return re.sub('(\*\*|__)(.*?)\1', '[b]\2[/b]', candidate, 2)
    return re.sub('\*\*(.*)\*\*', '[b]\g<1>[/b]', candidate)

def process_italics(candidate):
    return re.sub('(\*|_)(.*?)\1', '[i]\g<1>[/i]', candidate, 2)

def process_links(candidate):
    return re.sub('\[([^\[]+)\]\(([^\)]+)\)', 'link test')

    # the following is taken from Slimdown, but it needs further editing as some of these don't work yet

    # '/(#+)(.*)/' => 'bigger font',                           // headers
    # '/\[([^\[]+)\]\(([^\)]+)\)/' => 'link in kivy?',  // links
    # '/\~\~(.*?)\~\~/' => '<del>\1</del>',                     // del
    # '/\:\"(.*?)\"\:/' => '<q>\1</q>',                         // quote
    # '/`(.*?)`/' => '<code>\1</code>',                         // inline code
    # '/\n\*(.*)/' => 'self::ul_list',                          // ul lists
    # '/\n[0-9]+\.(.*)/' => 'self::ol_list',                    // ol lists
    # '/\n(&gt;|\>)(.*)/' => 'self::blockquote ',               // blockquotes
    # '/\n-{5,}/' => "\n<hr />",                                // horizontal rule

# testing 

candidate = "this should be **bold** and also **this** too but not *this*."
candidate2 = "this should be *italics*"
candidate3 = "this is a [link](https://example.com)"

print(process_bold(candidate))
