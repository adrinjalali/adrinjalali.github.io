Title: Open Source - CoC - Conflicts
Date: 2020-04-12
Tags: community, open-source
Category: open-source

[![CoC](files/img/code-of-conduct1-min.jpg)](https://www.stalawfirm.com/en/news/view/jordanian-code-of-conduct.html)

(Since I don't know individuals' pronouns involved in this post, _they/them_ is
used instead.)


This post was triggered by three of PyTest maintainers leaving the project in a
single day. That's 3 out of 4-5 active developers of a project which is relied
on by a massive part of the ecosystem to test their projects/software/library.
So it really is a big deal (obviously not as big of a deal as covid19 which is
happening these days ;) ).

The first person to leave was [Bruno
Oliveira](https://mail.python.org/pipermail/pytest-dev/2020-April/004939.html):

> Hi everyone,
> 
> For the past years I've been part of pytest, which is an awesome library
> and also a community with awesome people. It definitely made me a better
> person and better programmer.
> 
> However, the past months or so one individual has drained my will to work
> on the project because of his interactions, so I decided it is best that I
> leave the project for a while and focus on other things.
>
> I of course wish the project and everyone involved the best, and will
> definitely continue to work on my numerous plugins meanwhile.
>
> Stay safe, and cheers!
>
> Bruno

Immediately after [Anthony
Sottile](https://mail.python.org/pipermail/pytest-dev/2020-April/004940.html)
and [Ronny
Pfannschmidt](https://mail.python.org/pipermail/pytest-dev/2020-April/004941.html)
left for a similar reason. It seems there have been discussions in PyTest's CoC
committee which have not come to a satisfying conclusion: judging from the fact
that two of the three developers who have stepped down are/were in PyTest's CoC
(Code of Conduct) team, one of them [removing themself from the
committee](https://github.com/pytest-dev/pytest/pull/6857) and [this
email](https://mail.python.org/pipermail/pytest-dev/2020-April/004945.html) by
Brianna, another member of the CoC team:

> Hi all,
>
> As one of the Code of Conduct (CoC) committee members (
> https://github.com/pytest-dev/pytest/blob/master/CODE_OF_CONDUCT.md ) I
> want to apologise for the poor handling of issues that have led Bruno,
> Anthony and Ronny to step back from the project. As a group we failed to
> act decisively and now people who have contributed so much to pytest are
> suffering, and for that I am sorry.
>
> I intend to reach out to the PSF Conduct Working Group and ask them to
> advise us on a way forward.
>
> thanks,
> Brianna

I'm very curious to see how it unfolds and what the PSF's CoC team thinks about
the issue, but having my CoC related experience (writing them, serving in CoC
committees, dealing with the same issues in other open source projects, etc.),
I don't think there's an easy answer to the issue.

Before talking about potential solutions, we need to understand what has been
happening. It is really important to note that __I'm not a PyTest
developer/maintainer and I'm trying to understand the issue from an outsider's
perspective, and the reason I'm writing this post is that this issue is by far
not unique to PyTest, and as a community we need to be better equipped to deal
with such issues__. 

It seems the individual in question is [Daniel
Hahler](https://github.com/blueyed) who has been very active in PyTest's
development since about [June
2019](https://github.com/pytest-dev/pytest/graphs/contributors?from=2017-04-22&to=2020-04-11&type=c).
Unfortunately, not all interactions with this person have been productive or
pleasant. As an example of an interaction which has frustrated Bruno, [they
have pointed](https://twitter.com/nicoddemus/status/1248946262453424130?s=20)
to [this PR/comment
thread](https://github.com/pytest-dev/pytest/pull/6663#discussion_r375763028),
which I completely agree is a very unpleasant interaction. However, when it
comes to CoC violations, if I were in PyTest's CoC committee, I would have a
hard time deciding whether this single instance warrants banning Danial from
the project or not. Therefore I decided to dig in and see how other
interactions with them look.
[Here](https://github.com/pytest-dev/pytest/pulls?q=is%3Apr+is%3Aopen+involves%3Ablueyed)
you can see the list of PRs where Daniel has been involved either as the author
or as a reviewer. A quick look at the conversations shows that clearly not all
interactions are hostile, but by looking at just the first page, I found these
examples clearly not nice:
[this](https://github.com/pytest-dev/pytest/pull/7029),
[this](https://github.com/pytest-dev/pytest/pull/6934), and [this
one](https://github.com/pytest-dev/pytest/pull/6840). One could argue that some
of the frustrations are miscommunications or cultural differences; but even
then, my judgment is that they are not constructive or respectful, at all.

Now putting all the instances together, it is very clear to me that this person
is creating an unpleasant and disrespectful environment. But does this warrant
Daniel's removal from the team? [Here's PyTest's
CoC](https://github.com/pytest-dev/pytest/blob/master/CODE_OF_CONDUCT.md), and
as examples of expected behavior it states:

> - Being respectful of differing viewpoints and experiences
> - Gracefully accepting constructive criticism

And in the enforcement section, it states:

> Project maintainers who do not follow or enforce the Code of Conduct in good
> faith may face temporary or permanent repercussions as determined by other
> members of the project's leadership.

Now this seems like a very clear case of violation to me, and the CoC seems to
have defined a clear consequence of those violations. Then why is this person
still on the project?

Unfortunately dealing with CoC cases is usually very complicated and in my
experience, even in cases where it seems very clear what the judgment should
be, the committee does not easily agree on a single course of action, as very
apparent from this case as well. Let's talk about some of the reasons:

- Intent vs Impact: Some would argue that the person violating the CoC did not
  _intend_ to disrespect or harass anybody, and that's more important than the
  impact the interaction has had on the disrespected/harassed person. These
  days I personally don't really agree with the argument, especially after
  reading [35 Dumb Things Well-Intended People Say: Surprising Things We Say
  That Widen The Diversity
  Gap](https://www.goodreads.com/book/show/4455729-35-dumb-things-well-intended-people-say).
  As individuals, we should be aware of the consequences and the impact of our
  actions and watch for them.
- Considering the accused's position in the community: I think the most infamous
  example is [Linus Trovalds' many aggressive
  emails](https://arstechnica.com/information-technology/2013/02/linus-torvalds-i-will-not-change-linux-to-deep-throat-microsoft/)
  in the Linux Kernel community, and the community not reacting with an
  appropriate response. When people are in a position of power or influence, it
  makes it harder for the community or a CoC committee to act decisively. They
  don't have to be the sole owner of the
  [BDFL](https://en.wikipedia.org/wiki/Benevolent_dictator_for_life) of the
  project to make it hard to deal with; being a main contributor makes it hard
  enough.
- The accused being a peer: In many cases including this PyTest incidence, the
  accused is in a way a peer to the members of the CoC committee, who are also
  maintainers of the same project. This makes it really hard to deal with the
  case, since most people would rather try and _resolve_ the issue in one way
  or another, which does not involve banning their peer from the community.
  Most people would rather resolve the issue in the _nicest_ way possible.


In my experience, these [and many other] reasons prevent a candid, timely, and
decisive decision by the CoC committee. However, understanding the challenges
does not make individuals who feel strongly about the issue feel better about
the indecisiveness or lack of action, and as somebody who has been in that
position, I completely understand them.

So what can we do to improve the situation?

I believe having external people in the CoC team helps with providing an
outsider's perspective. They may have a more objective understanding of the
situation than people who are closely involved with the case. That said, many
teams may be averse to the idea since it would mean letting an _outsider_
in the team, and in a place which is very intimate and close to the heart of
many communities. Understandably, people don't want to _give control_ to an
outsider. However, our community is larger than a single project's community,
and we could help each other out. This doesn't have to be a centralized place
like the PSF to handle all the cases (of course they can be a great place for
advice), instead it could be a group of trusted and respected people who are
rather experienced and concerned about these issues, and could sit in different
CoC committees.

Another issue is that handling CoC cases is hard, unpleasant, and is not a
trivial skill. Unfortunately as a community we don't really appreciate these
skills [yet] and most people are extremely inexperienced in this regard. As a
consequence, when a project appoints a CoC committee, most probably many
members of the committee have not had any experience handling CoC cases.

I remember after handling a difficult CoC case, I reached out to people who
were CoC contacts of different projects to inquire about enforceability of a
given CoC, and almost nobody had any satisfying answer. This is a result of us
as a community having no clue about how to enforce our CoCs, and sometimes the
legal challenges attached to the issue make it harder. For instance,
somebody violating a CoC may not be breaking any laws (CoC are usually more
strict than the laws of the given country), and therefore it is really tricky
to enforce that CoC in a _public_ event. This and many other related details
are not things which you can expect a usual developer in a project to know
about.

As I see it, our communities have embraced having a code of conduct in one way
or another. These CoCs may not be perfect, but they're a step towards the right
direction (IMO). Then we had issues enforcing and actually implementing them,
and larger communities who have already had cases are now more equipped with
the tools they need to handle the cases. What needs to happen next, is for us
to openly talk about our cases without revealing the identities of people
involved. We should have a conversation about the details, and learn from one
another. We should also celebrate people who know how to handle these cases,
know them, and reach out for help when we're not sure what to do.

I'm very happy that this incident has attracted some attention in the
community, and I hope we learn from it and keep our communities more respectful
and healthier than what they are now. Afterall, this is one of the reasons we
are not really good at diversity and inclusion in our communities and improving
on this front would help with D&I as well.
