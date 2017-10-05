Title: A Criticism of "Detecting Sexual Orientation Using Neural Networks"
Date: 2017-10-05
Tags: ethics, machine-learning
Category: ethics

I'd like to talk about this study: [Deep neural networks are more accurate than humans at detecting sexual orientation from facial images](https://osf.io/fk3xr/), and it's not going to be a praise of the research!

## Damaging Message
I put this study in the same category as studies trying to argue women are different than men, usually in derogatory ways, e.g. proving they're weaker, less intelligent, or worse at math. Recently we had the google engineer citing a whole bunch of them to support his argument about why men are better coders, or men are better in tech, or whatever bullshit he wanted to argue for. Honestly I won't bother reading it; I mostly heard about it in podcasts and read about it in the news. My point is, those gender related studies tend to be more damaging than beneficial, and I see no point in doing them. I understand this is a very consequentialist way of assessing the value of the work, but I'm comfortable with it for now.

It's the same with the study in question. What's the point of having a module predicting people's sexual orientation given a face image, other than some other people using it in an argument such as: "Your face shouts you're gay, scientifically proven"!!! I'm sure our dear homophobes out there can think of more damaging ways of using the results of this research. This is all I could come up with!

## Methodology
I don't even know where to start. I'll split these points into the ones questioning the validity of the study, and the ones which are simply poor wording.

### Questioning Validity

#### AUC calculation
In a classification problem, you'd use your module to predict the outcome, draw the ROC, and calculate the Area Under ROC (AUC). Pretty straightforward for a binary classification, which is the case in this paper. What I don't understand, is this randomly choosing a straight person's photo to compare against a homosexual, to calculate an AUC. I simply don't understand why you'd do that, and as a result, I can't assess the performance measures reported in the article.

#### Variance of the accuracy
They report one AUC performance for those 20 folds. I guess the results are accumulated over 20 folds and one single AUC is calculated overall. This is important, because the calculated performance usually highly depends on the random split of the data. Therefore without a data showing the distribution of the calculated AUCs, one single number is not representative of how reliable the model in reality is.

#### SVD on each fold separately or not?
In any data analysis, it is crucial to apply [virtually all] preprocessing steps only on the training data. Otherwise you're already seeing the test data before even starting you training, and that's cheating.

The text is not clear weather they run a separate SVD for each of those 20 folds they have or not. If they do SVD once and use the same features on all those folds, the results are immediately invalid. I cannot tell from the text what they've done, and I couldn't see a link to their source code. My guess is that they are actually doing it the right way, but it's not written clearly.

#### Model Interpretation
Quoting the article:

> The gender atypicality of gay faces extended beyond morphology. Gay men had less facial hair, suggesting differences in androgenic hair growth, grooming style, or both. They also had lighter skin, suggesting potential differences in grooming, sun exposure, and/or testosterone levels. Lesbians tended to use less eye makeup, had darker hair, and wore less revealing clothes (note the higher neckline), indicating less gender-typical grooming and style. Furthermore, although women tend to smile more in general (Halberstadt, Hayes, & Pike, 1988), lesbians smiled less than their heterosexual counterparts. Additionally, consistent with the association between baseball caps and masculinity in American culture (Skerski, 2011), heterosexual men and lesbians tended to wear baseball caps (see the shadow on their foreheads; this was also confirmed by a manual inspection of individual images). The gender atypicality of the faces of gay men and lesbians is further explored in Study 2.

Comparing these factors with the reported AUC, you could argue that social trends and stereotypes followed by many people, has a substantial factor in giving the classifier its power. To better understand my point, assume you want to train a classifier predicting whether or not a person in a picture is a transgender. Since many transgender people follow an exaggerated version of the opposite gender's stereotypes in the society, and the skull itself is predictive of the sex of the person to a good extent on its own, the model would probably have an easy time giving the right outcome.

[![Skull and sex](http://img.youtube.com/vi/GHl8xvc-GCI/0.jpg)](http://www.youtube.com/watch?v=GHl8xvc-GCI)

What I mean, is that if you have a model which doesn't take into account the confound social variables to predict a certain variable, your results are crap!

### Poor wording

#### Not a Deep Neural Network (DNN) Method
The article suggests DNNs can achieve the reported performance, while using a DNN only to extract features, and then feeding them to an SVD->LASSO->logistic regression pipeline. How is that a DNN method? I can only imagine they've chosen to advertise it as such, due to the hype around deep learning; after all, who would dare to argue with a DNN these days? Basically, the statement "deep neural networks can detect sexual orientation from faces" is a complete misrepresentation of the research.

#### LASSO and alpha
They say they use LASSO with alpha=1 for feature selection. The alpha they refer to is a parameter of elastic net, not LASSO, which results in LASSO when set to 1. In other words, LASSO ALWAYS has that alpha equal to 1, otherwise it's not a LASSO.

## Final Remarks
I guess at the writing of this post, the article has not been accepted and it may be subject to many changes; in which case, I hope reviewers find the problems I found and many more, so that the final version of the article is a much better work than what I read. But even then, I have a hard time understanding the reason behind such studies. I'm sure there are much better and more beneficial ways of analyzing the same data and coming up with much better conclusions.

Also, I could only analyze this research in depth only if I had the code and the data publicly available. One may argue that I can contact the authors asking for the code and the data; but that's not what I call "publicly available"!