1. Started in Perplexity (on my ipad) to come up with a basic prompt, here are my questions:
    - "How does a til repo like this work: https://github.com/simonw/til"
    - "Details on how it becomes a website please. Also, the readme , is that manual update?"
    - "Could i use zola static site gen for this?"
        - Zola because I use it already and it looked to me I do not need the unfamilar stuff to me the author of the repo is using
    - "Can I deploy til repo -> zola site -> hetzner vps?"
        - I run my static sites om a Hetzner server
    - "__Create a llm prompt to create a til repo structure, zola setup to generate a site and deploy from gh action to hetzner vps__"
    - (Then I could not get it to give me a downloadedable markdown file which was kind of unfortunate because the web site did not allow a clean copy of the full answer, eventually I copy pasted 10 texts manually ...)
3. Optimize using ChatGpt optimizer
  - Just to make it better with role and reviewing it a bit more
4. Gave prompt to Claude Code Web first, empty repo was maybe confusing so I I started again
5. Droid + Claude Opus 4.5 with a slightly modified prompt I saved to the root of the project
6. I asked to come up with a plan before implementing
7. During implementation:
    a. found initial instruction to use elasticlunr.js to be wrong, it is abandoned, asked Opus feedback, gave 3 option, chose the option to rely on basic built-in navigational search in Zola and asked to write a task to the backlog with the option to use a more modern alternative (Pagefind, will research this more when I get to the actual task)
    b. it tried to install Zola
