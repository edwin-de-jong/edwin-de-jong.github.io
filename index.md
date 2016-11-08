---
layout: page
title: Edwin D. de Jong
#tagline: homepage
---
{% include JB/setup %}


[](Posts:)
<ul class="posts">
  {% for post in site.posts %}
    <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>





<img src="fig/edwin-de-jong.jpg" style="width:150px;height:150px;">

Twitter: [@EdwinDdeJong](https://twitter.com/EdwinDdeJong)

Github: [https://github.com/edwin-de-jong](edwin-de-jong)

Email: <img src="edwin-de-jong-contact.png" alt="email" style="width:600px;height:40px;">

Interests: Building new machine learning technology &#124; Deep Learning &#124; Representation Learning &#124; Artificial Intelligence &#124; Coevolutionary Algorithms

##Publications
See [Google Scholar page](https://scholar.google.com/citations?user=l9w80gcAAAAJ&hl=en)	

##Projects

###Incremental Sequence Learning


<a href="pub/incremental-sequence-learning.pdf">
<img src="blog/isl/rnn-movies/2-movie.gif" width="275">
<img src="blog/isl/rnn-movies/4-movie.gif" width="275">
<img src="blog/isl/rnn-movies/9-movie.gif" width="275">
</a>

These videos show what a generative recurrent neural network has learned over the course of training.
This research is based on the notion that you need to *remember the past to predict the future*, as noted in this excellent [presentation on generative RNNs](https://www.youtube.com/watch?v=-yX1SYeDHbg) by Alex Graves.

To ensure that the preceding part of the sequences has been learned well before the network is asked to predict later parts of the sequence, we start out by training on the *first few steps* of each sequence only. Once a reasonable performance level has been reached, the lengths of the sequences presented to the network is increased, until the network is trained on complete sequences.

In experiments with the MNIST stroke sequence data set, this simple technique was found to greatly speed up learning *and* improve generalization performance. For details, see the [article](pub/incremental-sequence-learning.pdf) on Incremental Sequence Learning.


###The MNIST Stroke Sequence Data Set


<a href="https://github.com/edwin-de-jong/mnist-digits-stroke-sequence-data/wiki/MNIST-digits-stroke-sequence-data"><img src="https://github.com/edwin-de-jong/mnist-digits-stroke-sequence-data/raw/master/fig/trainimg-25-sequence.png" width="200"></a> MNIST stroke sequence [data](https://github.com/edwin-de-jong/mnist-digits-stroke-sequence-data/wiki/MNIST-digits-stroke-sequence-data): all 70000 [MNIST](http://yann.lecun.com/exdb/mnist/) handwritten digit images transformed to stroke sequences. The code to reproduce the MNIST stroke sequence data is available [here](https://github.com/edwin-de-jong/mnist-digits-as-stroke-sequences/wiki/MNIST-digits-as-stroke-sequences-(code)) .


