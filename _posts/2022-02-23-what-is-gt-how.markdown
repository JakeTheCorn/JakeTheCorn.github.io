---
layout: post
title:  '"What" is more important than "How"'
date: 2022-02-23 09:00:00 -0400
categories: jekyll update
---

Todo: article in progress...

## We naturally care more about "What happened" than "How"

If I told you how something happened before telling you what happened it could be very confusing and time wasting. Imagine I tell you all about the inner workings of a combustion engine
before I tell you that I drove to the grocery.  This pattern follows in the ways we humans communicate. We want to know what happened before we want to know how it happened.  Newspapers have
sections, then titles, then leading paragraphs, finally followed by the smaller details.  Details in the natural world are accessed by zooming in to the upper level.


## Left to Right

You're currently able to read this sentence because you started from the left side of it. I didn't have to tell you to do that.  It is how we tend to read things in the English speaking world.

We read left to right.


## Top to Bottom

You're also able to read this because you're reading ...

```
top
to
bottom
```

## How does this affect how we should organize software?

Software should be written for humans.  In the English language we read from left to right then top to bottom.  So following the ideas laid out above
it makes sense to organize our code with higher level concepts on the left and above details.

I have no data for proof, but I guess this is why recent languages try to keep names on the left and types on the right.  Not that a type can't be a high level concept, but in most cases
the name of a thing should convey higher level details than the type itself.


## Function / Method organization

Often I see programs written where everything is forward declared. Meaning given the following javascript...

``` javascript
function getEmailValidationErrorMessage(email) {
    // ...
    // ...
    // ...
    // ...
    return validationErrorMessage;
}

function getUsernameValidationErrorMessage(username) {
    // ...
    // ...
    // ...
    // ...
    return validationErrorMessage;
}

function getPhoneValidationErrorMessage() {
    // ...
    // ...
    // ...
    // ...
    return validationErrorMessage;
}

export function getValidationErrors(form) {
    return {
        email: getEmailValidationErrorMessage(form.email),
        username: getUsernameValidationErrorMessage(form.username),
        phone: getPhoneValidationErrorMessage(form.email),
    };
}
```

In the previous example one has to read through all the details of how each function does its work before we get to the thing that is actually used.

While there are other problems with this code, an easy win could be attained by re-ordering the code so that the smaller details live under the higher level ones....

``` javascript
// what it does ...
export function getValidationErrors(form) {
    return {
        email: getEmailValidationErrorMessage(form.email),
        username: getUsernameValidationErrorMessage(form.username),
        phone: getPhoneValidationErrorMessage(form.email),
    };
}

// followed by how...

function getEmailValidationErrorMessage(email) {
    // ...
    // ...
    // ...
    // ...
    return validationErrorMessage;
}

function getUsernameValidationErrorMessage(username) {
    // ...
    // ...
    // ...
    // ...
    return validationErrorMessage;
}

function getPhoneValidationErrorMessage() {
    // ...
    // ...
    // ...
    // ...
    return validationErrorMessage;
}
```


## Arguments
If multiple arguments are used, hopefully they are used with the more important ones on the left.


``` csharp

// why it should be false is important to the human reading before the software element holding the value becomes important.

Assert.False("User form should fail validation if email is malformed", validationReport.HasValidUserEmail);

// vs

Assert.False(validationReport.HasValidUserEmail, "User form should fail validation if email is malformed");
```


## Constructors

    A public constructor might say a lot about how a class works internally, hopefully not, but it happens.  So why are constructors so often found at top of classes even above public methods?

    Because constructors say "What I need"



