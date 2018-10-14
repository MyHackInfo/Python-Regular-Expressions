'''
     #### Regular Expressions ####
     ->Regular expressions are patterns that specify a matching rule.
     ->Generally contain a mix of text and special characters.
     ->Provides regular expression pattern matching and replacement.

     ## Regular expression pattern rules ##
        text    -Match literal text
        .       -Match any character except newline
        ^       -Match the start of a string(^ kerat-sign)
        $       -Match the end of a string
        *       -Match 0 or more repetitions
        +       -Match 1 or more repetitions
        ?       -Match 0 or 1 repetitions
        *?      -Match 0 or more, few as possible
        +?      -Match 1 or more, few as possible
        {m,n}   -Match m to n repetitions
        {m,n}?  -Match m to n repetitions, few as possible
        [...]   -Match a set of characters(range or "variance",[A-Z])
        [^...]  -Match characters not in set
        A | B   -Match A or B( | bar)
        (...)   -Match regex in parenthesis as a group


      ## Special characters ## (Identifiers:)
      \number   -Matches text matched by previous group
      \A        -Matches start of string
      \b        -Matches empty string at beginning or end of word
      \B        -Matches empty string not at begin or end of word
      \d        -Matches any decimal digit
      \D        -Matches any non-digit
      \s        -Matches any whitespace
      \S        -Matches any non-whitespace
      \w        -Matches any alphanumeric character
      \W        -Matches characters not in \w
      \Z        -Match at end of string.
      \\        -Literal backslash


      ## White Space characters: ##
      \n        -new line
      \s        -space
      \t        -tab
      \e        -escape
      \f        -form feed
      \r        -return


      ## Regular Expressions Objects ##
        re.search('patten','string')                 # Search for a match
        re.match(s [,pos [,endpos]])                 # Check string for match
        re.split(s)                                  # Split on a regex match
        re.findall(s)                                # Find all matches
        re.sub(repl,s)                               # Replace all matches with repl



## What we need

1- import re
2- re.findall( r' here match ', string)             # findall method take two arg(patten,string)




26
'''
