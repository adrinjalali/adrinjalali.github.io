Title: A Central Cancer Diagnostics Hub 
Date: 2017-02-28
Tags: reproducibility-crisis, ideas, cancer, bioinformatics
Category: science
Status: draft

Although the context of this post is bioinformatics and cancer, it applies to many other fields as well. I've had this idea for a while, and this an effort to make it more concrete. In this post, a method refers to a computational model or an algorithm, from the preprocessing phase to the final result.

### Motivation
The idea is motivated by my experience in bioinformatics, dealing with cancer data and cancer related questions such as cancer diagnostics. It tries to help the following challenges:

- Reproducibility crisis, which I talked about in more detail [here](http://adrin.info/an-essay-on-the-reproducibility-crisis.html)
- Reinventing the wheel (over and over again). In science to show the merits of your work, you most probably need to compare it with other methods. Since most methods are not open source, and even when they are, it's not a trivial task to use them on your data. Hence you end up at least partially re-implementing those methods yourself. 
- The gap between research and clinics. Again, since it's not easy to use most published methods on your data, it's not easy for clinics to take a publication and use that method on patients' data.

### Proposed solution
We could, ideally, have a place facilitating method development as well as their usage. To understand the proposed system, consider the problem of predicting the subclass of different cancer types, and the following three players or stakeholders.

#### The programmer, or the bioinformatician
The system provides certain APIs for programmers to deliver tasks related to cancer diagnostics. These tasks are steps along the way of the analysis. Preprocessing of the data is one step, so is predicting the sub-class of a cancer for instance. Programmers don't have to implement the whole pipeline; they can focus on a method, for example, which relies on a certain preprocessing model which has already been implemented on the datasets. Or in contrast, a researcher can implement a preprocessing technique and test it in combination with different methods available in the repository of the system.

#### The oncologist, or a clinic
Once a method is uploaded in the system, it can be trained on different cancer types, and then a clinic or a hospital can use the system to get suggestions on the subclass of the cancer of a newly acquired sample from a patient. They can also check if different methods agree with each other on the predicted subclass.

#### The lab/person producing data
The data can be added to the system, to have the back-end run different existing algorithms against the newly acquired dataset.


### Practicalities

