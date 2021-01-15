# rez-kitt

For testing release vcs plugin "kit".

The vcs plugin "kit", is an extended git releasing plugin. It will only work on the most recent commit that modified the current releasing package, if it found a file named `.kit` in package root dir. Which allows you to release package from a multi-package git repository (like this one), without mixing other package's commit in current releasing package's changelog.
