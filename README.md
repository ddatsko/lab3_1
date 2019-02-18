This python module helps to navigate in a .json file, got
via Twitter API. The example of file is in docs directory.
For moving to different parts of file type the name of location
you'd like to go (list of them is shown) or type ".." to
move one level higher.
e.g.:
___________________________________________________________________
    This program helps to navigate on .json file got via Twitter API
    You can navigate to items marked as "..." by writing
    their names or use ".." to move a level higher
    Enter the file name (.json format) or path to it: ../docs/example.json
____________________________________________________________________
    You are here: root
    users                : ...
    next_cursor          : 1558075440525490518
    next_cursor_str      : 1558075440525490518
    previous_cursor      : 0
    previous_cursor_str  : 0
    total_count          : None
    Where to go now: users
____________________________________________________________________
    You are here: root."users"
    13ReasonsWhy         : ...
    LupusResearch        : ...
    HotelT               : ...
    DBtodomundo          : ...
    KygoMusic            : ...
    Where to go now: ..
____________________________________________________________________
    You are here: root
    users                : ...
    next_cursor          : 1558075440525490518
    next_cursor_str      : 1558075440525490518
    previous_cursor      : 0
    previous_cursor_str  : 0
    total_count          : None
    Where to go now: ..
____________________________________________________________________
(end)
