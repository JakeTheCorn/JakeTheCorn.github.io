---
layout: post
title:  "Tdd with me: Python Number Guessing Game"
date:   2021-05-17 09:30:00 -0400
categories: jekyll update
---

This is an exercise for learning tdd (test driven development).

### How TDD Works
At a high level TDD has a few rules.

1. Get Tests Running
   <!-- - Optimize Feedback Cycles
      - Watcher: Preferably on a watcher where when new changes are saved, the tests are run automatically.  In lieu of this, run the tests in a while loop from command line.
      - Try to only run the tests needed. -->

2. Write a failing test (Red)
3. Write the code that passes this test. (Green)
4. Refactor the code to improve design  (Refactor)

### Prerequisites
Install docker on your machine. Make sure it is running. Run the following command

{% highlight bash %}
docker pull python:3.10.0b1-alpine3.13
# Confirm it is installed and that python is available
docker run -it --rm python:3.10.0b1-alpine3.13 python --version
{% endhighlight %}

### Setup

{% highlight bash %}
mkdir python_number_guessing_game
cd python_number_guessing_game
{% endhighlight %}

Then we need to shell into our docker container as well as connect local file system to the container's file system.

{% highlight bash %}
docker run \
    -it \
    --volume="$(pwd)":/python_number_guessing_game \
    --rm \
    --workdir=/python_number_guessing_game \
    python:3.10.0b1-alpine3.13 \
        /bin/sh
{% endhighlight %}

You should notice that your shell's prompt has now changed


### Get Tests Running
Before it is important to write a test it is important to get a test running.  This may seem counterintuitive but
in my experience it is as simple as pointing a test runner towards a test file that will be created.

Inside the container run the following...

{% highlight bash %}
python -m unittest number_guessing_game_tests.py
{% endhighlight %}

You should then see an error like
```
ModuleNotFoundError: No module named 'number_guessing_game_tests'
```

So to get around this, let's create a file and rerun...

{% highlight bash %}
touch number_guessing_game_tests.py
python -m unittest number_guessing_game_tests.py
{% endhighlight %}

You should then see output like...
```
Ran 0 tests in 0.000s
```

But it was kind of a pain to have to manually run these tests... let's automate the running of our test

{% highlight bash %}
watch python -m unittest number_guessing_game_tests.py
{% endhighlight %}

Great! we're able to run our tests... but we don't have any tests in our file...

But... we also don't know yet _what to test_!

### Todo list
The todo list is an important part of Test Driven Development.  It allows you to focus on one thing at a time.

Let's write ours.  This is where we will define what our program should do.
Let's keep it as simple as possible for now.

at the top of the new file add the following

{% highlight python %}
"""
    TODO:
        - It writes a welcome message before the game begins
"""
{% endhighlight %}

Now we know _what to test_ let's write our test. Lower in the file we write our tests.

{% highlight python %}
# above here is our todo list...
import unittest


class NumberGuessingGameTests(unittest.TestCase):
    def test_it_writes_a_welcome_message_before_the_game_begins(self):
        pass
{% endhighlight %}

Output should look like ...

```
Ran 1 test in 0.000s
```

(Note: Have you noticed how many times this code has been run?)

**_But we're not yet making any valuable assertions._**

### No new code until a new test is failing




<!--

1. Optimize Feedback Cycles
      - Watcher: Preferably on a watcher where when new changes are saved, the tests are run automatically.  In lieu of this, run the tests in a while loop from command line.
      - Try to only run the tests needed. -->
