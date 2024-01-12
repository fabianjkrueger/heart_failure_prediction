# Project Journal
This is the journal I wrote while completing the project. It is structured in some way, but not nearly as much as a blog post or an actual report would be. In contrast the mentioned other formats, this journal is written in small chunks for me to document my thought processes, decisions and progress. It is not to be interpreted as a polished document for presentation. For such a document, please see the blog or a report.

## Set Up the Repo

### General
I set up the repo so that it is public, I am the only contributor, main branch is protected, but I can (due to being the only contributor) merge without approval. I set up a personal access token for my local machine. I will work in feature branches. This, for example, is done in the "documentation" branch.

### Directory Structure
#### Thought Process
In past projects, I had suboptimal directory structures. While I improved over the time, I still think there is a lot of room for improvements. I finally want to move to best practices and adapt a standardized and generic approach that is logical and easy to understand for others. I found two very reasonable approaches that resemble another strongly. 

1. Use Cookie Cutter. This automatically set up a directory structure for you that fulfills all criteria mentioned above and more. This is a well thought through function and the structure is great. However, I will not use it for this project. Since this is the first time I will use standardize directories like src, docs, notebooks etc., I want to set them up manually to get a better understanding of why they are used. Furthermore, I feel like Cookie Cutter could be slightly overkill for my first project. I will not need all of its directories. It is even one of Cookie Cutter's own philosophies to adapt details to needs while keeping the general structure.
2. Set it up yourself, but stickt to established structures. There are some great resources out there, including the Cookie Cutter docs and many others, that explain all directories and how to set up a logical structure. They usually slightly differ from another. However, that is fine, because while sticking to the general framework, it is crucial to adapt the details to the current situation.

Conclusion: I will set up the directory structure manually this time and hope to use Cookie Cutter in my next or one of my future projects. However, I will incorporate many of Cookie Cutter's directories/elements.

#### Implementation
I make a `src` directory by combining Cookie Cutter's `src` and ericmjl's `projectname` directories.

Git will not push empty directories. Most likely usually it is better like that. Also, usually you do not add a README.md to every subdirectory. I will still do it here. There are several reasons for this:

1. I want all the subdirectories to be in GitHub right away, since the main point of this step is to implement the directory structure. If they cannot be pushed, what is the point? I want to be able to access the project from anywhere! Adding a README.md allows me to push.
2. This is the first time I stick to this specific directory structure. Having a README.md in every directory allows for a maximum level of readability. Also for someone having a look at my project, this is going to prove very helpful to get an overview.
3. It just does not hurt to have it, even though it is not usual. If it turns out that it does hurt in some specific directory, I will remove it. In the end, I will also remove all the empty ones.

I made a lot of directories now and most have subdirectories themselves. I will use the Shell to add the all the README.md like this.

```zsh
# work in the project's base directory
# get overview about sub directories
$ ls
> README.md		data			docs			models			notebooks		requirements.txt	scripts			setup.py		src

# copy the base directories README.md to each sub directory recursively
# so far the README.md is still empty, so I do not need to use another empty file
# find . -type d: find all directories and sub directories recursively
#-not -path '*/.git': there are git directories as well. do not mess with them, exclude them from this
# -exec cp README.md '{}' \; copy the README.md to all found directories
$ find . -type d -not -path '*/.git' -exec cp README.md '{}' \;
```

#### Main Resources for Directory Structure
While there are a lot of resources out there, I decided to use these two, since for me they seem to make the most sense. I combine them and make some adjustments.

- Cookie Cutter: http://drivendata.github.io/cookiecutter-data-science/
- How to organize your Python data science project by ericmjl: https://gist.github.com/ericmjl/27e50331f24db3e8f957d1fe7bbbe510

#### Idea for the future: ShellScripting
Right now, I still need to read a lot and based on this, decide which directories exactly I am going to use. In future projects, I hope, I can either just use Cookie Cutter or perhaps if I decided what my needs are, I can write a Shell script that sets up the directory structure for me. This would be super handy, because I could re-run it and it would allow for significantly better documentation. This time, due to planning while doing, this is not preferable though.

### Virtual Environment and Packages
I try to set up a virtual environemt using this workflow:

1. Run mkvirtualenv when creating a new project
2. pip install the packages that your analysis needs
3. Run pip freeze > requirements.txt to pin the exact package versions used to recreate the analysis
4. If you find you need to install another package, run pip freeze > requirements.txt again and commit the changes to version control.

Using something like Docker would be overkill right now. I can try this in a later and larger project.

### License
This is a small project for showcasing some data analysis. It is unlikely that someone will build on it, because most likely I will not produce an application or production code. Nonetheless, I want it to be open source, so that if people want to use it, they can. Also, I want protection against liability. I do not want virality. This mostly rules out Copyleft and Public Domain. Creative Commons is not nessessarily even open source. For this project, the best options are MIT, BSD, and Apache. They are all pretty similar. After comparison, I found that the MIT license is sufficient for the scope of this project. It fulfills all my needs and does not make things overly complicated for others to use. Under it, the code in this repository is open source by the definition of the open source initiative (OSI) can be modified, distributed, sublicensed, used privately and commercially, but I cannot be held liable.

## Ideation
Now I begin to ideate milestones and a general plan with stages. I set the stages/milestones as issues. Not complete or comprehensive right now, since the project is going to evolve.

Main onjective right now: Frame the plan. I need to find an interesting research question or project idea to solve and with it a data set allowing to do so. I could also go the other way round and look for data sets, then see what I can do with them. I want to do data cleaning, visualisations and finally some predictive modelling using Scikit-learn.

## Data Acquisition
I decided to use Kaggle's API via the command line to download the data instead of the GUI on its website. This saves several steps of moving files and allows for great potential of automation (for example in future proj

Jan 12, 2024: After focusing on other projects, I picked up work on this again today. I selected a data set about heart failure and adapted the data acquisition notebook and framed the idea. Since there has been a break now, I also include the date. I can still remove it from this journal. Anyway, the data is now downloaded and the decision about the specific data set, projects objective and scope has finally been made.

