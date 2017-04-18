Title: A Central Cancer Diagnostics Hub 
Date: 2017-04-18
Tags: reproducibility-crisis, ideas, cancer, bioinformatics
Category: science

Although the context of this post is bioinformatics and cancer, it applies to many other fields as well. I've had this idea for a while, and this an effort to make it more concrete. In this post, a method refers to a computational model or an algorithm, from the preprocessing phase to the final result.

### Motivation
The idea is motivated by my experience in bioinformatics, dealing with cancer data and cancer related questions such as cancer diagnostics. It tries to help the following challenges:

- Reproducibility crisis, which I talked about in more detail [here](http://adrin.info/an-essay-on-the-reproducibility-crisis.html)
- Reinventing the wheel (over and over again). In science to show the merits of your work, you most probably need to compare it with other methods. Since most methods are not open source, and even when they are, it's not a trivial task to use them on your data. Hence you end up at least partially re-implementing those methods yourself. 
- The gap between research and clinics. Again, since it's not easy to use most published methods on your data, it's not easy for clinics to take a publication and use that method on patients' data.

### Players
We could, ideally, have a place facilitating method development as well as their usage. To understand the proposed system, consider the problem of predicting the subclass of different cancer types, and the following three players or stakeholders.

#### The programmer, or the bioinformatician
The system provides certain APIs for programmers to deliver tasks related to cancer diagnostics. These tasks are steps along the way of the analysis. Preprocessing of the data is one step, so is predicting the sub-class of a cancer for instance. Programmers don't have to implement the whole pipeline; they can focus on a method, for example, which relies on a certain preprocessing model which has already been implemented on the datasets. Or in contrast, a researcher can implement a preprocessing technique and test it in combination with different methods available in the repository of the system.

#### The oncologist, or a clinic
Once a method is uploaded in the system, it can be trained on different cancer types, and then a clinic or a hospital can use the system to get suggestions on the subclass of the cancer of a newly acquired sample for a patient. They can also check if different methods agree with each other on their prediction.

#### The lab/person producing data
When a lab produces a new dataset, they usually need to analyze the data and explain how their dataset can be used and where its values are. They could upload the dataset to this system and have different methods run against it, and analyze their outcome.

### Related and existing work
There are many open datasets out there, but they are not necessarily nicely formatted and they don't follow the same guidelines to store the data. There are however, at least two efforts to tackle this problem, one is [ICGC](https://icgc.org/) in Europe, and the other one is [TCGA](https://cancergenome.nih.gov/) in the US. These efforts store the data in a nicely formatted way, which makes it convenient to develop a method on one cancer type, and try it on the other ones. There are also places which have their own method run against different datasets, and you can browse their results and visualizations, or efforts and products enabling you to create your own platform and data storage. Some examples using the TCGA data are listed [here](https://cancergenome.nih.gov/abouttcga/aboutdata/analyticaltools), and [DNAnexus](https://www.dnanexus.com) is an example of a company providing related services.

### Conclusion
We, as a society, need an open product and a team delivering such a service, which is easy to setup and use. I recently left academia, while still wrapping up my PhD thesis, and joined industry. I see very well where academia could use recent advancements in industry when it comes to big data and machine learning infrastructure, and also how clinics and the industry could benefit from a fast adaptation of recent academic advances.


_Note_: I'll try to update this post as it develops.
