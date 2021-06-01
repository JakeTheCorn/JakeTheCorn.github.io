---
layout: post
title:  "Testing Node debounce function"
date:   2021-06-01 09:12:00 -0400
categories: jekyll update
---

using jest testing...

{% highlight typescript %}
describe('getDebouncedVersion', () => {
    afterEach(() => {
        jest.useFakeTimers()
        jest.runOnlyPendingTimers()
        jest.useRealTimers()
    })

    it('delays the initial call to supplied function if under timeout', () => {
        jest.useFakeTimers();
        jest.advanceTimersByTime(0);
        const mockFn = jest.fn()
        const debounced = getDebouncedVersion(mockFn, 100)
        debounced(1, 1)
        jest.advanceTimersByTime(10);
        debounced(2, 2)
        jest.advanceTimersByTime(10);
        debounced(3, 3)
        expect(mockFn).toHaveBeenCalledTimes(0)
        jest.advanceTimersByTime(100);
        expect(mockFn).toHaveBeenCalledTimes(1)
        expect(mockFn).toHaveBeenCalledWith(3, 3)
    })

})

function getDebouncedVersion(fn, ms) {
    if (typeof ms !== 'number') {
        return function newFn(...args) {
            typeof fn === 'function' && fn(...args);
        }
    }
    let lastTimeoutHandle;
    return function newFn(...args) {
        lastTimeoutHandle && clearTimeout(lastTimeoutHandle);
        lastTimeoutHandle = setTimeout(() => {
            typeof fn === 'function' && fn(...args);
        }, ms)
    }
}

{% endhighlight %}
