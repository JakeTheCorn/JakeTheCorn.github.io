---
layout: post
title:  "Design Patterns - Template Method - C#"
date:   2021-06-07 09:00:00 -0400
categories: jekyll update
---

# Design Patterns: Template Method

I was recently installing a couple of storm doors on the house we live in.  The door was not sold with
a handle, you have to buy the handle separately which is nice because it allows one to choose from
a few different styles and finishes. On top of that, the doors were not sold as either "left-hand" or
"right-hand"... meaning that if you would actually like a functioning door, you have to drill a hole
for the handle on one side of the door or the other, and place the hinge on one side or the other.

Pretty versatile door setup.  We're pretty happy with both doors.

The directions were very well written.  Most of the steps for assembling and attaching the door to its frame
fit on one page. There was a separate page included that on one side had the specific directions for a
"left-open" door and on the other side had directions for a "right-open" door.

The main directions page was too abstract to install the door.  But it did contain all of the same shared steps which meant
that the company did not have to print redundant directions for both installations.

## How does that relate to the template method pattern?

The Template method pattern is any time when a "Fill in the blanks" kind of solution can take place.

For this example we'll parse some data for the results of classes for some students.

The problem is that one class listing comes to us in Json (JavaScript Object Notation) and one comes to us in
Csv - (Comma Separated Values)...

Here is the Csv results for Chemistry 101...
```
StudentLastName,StudentFirstName,GradePercentage
Johnson,John,50
Silver,Silvia,67
```

and here are the Json results for English Literature...

{% highlight json %}
{
    "student": {
        "firstName": "John",
        "lastName": "Johnson",
        "gradePercentage": 34
    },
    "student": {
        "firstName": "Silvia",
        "lastName": "Silver",
        "gradePercentage": 26
    }
}
{% endhighlight %}


(these are not the brightest two in their grade...)

There is a piece of software in our school that takes all of the class reports and runs through them to gather all of the
grades for each student and produce a Report Card.  In order to create this report card we need to produce a data class
similar to...

{% highlight csharp %}
public class StudentClassGrade
{
    public string FirstName { get; set; }
    public string LastName { get; set; }
    public double GradePercentage { get; set; }
}
{% endhighlight %}


