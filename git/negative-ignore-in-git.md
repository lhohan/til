# Negative Ignore In Git

Usually, when working with Git, I ignore files by adding them to the .gitignore file. Turns out you can also do the opposite. You can ignore all files _except_ the ones you specify. 

Here is an example of a .gitignore file that ignores all content in a directory except files with a certain extension and the .gitignore file itself:

```
*
!*.dsl
!.gitignore
```

_Created: 2026-03-05_
