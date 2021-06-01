---
layout: post
title:  "Testing NodeJs function runtime"
date:   2021-06-01 09:00:00 -0400
categories: jekyll update
---

using jest testing...

{% highlight typescript %}
const { performance } = require('perf_hooks');

describe('running with timeouts', () => {

    const tables = [
        ['name@gmail.com', true],
        ['amuchlongernam+asdfasdfadsfeinordertoshowanypossibleperformanceflaws@gmail.lskdjflkjsdlkfjjlksdjfds.com', true],
        ['with space@gmail.com', false]
    ]

    for (const [input, expected] of tables) {
        it('returns ' + expected + ' when given "' + input + '"', () => {
            const { returnValue, runtime } = withRuntime(() => {
                return /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/.test(input)
            })
            expect(returnValue).toBe(expected);
            expect(runtime).toBeLessThan(1)
        })
    }
})

function withRuntime(cb) {
    const start = performance.now();
    const returnValue = cb();
    const end = performance.now();
    return {
        runtime: end - start,
        returnValue,
    }
}

{% endhighlight %}
