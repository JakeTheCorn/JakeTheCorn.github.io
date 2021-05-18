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

_(Errors like this are good feedback, errors can be our friends)_

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

Great! we're able to run our tests automatically... but we don't have any tests in our file...

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

One of the rules of TDD is that no new production code should be written until we've first written a failing test.

But what comprises a test...?

### Arrange, Act, Assert


Every test has three parts
- Arrange
  - We set up controlled inputs and conditions important to the test.
- Act
  - We pass in any inputs we built up in the arrange step and execute the code that is under test.
- Assert
  - We assert the results we expect to see.

_(If you can try to write the assert step first)_

### Back to writing our test...

Let's start by writing the assertion first

{% highlight python %}
class NumberGuessingGameTests(unittest.TestCase):
    def test_it_writes_a_welcome_message_before_the_game_begins(self):
        writer.write.assert_called_once_with('Welcome to the number guessing game')
{% endhighlight %}


Now you should see something like...
```
NameError: name 'writer' is not defined
```

That's okay, let's create it...

### Mocks

So we want to say that a writer's write method is called... but now we have the problem of defining a "writer"

(If we weren't test-driving this we probably just would have written this to stdout by calling print...but this is so much better, I'll tell you why later)

Let's use python's standard mock library...

{% highlight python %}
# ...
import unittest
from unittest.mock import Mock


class NumberGuessingGameTests(unittest.TestCase):
    def test_it_writes_a_welcome_message_before_the_game_begins(self):
        writer = Mock()
        writer.write.assert_called_once_with('Welcome to the number guessing game')
{% endhighlight %}

Now we look and the error has changed...

```
AssertionError: Expected 'write' to be called once. Called 0 times.
```

So, we start working our way backwards.

**_What is the relationship of the Game and the Writer?_**

Let's pass a writer to the Game's constructor and call game.play()

{% highlight python %}
class NumberGuessingGameTests(unittest.TestCase):
    def test_it_writes_a_welcome_message_before_the_game_begins(self):
        writer = unittest.mock.Mock()
        game = Game(writer)
        writer.write.assert_called_once_with('Welcome to the number guessing game')
{% endhighlight %}

Now we get a new error...

```
NameError: name 'Game' is not defined
```

Let's define it in the same file... Currently the test is the only client of our Game code so it makes sense to keep it as close as possible to keep things easy to change.

Below our test class let's define Game...

{% highlight python %}
class Game:
    def __init__(
        self,
        writer,
    ):
        self.writer = writer
{% endhighlight %}

New error...

```
AttributeError: 'Game' object has no attribute 'play'
```

Let's define play to make that error go away...

{% highlight python %}
class Game:
    def __init__(
        self,
        writer,
    ):
        self.writer = writer

    def play(self):
        pass
{% endhighlight %}

Yet another error...

```
AssertionError: Expected 'write' to be called once. Called 0 times.
```

But... Didn't we already have this error? Yes... but now we have some idea about the relationship our Game has with our Writer, so we're actually much further along. Let's call our write method...

{% highlight python %}
class Game:
    def __init__(
        self,
        writer,
    ):
        self.writer = writer

    def play(self):
        self.writer.write('Welcome to the number guessing game')
{% endhighlight %}

** Viola! A passing test! **
```
Ran 1 test in 0.001s

OK
```

### Refactor Check In...

You may remember that we had three steps...
1. Red - Write a failing test
2. Green - Write the code that makes it pass
3. Refactor - Improve the design of the existing code.

So we are at the refactor stage for this functionality.

What kinds of things could we do to improve the design?

