---
layout: post
title:  "Design Patterns - Observer - TypeScript"
date:   2021-06-02 09:00:00 -0400
categories: jekyll update
---

# The Observer Pattern

TL;DR; "Call me when something I care about occurs".

The Problem occurs when a client cares about a particular event.

For Example, if a movie store has a particular movie ready for rent.

The client might solve this by repeatedly checking the movie store. Making many trips, and mostly
unsuccessful until the movie is in stock.

The Movie Store might solve this by calling the client every time a movie gets returned.  But this
is annoying and also wastes a lot of effort. (It's SPAM!)

A Better solution might be for the movie store to keep track of customers who are interested in a
particular movie.  That way the only communication that occurs is communication that is valuable.

For this example we'll use the status of a network call. Let's say it has 3 possible states...

    network states:
        start
        success
        error

For this example we don't care what we would like to do during these states, that's up to larger
application concerns

## Details

There are two members in the observer pattern...

the Subject - the one being observed
and
the Observer - the one who is observing

sometimes referred to by different names.

it works by the subject having a `.subscribe(Observer observer)` that takes in an observer.

when `.subscribe(Observer observer)` is called, the Subject adds the Observer to some kind of collection it is tracking -- basically a list of who to call when an event happens.

but what to call?

there will be something analogous to an `.update(...)` method on the observer class that the Subject will know to call with relevant updates.

but..

## The code does not have to read exactly the same to be using a particular pattern

in this example, I'm be using the method `on(event: EventName, handler: Function)` instead of the more
standard `.subscribe(...)`.

and in place of the standard `.update(...)` method, I'm using regular old functions, since JS supports first class functions.

but it's the same idea.  "Call me when something I care about occurs".

## Tests

A test might look like...

{% highlight typescript %}
import { CatsApiClient } from "./CatsApiClient";

describe('The Observer Pattern', () => {
    describe('how it works...', () => {
        it('allows clients to "subscribe" to events they care about', async () => {
            let resolve;
            let reject;

            const httpClient = {
                get(url) {
                    return new Promise<string[]>((res, rej) => {
                        resolve = res;
                        reject = rej;
                    }) as any
                }
            }

            let onGetCatsStart = jest.fn();
            let onGetCatsSuccess = jest.fn();
            let onGetCatsError = jest.fn();

            let client = new CatsApiClient({ httpClient });
            client
                .on('getCats.start', onGetCatsStart)
                .on('getCats.success', onGetCatsSuccess)
                .on('getCats.error', onGetCatsError);

            client.getCats()

            expect(onGetCatsStart).toHaveBeenCalledTimes(1);
            expect(onGetCatsSuccess).not.toHaveBeenCalled();
            expect(onGetCatsError).toHaveBeenCalledTimes(0);

            const catNames = ['beefcake' ,'muscle-cat'];

            await resolve(catNames);

            expect(onGetCatsStart).toHaveBeenCalledTimes(1);
            expect(onGetCatsSuccess).toHaveBeenCalledTimes(1);
            expect(onGetCatsSuccess).toHaveBeenCalledWith(catNames);
            expect(onGetCatsError).toHaveBeenCalledTimes(0);

            jest.resetAllMocks();

            client = new CatsApiClient({ httpClient })
                .on('getCats.start', onGetCatsStart)
                .on('getCats.success', onGetCatsSuccess)
                .on('getCats.error', onGetCatsError);

            client.getCats()

            expect(onGetCatsStart).toHaveBeenCalledTimes(1);
            expect(onGetCatsSuccess).not.toHaveBeenCalled();
            expect(onGetCatsError).toHaveBeenCalledTimes(0);

            const err = new Error('not found');
            await reject(err);

            expect(onGetCatsStart).toHaveBeenCalledTimes(1);
            expect(onGetCatsSuccess).toHaveBeenCalledTimes(0);
            expect(onGetCatsError).toHaveBeenCalledTimes(1);
            expect(onGetCatsError).toHaveBeenCalledWith(err);
        })
    })
})
{% endhighlight %}

## Implementation

{% highlight typescript %}
interface ICatsApiClientDeps {
    httpClient: {
        get<T>(url): Promise<T>
    }
}

export class CatsApiClient {
    private listeners = {}

    constructor(private deps: ICatsApiClientDeps) {}

    getCats = async (): Promise<{ data?: string[], error?: Error }> => {
        this.runCallbacks('getCats.start'); // .notify(...)
        const { httpClient } = this.deps;
        try {
            const data = await httpClient.get<string[]>('/cats');
            this.runCallbacks('getCats.success', data); // .notify(...)
            return { data }
        } catch (error) {
            this.runCallbacks('getCats.error', error); // .notify(...)
            return { error }
        }
    }

    // .subscribe(...)
    on(event: 'getCats.start', handler: () => void) // handler is equivalent to .update(...)
    on(event: 'getCats.success', handler: (data: string[]) => void)
    on(event: 'getCats.error', handler: (error: Error) => void)
    on(event: EventName, handler: Function): this {
        if (!Array.isArray(this.listeners[event])) {
            this.listeners[event] = [];
        }
        this.listeners[event].push(handler);
        return this;
    }

    private runCallbacks = (event: EventName, ...args: unknown[]): void => {
        const callbacks = this.listeners[event];
        Array.isArray(callbacks) && callbacks.forEach(f => f(...args))
    }
}

type EventName =
    'getCats.start' |
    'getCats.success' |
    'getCats.error';

{% endhighlight %}


Thanks for the read.
