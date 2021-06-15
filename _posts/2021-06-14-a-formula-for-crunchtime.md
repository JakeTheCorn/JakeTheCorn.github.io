---
layout: post
title:  "A Formula for Crunch Time"
date:   2021-06-14 09:00:00 -0400
categories: jekyll update
---

# IT'S CRUNCH TIME
The project is running behind! It's due tomorrow! Everyone must work on the weekend!


<!-- here explain the symptoms and madness -->

# What to do?

## Identify the Core Stakeholders
<!-- these are the people who need to be alerted -->

## Assess current state
<!-- figure out where we are and what kind of effort needs to occur to push this across the finish line -->

## Identify the Requirements - (The Functional ones...)

<!-- here talk about behavioral changes needing to be prioritized much higher than structural ones -->

## De-scope!
<!-- general overview about descoping -->
### De-Scope the Behavioral Changes

What is "Core" and what is "Fluff"?


<!-- De-scope to the core use case -->

### De-Scope the data
<!-- if the data is particularly vast, solve for the bell curve, the most common data -->

## Optimize the Feedback Loop

-- One will not be able to go fast unless changes can be easily and quickly verified

***CRUNCH TIME*** might seem like a time when we do not have time for tests...

However, this is likely a false assumption.

Tests are generally a way to receive automated feedback about whether or not our functionality is doing
what it should be doing.

If a test takes 2 seconds to run, and the alternative takes 30 seconds to run, and if the test is relatively easy to write, one will generally save a good amount of time by writing tests.

***Trade-offs do exist***... and often (especially if most of the changes are very easy to see with the human eye, but hard to test) it is worth it to skip the automated test...

The key point here, is that if you need to go fast, one needs fast feedback.

## Test

You don't want to get stuck in a place where the work was done quickly but validating it takes a long time.
If the work cannot be easily validated, it will be hard to get it across the line and into the hands of customers.

Moreover, what is the point of doing work if we don't expect to validate the work?

Testing will uncover important nuance in the functionality much faster than manual testing in most cases.  If a problem is found, it is faster to find it early than to wait until code review time.

## Pair up.

Ask for help.  If the project depends on this feature/bugfix/etc... then it concerns the whole team.  Swarm the problem.

<!-- here, list ways in which a pairing buddy will make you go faster -->

# Capture non essentials in tickets

Anything that will be glossed over still needs to be documented somewhere in a ticket/issue.

This makes it not just so that we don't miss anything, but more importantly for our context, it allows us to keep only the core use case in mind while working.

The ability to only keep one thing in mind was never more important than it is in crunch time.

The more items one has to keep in mind, the less "Mental RAM" they have for what is core, essential, and urgent.
