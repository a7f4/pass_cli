# pass-cli:  CLI interface for [pass](https://www.passwordstore.org/).
|           |                                             |
|-----------|---------------------------------------------|
| Info      | This is the README file for pass-cli.       |
| Author    | Aleksandr Block <aleksandr.block@gmail.com> |
| Copyright | © 2019, Aleksandr Block.                    |
| Date      | 2019-08-23                                  |
| Version   | 0.0.2                                       |



Inspired by [upass](https://github.com/Kwpolska/upass)

Pre-requirements
----------------
* Make sure that you've installed [pass](https://www.passwordstore.org/).
* **PASSWORD_STORE** - path to a password store (optional env variable)
* **EDITOR** - editor (`emacs` | `vim` | `nano` | etc.)

Installation
------------
    $ python3 -m pip install pass_cli
    
Key-bindings
------------
* `q` quit
* `e` edit entry
* `r` refresh
* `b` back
* `:s <part of pass entry>` + `enter` - to search pass-entries
* `:q` + `enter` - quit
* `enter` [on pass entries] - load a pass-entry
* `enter` [on content of pass-entry] - copy to clipboard

