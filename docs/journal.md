# Project Journal
This is the journal I wrote while completing the project. It is structured in some way, but not nearly as much as a blog post or an actual report would be. In contrast the mentioned other formats, this journal is written in small chunks for me to document my thought processes, decisions and progress. It is not to be interpreted as a polished document for presentation. For such a document, please see the blog or a report.

## Set Up the Repo

### General
I set up the repo so that it is public, I am the only contributor, main branch is protected, but I can (due to being the only contributor) merge without approval. I set up a personal access token for my local machine. I will work in feature branches. This, for example, is done in the "documentation" branch.

#### Update January 2024
The idea of strictly working in feature branches and merging afterwards proved impractical for this stage of this kind of solo project. I am currently still in a phase in which progress is very linear and where there are obvious tasks. I think of a general idea, structure and get the data, then explore it. Even afterwards, steps are already more or less clear. I will fit a model and evaluate it. I don't currently think I will deploy the model of this project somewhere. This is rather a data analysis project. I will more likely move on to the next project and once I develop anything with an actual functionality, then deploy that one. Anyway, working in branches was a little annoying here. In general, I love the idea. When working on experimental or fundamental features of the project, you are basically safe from messing it all up. Also, branches are absolutely crucial when working in teams. But in my case, as described before, none of this is the case. Because of that, I will just push directly into main for now. Even if I think that might not be best practice in every situation, it is equally important to make use of strategies that best benefit your current situation. If I still develop larger features, I will definitely get back to working in feature branches.

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
2. I am currently still learning. This is an exercise project for me and it is the first time I stick to this specific directory structure. Having a README.md in every directory allows for a maximum level of readability. Also for someone having a look at my project, this is going to prove very helpful to get an overview.
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

It would also have been cool to implement the entire directory structure using a shell script. However, I am not yet sure if I even need all of it and it is basically just a few lines of commands. Can still do it in the future if this structure proved to be helpful.

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

Main onjective right now: Frame the plan. I need to find an interesting research question or project idea to solve and with it a data set allowing to do so. I could also go the other way round and look for data sets, then see what I can do with them. I want to do data cleaning, visualisations, predictive modelling using Scikit-learn and properly evaluating different models. These are actually already the milestones. I want to pay attention to best practices and showcase my ability to do data science as well as project planning, documentation and (in this project only possible to a certain degree, because here I do not actually build anything) software development.

Jan 15, 2024: I decided to use a dataset about heart failure. I think it is very interesting, because it fits my background in biomedical research. It is also highly relevant, because cardiovascular diseases are the most common cause of death world wide. While this is just an exercise and will not harbor any new results, it fits my resumee and might help raising awareness for this terrible issue.

## Data Acquisition
I decided to use Kaggle's API via the command line to download the data instead of the GUI on its website. This saves several steps of moving files and allows for great potential of automation (for example in future projects).

Jan 12, 2024: After focusing on other projects, I picked up work on this again today. I selected a data set about heart failure and adapted the data acquisition notebook and framed the idea. Since there has been a break now, I also include the date. I can still remove the date from this journal. Anyway, the data is now downloaded and the decision about the specific data set, projects objective and scope has finally been made. I save all data downloaded data in the `data/raw` directory and treat it as immutable. This means I will always keep an unchanged copy of the original. I will derive processed versions of it, but they will be saved in addition to the original instead of replacing it. In this project, all data will be ignored by Git.

This is the dataset I decided to use:

Davide Chicco, Giuseppe Jurman: Machine learning can predict survival of patients with heart failure from serum creatinine and ejection fraction alone. BMC Medical Informatics and Decision Making 20, 16 (2020).

It is distributed under a CC BY 4.0 license. Attribution is made above. I will not change the original dataset, as described above, but derive processed versions of it, and finally use it for predictive modeling.

https://www.kaggle.com/datasets/andrewmvd/heart-failure-clinical-data

The dataset is very well documented and has a lot of nice features that can be used for predictive modeling.

## Exploratory Data Analysis (EDA)
January 15, 2024: Today, I start the EDA.


