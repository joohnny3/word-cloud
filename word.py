#!/usr/bin/env python
"""
Minimal Example
===============

Generating a square wordcloud from the US constitution using default arguments.
"""

import os
import random
from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import ImageColor


def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(240, 100%%, %d%%)" % random.randint(25, 75)


# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
text = open(path.join(d, 'text.txt')).read()

# Generate a word cloud image
wordcloud = WordCloud(background_color='white',
                      color_func=color_func).generate(text)

# Display the generated image:
# the matplotlib way:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

# lower max_font_size
wordcloud = WordCloud(background_color='white', height=360, width=1440, min_font_size=12,
                      max_font_size=48, color_func=color_func, max_words=80, stopwords={"Catcher"},font_step=2).generate(text)
wordcloud.to_file(path.join(d, 'wordcloud.png'))
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

# The pil way (if you don't have matplotlib)
# image = wordcloud.to_image()
# image.show()
