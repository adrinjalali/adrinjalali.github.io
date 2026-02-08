Title: Talks
Slug: talks

I've given talks at various Python, data science, and machine learning conferences over the years. Here are some recordings.

---

### Let's exploit pickle, and `skops` to the rescue!
**EuroSciPy 2023** · Basel, Switzerland · [Conference page](https://pretalx.com/euroscipy-2023/talk/ARBBQF/)

Pickle files can be evil and simply loading them can run arbitrary code on your system. This talk presents why that is, how it can be exploited, and how skops is tackling the issue for scikit-learn/statistical ML models. I go through the process used by the pickle module to persist Python objects, demonstrating how `__getstate__`, `__setstate__`, and `__reduce__` methods can be exploited to create malicious pickle files. Then I introduce the skops library's alternative format for securely storing scikit-learn, xgboost, lightgbm, and catboost estimators.

<div class="ratio ratio-16x9 mb-4">
<iframe src="https://www.youtube.com/embed/kfEaIPAYcLM" title="Let's exploit pickle, and skops to the rescue!" allowfullscreen></iframe>
</div>

---

### Dynamically generated methods with a non-generic signature
**EuroPython 2023** · Prague, Czech Republic · [Conference page](https://ep2023.europython.eu/session/dynamically-generated-methods-with-a-non-generic-signature)

A deep dive into Python metaprogramming using scikit-learn as a case study. This talk explores how to add methods to all subclasses of a base class where the generated method signatures depend on existing subclass methods. I cover inspecting method signatures with the `inspect` module, traversing the Method Resolution Order (MRO), using descriptors for method generation, applying PEP-362 to attach signature objects, dynamically creating docstrings, and leveraging PEP-487's `__init_subclass__` to attach methods to child classes.

<div class="ratio ratio-16x9 mb-4">
<iframe src="https://www.youtube.com/embed/1rf6HI-pYq8" title="Dynamically generated methods with a non-generic signature" allowfullscreen></iframe>
</div>

---

### Best practices to open source a product and creating a community around it
**EuroPython 2022** · Dublin, Ireland · [Conference page](https://ep2022.europython.eu/session/best-practices-to-open-source-a-product-and-creating-a-community-around-it)

In certain areas of the industry, open source has become mainstream. But making source code publicly available on platforms like GitHub is not enough. This talk explores critical factors for successful open source projects including licensing, governance structures, and common mistakes that discourage newcomers. I cover various governance models (do-ocracy, founder-led, electoral, corporate-backed, and foundation-backed approaches) and community pitfalls such as poor onboarding, unclear leadership, weak communication, and insufficient transparency.

<div class="ratio ratio-16x9 mb-4">
<iframe src="https://www.youtube.com/embed/wuS8PTkNHiQ" title="Best practices to open source a product" allowfullscreen></iframe>
</div>

---

### scikit-learn and fairness, tools and challenges
**NeurIPS 2020** · Virtual · [SlidesLive](https://slideslive.com/38942315/scikitlearn-and-fairness-tools-and-challenges)

Presented with Nana Yamazaki at the NeurIPS Expo. We start with a common classification pipeline, then assess fairness/bias of the data/outputs using disparate impact ratio as an example metric, and finally mitigate unfair outputs while searching for hyperparameters that give the best accuracy while satisfying fairness constraints. This workflow exposes limitations of the scikit-learn API related to passing around feature names and sample metadata in a pipeline down to the scorers. We discuss workarounds and the ongoing work to address these issues.

<div class="ratio ratio-16x9 mb-4">
<iframe src="https://slideslive.com/embed/presentation/38942315" allowfullscreen></iframe>
</div>

---

### How to write a scikit-learn compatible estimator/transformer
**FOSDEM 2020** · Brussels, Belgium · [Conference page](https://archive.fosdem.org/2020/schedule/event/python2020_scikit_learn_estimator/)

A hands-on tutorial on writing custom estimators or transformers that work seamlessly in scikit-learn pipelines. The session covers tips and tricks, testing your estimator against scikit-learn's common tests, and integration with pipelines and grid searches. This was my first time presenting to ~500 people in the Python room.

<div class="ratio ratio-16x9 mb-4">
<video controls style="width: 100%; height: 100%;">
<source src="https://video.fosdem.org/2020/UB2.252A/python2020_scikit_learn_estimator.mp4" type="video/mp4">
Your browser does not support the video tag. <a href="https://video.fosdem.org/2020/UB2.252A/python2020_scikit_learn_estimator.mp4">Download the video</a>.
</video>
</div>

---

### Current affairs, updates, and the roadmap of scikit-learn
**PyConDE & PyData Berlin 2019** · [Conference page](https://2019.pycon.de/program/pydata-x7fsx9-current-affairs-updates-and-the-roadmap-of-scikit-learn-and-scikit-learn-contrib-adrin-jalali/)

An update on recent scikit-learn changes, current affairs, and the project roadmap. I discuss the challenges of managing scikit-learn with significant community engagement but limited core developer capacity, covering recent events around the scikit-learn community and major ongoing initiatives. The talk also addresses the broader ecosystem including scikit-learn-contrib and scikit-learn-extra, which houses models and methods that don't pass the inclusion criteria of scikit-learn.

<div class="ratio ratio-16x9 mb-4">
<iframe src="https://www.youtube.com/embed/0tXIkjClGOs" title="Current affairs, updates, and the roadmap of scikit-learn" allowfullscreen></iframe>
</div>

---

### The path between developing and serving machine learning models
**PyData Berlin 2017** · [Conference page](https://pydata.org/berlin2017/schedule/presentation/31/)

A tutorial on deploying machine learning models using PipelineIO and PMML (Predictive Model Markup Language). This talk explores the gap between developing models in Python and serving them in production environments, covering practical approaches to model serialization and deployment.

<div class="ratio ratio-16x9 mb-4">
<iframe src="https://www.youtube.com/embed/0knKCboeDBM" title="The path between developing and serving machine learning models" allowfullscreen></iframe>
</div>
