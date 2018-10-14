Title: How to find a good open source project for contributions?
Date: 2018-10-13
Tags: open-source
Category: open-source

![Diversity](files/img/foss-diversity.jpg
Credit:https://blog.mapbox.com/our-code-of-conduct-for-open-source-2b3a81c00c80)

When looking for a project to which you'd like to contribute, there are two
major aspects you may want to consider. One is the way it's released and
managed, and the other is the community around it.

The way I see the first aspect, it's like a spectrum. Closed source proprietary
software on one side (let say the right side), and community driven and fully 
transparent and open
sourced project on the other side (let say the left side).
And it's important to realize that different
projects are somewhere on this spectrum, and not necessarily on either of the
two ends; let aside the whole licensing issue which itself complicates matters
by another order of magnitude.

Sometimes companies "release" the source code of a product, or a part of a
product. Microsoft does this pretty often. You can only look at the code; you
can't run it, you can't use it, and most people won't. To me it's more like a
public relations thingy. They use it as a tool to gain reputation among the
community. I see such examples as the ones pretty close the right side of the
spectrum.

Going slightly to the left side of the spectrum, there are projects which are
"released" as a whole, and they may even include a friendly license letting
you use it under certain conditions. They may even have a GitHub account and
dump the source code there. Some of these projects are released once, and never
maintained further, and some go through periodical releases; but they still
keep the public community mostly in dark about the development of the
new features. They usually also don't really welcome contributions from
"outsiders", and that's not because they don't like contributions; it's mostly
due to the fact that they have limited amount of resources and their priorities
are dictated by the products in which these pieces of software are used. I'm not
a big fan of contributing to these projects since a large part of the
conversation about the project happens within the team inside the company,
and external contributors are treated somewhat like a second order citizens to
these projects. I get the feeling that projects such as
[spaCy](https://github.com/explosion/spaCy) or
[tensorflow](https://github.com/tensorflow/tensorflow) are such projects. They
have an extremely slow response rate on community questions. You do get the
feeling that it's a one sided relationship, _i.e._ they release a version,
and if you're lucky, your concerns may have been addressed in the release.

The next group of projects are the ones which are considered as a part of
[free and open source software (FOSS)](https://en.wikipedia.org/wiki/Free_and_open-source_software).
This means not only the software is free and open source, but also volunteers
are encouraged to contribute to it and help it be improved. Naturally, if you'd
like to work on a project as a volunteer, these are good candidates. But even
within this category of projects, not all of them are a friendly place to
contributors. Fortunately, more and more projects are moving towards having
a proper code of conduct ensuring a harassment free environment, and probably
the most high
profile one among the recent ones is the Linux Kernel project, which recently
confronted Linus Trovalds about it and adopted a
[new code of conduct](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=8a104f8b5867c682d994ffa7a74093c54469c11f).
It is important to realize that there's no such thing as the open source
community. The reality is that there are different communities around different
projects/topics. People's attitudes differ from community to community,
programming language to programming language, etc.

My personal experience, which admittedly doesn't necessarily project the
complete picture about any community since it's by definition subjective, has
been the following:

- __C++__ community has always been the harshest in my experience (and I know
  I'm not alone having experienced that). If you ask a question there which
  sounds _stupid_ to the experts in the field, they probably would crush you by
  asking why you haven't read a "proper" book on C++. By that they usually
  mean the whole C++ ISO standard.
- __R__ community was really unpleasant to interact, to the point it encouraged
  me to switch from R to Python (yeah, that is in fact why I became a python
  coder). After creating and maintaining three packages for R in CRAN and
  Bioconductor, I was kinda done with it. I need to mention that this was back
  in 2012, and a lot could have changed in these few years. I have no idea how
  the community behaves these days; and I'd be delighted if I'm completely wrong
  about the community now.
- __Python__ has always been nice as far as I'm concerned. It is a language
  which has it's
  [own code of conduct](https://www.python.org/psf/codeofconduct/). You can
  imagine how that has influenced the whole community around it.

Here are a few things you can consider when checking on a [FOSS] project:

- __Activity__: Is the project under active development? When was the last
  release? How often people open issues and contribute to the project? How often
  do main developers respond to those issues? Many projects may seem pretty cool
  at the first glance, but when you dig deeper, they may be dead projects. Sure
  you can try to revive it, but that may require more dedication and time than
  what you have at hand.
- __Code of Conduct__: The presence of a code of conduct is neither a necessary
  nor a sufficient condition for a healthy atmosphere in a project, but it's a
  sign that the core developers do care about the kind of atmosphere around the
  project. Also, the more people care about codes of conducts, the more pressure
  on the projects to adopt one.
- __Community Contributions__: For larger projects, you can check how open the
  community is, by checking the repository logs. There are many tools to
  visualize activity on repositories, for instance, you can check the activity
  around tensorflow
  [here](http://ghv.artzub.com/#repo=tensorflow&climit=100&user=tensorflow),
  and activity around scikit-learn
  [here](http://ghv.artzub.com/#repo=scikit-learn&climit=100&user=scikit-learn).
  You can easily notice how tensorflow has a special user called
  _tensorflow-gardener_, and you can read about it
  [here](https://www.oreilly.com/ideas/how-the-tensorflow-team-handles-open-source-support).
  I personally prefer repositories which have a larger set of contributors
  publicly contributing to the ones hiding internal development behind a special
  user.
- __Treating Contributors__: It's never pleasant to work with a bunch of snobs!
  As a new contributor, you are bound to make many mistakes, or try things the
  way which is not the common way it's done in the project you're working on.
  This is
  normal and expected as users join a community. It is very important for the
  core developers of that project to know that and treat newcommers nicely
  and encouragingly. You can see if that's the case or not, by going through
  some of the issues and pull requests in the project you're checking. Just
  take your time and read some of the conversations happening around some of
  the issues to make sure it suits your taste. You can also check the "closed"
  issues
  to see how the core developers handle closing issues.

In another post I'll talk about ways you can start contributing to a project
of your choice.
