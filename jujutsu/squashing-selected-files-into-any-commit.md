# Squashing Selected Files Into Any Commit

 Suppose you have files in your working copy that you want to move to a different commit. `jj` makes this easy using the squash command (rather than creating a new commit). 
 
   As an example, for my blog I keep a separate bookmark a.k.a. branch in Git where I keep all my drafts. Sometimes when I start with a new post, I end up with the post I am writing but also with a draft I started earlier and forgot to move to my dedicated drafts bookmark (`content/roadmap`). In this case I want to move the draft I started previously to my drafts bookmark. I can then continue working in the working copy for the new post.
 
 This is what it would look like:
 
 My working copy contains two files. I only want to publish the first one (`post-a.md`). The other one (`post-b.md`), is the file I want to move to a different commit.
 ```bash
 ❯ jj st --no-pager
 Working copy changes:
 A content/p/post-a.md
 M content/p/post-b.md
 Working copy  (@) : nztmnszt 4083a246 (no description set)
 Parent commit (@-): yqznnpzw d913752f main | feat(post): The best technical decision of 2025: moving to Proton
 ```
 
 This is what the history looks like. Note the `DRAFTS` commit with the `content/roadmap` bookmark and its change id: `wwsoonkl`.
 ```bash
 ❯ jj log ...
 @  nztmnszt (no description set) 13 minutes ago
 ◆  yqznnpzw feat(post): The best technical decision of 2025: moving to Proton main git_head() 2 weeks ago
 ...
 │ ○  wwsoonkl DRAFTS content/roadmap 3 weeks ago
 ├─╯
 ◆  oqzqknpm feat(post): TIL rules to remember 3 weeks ago
 ```

To squash the file into the commit, you can just mention the file or files directly in the `squash` command. 

Using the bookmark:
```bash
❯ jj squash --into content/roadmap post-b.md
```

Instead of the bookmark you can also put the change id `wwsoonkl`.

```bash
❯ jj squash --into wwsoonkl post-b.md
```

The status of the repository after this change is:

```bash
❯ jj st --no-pager
Working copy changes:
A content/p/post-a.md
Working copy  (@) : nztmnszt 4b00ff51 (no description set)
```

```bash
❯ jj show --summary content/roadmap --no-pager
Commit ID: 7a429f116457c8fc4da472a5afbe8720c590503c
Change ID: wwsoonklrykzysxtsnrpswrprkmmukrm
Bookmarks: content/roadmap* content/roadmap@git

    DRAFTS

M content/p/post-b.md
...
```

_Created: 2026-01-13_
