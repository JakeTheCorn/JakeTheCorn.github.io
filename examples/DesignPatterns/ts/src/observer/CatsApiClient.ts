interface ICatsApiClientDeps {
    httpClient: {
        get<T>(url): Promise<T>
    }
}

export class CatsApiClient {
    private listeners = {}

    constructor(private deps: ICatsApiClientDeps) {}

    getCats = async (): Promise<{ data?: string[], error?: Error }> => {
        this.runCallbacks('getCats.start'); // .notify('start')
        const { httpClient } = this.deps;
        try {
            const data = await httpClient.get<string[]>('/cats');
            this.runCallbacks('getCats.success', data); // .notify()
            return { data }
        } catch (error) {
            this.runCallbacks('getCats.error', error); // .notify()
            return { error }
        }
    }

    // .subscribe(...)

    on(event: 'getCats.start', handler: () => void)
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