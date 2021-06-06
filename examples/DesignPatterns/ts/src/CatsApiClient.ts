import axios from 'axios'

class ApiClient {
    get<T>(url): Promise<T> {
        return axios
            .get(url)
            .then(x => x.data)
    }
}

interface ICatsApiClientDeps {
    httpClient: {
        get<T>(url): Promise<T>
    }
}

export class CatsApiClient extends ApiClient {
    private listeners = {}

    constructor(private deps: ICatsApiClientDeps) {
        super(); // todo
    }

    getCats = async (): Promise<{ data?: string[], error?: Error }> => {
        const onStartCallbacks = this.listeners['getCats.start']
        if (Array.isArray(onStartCallbacks)) {
            onStartCallbacks.forEach(f => f())
        }
        try {
            const { httpClient } = this.deps;
            const response = await httpClient.get<string[]>('/cats');
            const onSuccessCallbacks = this.listeners['getCats.success'];
            if (Array.isArray(onSuccessCallbacks)) {
                for (const onSuccess of onSuccessCallbacks) {
                    typeof onSuccess === 'function' && onSuccess(response)
                }
            }
            return {
                data: response,
            }
        } catch (error) {
            const onErrorCallbacks = this.listeners['getCats.error'];
            if (Array.isArray(onErrorCallbacks)) {
                onErrorCallbacks.forEach(f => f(error))
            }
            return {
                error,
            }
        }
    }

    on = (event: EventName, handler: Function): this => {
        if (!Array.isArray(this.listeners[event])) {
            this.listeners[event] = [];
        }
        this.listeners[event].push(handler);
        return this;
    }
}

type EventName =
    'getCats.start' |
    'getCats.success' |
    'getCats.error';
