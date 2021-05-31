---
layout: post
title:  "Node js -- Calling Shell Scripts"
date:   2021-05-11 09:00:00 -0400
categories: jekyll update
---
This is a little utility I wrote to call shell scripts from node js.

The callback function can be supplied to do things as the script is processing.  By default, it just logs

{% highlight typescript %}
function runScript(command: string, args: string[], callback: Function = printRunScriptResults) {
    return new Promise((resolve, reject) => {
        const child = child_process.spawn(command, args, { shell: true });

        child.stdout.setEncoding('utf8');
        child.stdout.on('data', data => callback({ data: data.toString() }));

        child.stderr.setEncoding('utf8');
        child.stderr.on('data', data => callback({ error: data.toString() }));

        child.on('close', (code) => {
            if (code !== 0) {
                return reject(new Error(command + ' ' + args.join(' ') + ' exited with exit code ' + code))
            }
            resolve(code);
        });
    });
}

function printRunScriptResults({ data, error }) {
    typeof data === 'string' && process.stdout.write(data);
    error && console.error(error);
}

await runScript('docker', [
    `run \
        --rm \
        ubuntu:latest echo "hello"`
])
{% endhighlight %}
