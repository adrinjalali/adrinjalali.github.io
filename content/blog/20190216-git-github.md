Title: GIT/GITHUB, how to contribute to an open source project on GitHub?
Date: 2019-02-16
Tags: open-source
Category: open-source

![git/github](files/img/20190216-git-github.png
"Credit: https://medium.com/cs-note/git-and-github-for-beginners-i-tutorial-263caa01f9c3")

The idea behind this post is not to show how to install the tools you need, or
to list a bunch of [at a first glance seemingly random] `git` commands. There
are enough tutorials and blog posts explaining them out there in the wild that
with a web search you'll find too many of them anyway.

This goal of this post is to give you the ingredients you need to contribute to
a project on the GitHub platform and collaborate with other people there.

The first important point is the distinction between __git__ and __GitHub__!
GitHub is a platform which uses `git`, but it's also not the only platform that
uses it. Another somewhat similar platform is __GitLab__, but there are crucial
differences between the two that has made GitHub a much more convenient place
for a community of strangers to work together. By far the best source of
information I can recommend is the [Pro Git
book](https://git-scm.com/book/en/v2). To keep it practical, I may not strictly
stick to the definitions present in the book; the idea is to get you started
first, then you can cover the concepts more _accurately_ once you have more
time.

`git` is a version control system, which is:

> Version control is a system that records changes to a file or set of files
> over time so that you can recall specific versions later[^f1].

Strictly speaking, to develop a package using `git` there is no need for any
server or a platform. Most `git` related tasks you'd be doing are done
completely locally on your own machine anyway.


The main issue at the beginning when you start to work with `git` is all the
jargon used around it. To get an idea of what we're talking about here, the
[GIT Workflow - Georgia Tech - Software Development
Process](https://www.youtube.com/watch?v=3a2x1iJFJWc) short video is a great
place to start:

[![GIT Workflow - Georgia Tech - Software Development
Process](http://img.youtube.com/vi/3a2x1iJFJWc/0.jpg)](https://www.youtube.com/watch?v=3a2x1iJFJWc
"GIT Workflow - Georgia Tech - Software Development Process")

Now let's go through some of the concepts you'd encounter in
almost any project. For the rest of this post, I'll be assuming you've
installed `git` and gone through [this
tutorial](https://medium.com/cs-note/git-and-github-for-beginners-i-tutorial-263caa01f9c3)
up to Step 3: setup "config".

_Source tree_ is your project's folder, with all its subfolders and files that
are included in the project. Using `git` you'll be keeping track of all the
changes on the source tree.

However, there are always files and folders which you don't want to keep track
of, for instance the `build` directory which keeps compiled binary files of
your project. Cache and temporary files are also another category of files you
would like to exclude from being tracked. The way you tell `git` to ignore
those is through a `.gitignore` file usually put in the root of the project's
folder. For most programming languages, there are descent `.gitignore`
templates, for instance you can take a look at the
[Python.gitignore](https://github.com/github/gitignore/blob/master/Python.gitignore).
This means `git` will not automatically start tracking any of the files and/or
folders mentioned in `.gitignore`, but you can still explicitly tell it to do
so if you wish for a particular file or folder. For instance, you may want to
ignore all `.pdf` files, but keep a single `.pdf` in your repository for some
reason. You would be able to do so by explicitly telling `git` to keep track of
it.

stage

Git workflow

[^f1]: Chacon, Scott, and Ben Straub. Pro git. Apress, 2014.
