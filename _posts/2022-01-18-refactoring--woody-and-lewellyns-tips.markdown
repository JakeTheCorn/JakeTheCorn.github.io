---
layout: post
title:  "Refactoring - Tips from a Woody Zuill and Lewellyn Falco session"
date: 2022-01-18 09:00:00 -0400
categories: jekyll update
---

I just wanted to leave a few of the notes from this great video from Woody Zuill and Lewellyn Falco.

[Practical Refactoring - How to clean code in many small steps](https://www.youtube.com/watch?v=aWiwDdx_rdo&ab_channel=LlewellynFalco)


## Refactoring
***(do the following in order)***

<hr />

* Remove Clutter -- Remove Anything in the code that has no value
    * Format Code
    * Remove Comments
    * Remove Dead Code
    * Remove Unnecessary code

* Remove Complexity
    * Bad Names
    * Long Methods
    * Deep Conditionals
    * Magic Numbers/Strings
    * Improper Variable Scoping
    * Missing Encapsulation
    * Obscure Code Blocks

* Remove Cleverness
    * Cryptic Code
    * Abbreviated Code
    * Hijacked Methods - methods that have been modified beyond their original intent/design

* Remove Duplication


<hr />

<br />
<br />
<br />

Some quotes I like about refactoring.

  > Refactoring is held to a higher standard -- don't give business as reason to say 'no refactoring' -- Jay Bazuzi

  > "Good" is the enemy of "slightly less terrible" -- Arlo Benshee

One from Kent Beck...

> Strive to make the design of the system a perfect git for the needs of the system that day -- Kent Beck

I like this one a lot because it empowers us to design the system as well as it could be, without some kind of 
fortune telling or forecasting... We tend to always know the needs of the system for a given day and so it is
possible for us to design it perfectly to meet those needs... (At least we "Strive" to...)