I'd like to...
- Change the positional argument "writer" to a keyword only argument (I think it's less confusing to always use names instead of trying to conflate a position with a meaning.)
- Use an underscore inside the Game class for its writer attribute to denote that it should be viewed as non-public.

I like to use the todo list to capture these thoughts so I don't have to keep them in my head while I'm making other changes.

So...Let's add these to the todo list...

{% highlight python %}
"""
    TODO:
        - It writes a welcome message before the game begins
            - Make writer arg in Game ctor keyword only
            - Make writer attr in Game appear as non-public
"""
{% endhighlight %}

We make our changes and update the todo accordingly...

The file should now resemble

{% highlight python %}
"""
    TODO:
        √ It writes a welcome message before the game begins
            √ Make writer arg in Game ctor keyword only
            √ Make writer attr in Game appear as non-public
"""

import unittest
from unittest.mock import Mock

class NumberGuessingGameTests(unittest.TestCase):
    def test_it_writes_a_welcome_message_before_the_game_begins(self):
        writer = Mock()
        game = Game(
            writer=writer
        )
        game.play()
        writer.write.assert_called_once_with('Welcome to the number guessing game')


class Game:
    def __init__(
        self,
        *,
        writer,
    ):
        self._writer = writer

    def play(self):
        self._writer.write('Welcome to the number guessing game')
{% endhighlight %}

### Our Second Todo

Now we have completed our first cycle so it is time to think about what to test next.

The next thing it should do is ask me to guess a number between 1 and 10.

Update your Todo
{% highlight python %}
"""
    TODO:
        √ It writes a welcome message before the game begins
            √ Make writer arg in Game ctor keyword only
            √ Make writer attr in Game appear as non-public
        - It writes a message asking the player to guess a number between 1 and 10
"""
{% endhighlight %}


Let's write our new test...

{% highlight python %}
class NumberGuessingGameTests(unittest.TestCase):
    def test_it_writes_a_welcome_message_before_the_game_begins(self):
        writer = Mock()
        game = Game(
            writer=writer
        )
        game.play()
        writer.write.assert_called_once_with('Welcome to the number guessing game')

    def test_it_writes_a_message_asking_player_to_guess_number_between_1_and_10(self):
        writer = Mock()
        game = Game(
            writer=writer
        )
        game.play()
        writer.write.assert_called_once_with('Please pick a number between 1 and 10')
{% endhighlight %}

A new Error!

```
AssertionError: expected call not found.
Expected: write('Please pick a number between 1 and 10')
Actual: write('Welcome to the number guessing game')
```

(Thanks to unittest for producing such nice errors.)

BAM! red... now time to get to green...

Let's update the Game class

{% highlight python %}
class Game:
    def __init__(
        self,
        *,
        writer,
    ):
        self._writer = writer

    def play(self):
        self._writer.write('Welcome to the number guessing game')
        self._writer.write('Please pick a number between 1 and 10')
{% endhighlight %}

hmm... we still see an error, in fact now both of our tests are failing.

```
AssertionError: Expected 'write' to be called once. Called 2 times.
Calls: [call('Welcome to the number guessing game'),
 call('Please pick a number between 1 and 10')].
```

So it seems like we've learned something... maybe assert_called_once_with is exclusive. -- meaning that it is exclusive to not just the input, but the call itself.

While this could seem frustrating another way to look at it is that our tests are giving us rapid feedback about the libraries we are using... making it easier to try new things.

After googling for assert has calls with multiple calls I found an attribute called "mock_calls" that can be accessed and asserted against.

Let's try that...

### Back to Safety (Back to Green)

Currently both of our tests are failing. We need to fix that.

Put an _ (underscore) in front of our new test method so that it is removed from the running.

Now we only have 1 failing test.

It is failing because we are wanting to call .write(msg: str) multiple times and are asserting that it is called only once.  To fix this we use our new mock_calls attribute.


{% highlight python %}
# ...
import unittest
from unittest.mock import Mock, call

class NumberGuessingGameTests(unittest.TestCase):
    def test_it_writes_a_welcome_message_before_the_game_begins(self):
        writer = Mock()
        game = Game(
            writer=writer
        )
        game.play()
        first_call = writer.write.mock_calls[0]
        self.assertEqual(first_call, call('Welcome to the number guessing game'))

    def _test_it_writes_a_message_asking_player_to_guess_number_between_1_and_10(self):
        writer = Mock()
        game = Game(
            writer=writer
        )
        game.play()
        writer.write.assert_called_once_with('Please pick a number between 1 and 10')
# ...
{% endhighlight %}

```
Ran 1 test in 0.001s
```

But one thing I'm not crazy about is that my tests now know about about the order of which the writer is called.  I will add a TODO to revisit this.

{% highlight python %}
"""
    TODO:
        √ It writes a welcome message before the game begins
            √ Make writer arg in Game ctor keyword only
            √ Make writer attr in Game appear as non-public
        - It writes a message asking the player to guess a number between 1 and 10
            - Revisit the tests knowing about order of writer calls
"""
{% endhighlight %}

Now let's get that second test passing! We'll do something similar to what was done above...First, remove the underscore so the test runner will pick it up.

{% highlight python %}
# ...
import unittest
from unittest.mock import Mock, call

class NumberGuessingGameTests(unittest.TestCase):
    def test_it_writes_a_welcome_message_before_the_game_begins(self):
        writer = Mock()
        game = Game(
            writer=writer
        )
        game.play()
        first_call = writer.write.mock_calls[0]
        self.assertEqual(first_call, call('Welcome to the number guessing game'))

    def test_it_writes_a_message_asking_player_to_guess_number_between_1_and_10(self):
        writer = Mock()
        game = Game(
            writer=writer
        )
        game.play()
        second_call = writer.write.mock_calls[1]
        self.assertEqual(second_call, call('Please pick a number between 1 and 10'))
# ...
{% endhighlight %}

Now 2 tests are passing.

```
Ran 2 tests in 0.001s

OK
```

### Refactor Check in number 2

Looking at the code I think there are some things to address.

1. We are repeating common arrange/setup functionality in both methods.  It would be nice to remove repetition here.
2. I prefer putting the expectation on the left of my assertEqual calls.  It's just something I've noted from other test libraries and I'd like to maintain that habit
3. I think the calls to the `call()` method are a little vague.  I would like to call `mock.call()` instead to put front and center in the code that this is a mock call.  Will have to change imports if possible


Let's add these to our Todo list so that we don't have to keep them all in mind.

{% highlight python %}
# ...
"""
    TODO:
        √ It writes a welcome message before the game begins
            √ Make writer arg in Game ctor keyword only
            √ Make writer attr in Game appear as non-public
        - It writes a message asking the player to guess a number between 1 and 10
            - Revisit the tests knowing about order of writer calls
            - DRY common test arrage/setup steps
            - put expectation on left side of assertEqual
            - use mock.call() instead of call() to make meaningful distinction in calling code
"""

{% endhighlight %}

We'll talk about the revisit portion in a minute.  Update the code and check the other three items off.

At this point the file should look something like this...

{% highlight python %}

"""
    TODO:
        √ It writes a welcome message before the game begins
            √ Make writer arg in Game ctor keyword only
            √ Make writer attr in Game appear as non-public
        - It writes a message asking the player to guess a number between 1 and 10
            - Revisit the tests knowing about order of writer calls
            √ DRY common test arrage/setup steps
            √ put expectation on left side of assertEqual
            √ use mock.call() instead of call() to make meaningful distinction in calling code
"""

import unittest
import unittest.mock as mock


class NumberGuessingGameTests(unittest.TestCase):
    def setUp(self):
        self.writer = mock.Mock()
        self.game = Game(
            writer=self.writer
        )

    def test_it_writes_a_welcome_message_before_the_game_begins(self):
        self.game.play()
        first_call = self.writer.write.mock_calls[0]
        self.assertEqual(
            mock.call('Welcome to the number guessing game'),
            first_call,
        )

    def test_it_writes_a_message_asking_player_to_guess_number_between_1_and_10(self):
        self.game.play()
        second_call = self.writer.write.mock_calls[1]
        self.assertEqual(
            mock.call('Please pick a number between 1 and 10'),
            second_call,
        )


class Game:
    def __init__(
        self,
        *,
        writer,
    ):
        self._writer = writer

    def play(self):
        self._writer.write('Welcome to the number guessing game')
        self._writer.write('Please pick a number between 1 and 10')

{% endhighlight %}

### Discourage Sharing

The setup method runs for every test case.  This discourages shared state which enables us to improve the ergonomics of our tests while still maintaining high degrees of isolation. Isolation is really important since one would like to know that tests are not affecting each other thereby harming determinism -- one of the main points of testing.

### Tradeoffs

At this point I'd like to take a second to discuss tradeoffs.

- Tests should be behavior DEPENDENT and structure INDEPENDENT
   - Ideally we would like our tests to know as little about structure as possible so that structure can safely be changed/improved without breaking our tests.  Sometimes it is harder than it is worth, but it's always worth some examination.  In our case, our test knows about the order of calls to .write(msg: str) in the Game class.  I think this is okay though because what if instead of it knowing about structure we thought of it as the spec... for example: "It asks the writer to write a welcome message, then asks the writer to write the rules of the game".  That doesn't seem as structural. So it goes, and at this time I do not have a better solution.

Check off that "Revisit" todo. We have "revisited". And we can check off the second item as we have gone through another Red/Green/Refactor cycle.

{% highlight python %}
"""
    TODO:
        √ It writes a welcome message before the game begins
            √ Make writer arg in Game ctor keyword only
            √ Make writer attr in Game appear as non-public
        √ It writes a message asking the player to guess a number between 1 and 10
            √ Revisit the tests knowing about order of writer calls
            √ DRY common test arrage/setup steps
            √ put expectation on left side of assertEqual
            √ use mock.call() instead of call() to make meaningful distinction in calling code
"""
{% endhighlight %}
