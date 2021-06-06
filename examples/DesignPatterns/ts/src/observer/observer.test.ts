/**
 * The Observer Pattern
 *
 * The Problem occurs when a client cares about a particular event.
 *
 * For Example, if a movie store has a particular movie ready for rent.
 *
 * The client might solve this by repeatedly checking the movie store. Making many trips, and mostly
 * unsuccessful until the movie is in stock.
 *
 * The Movie Store might solve this by calling the client every time a movie gets returned.  But this
 * is annoying and also wastes a lot of effort. (It's SPAM!)
 *
 * A Better solution might be for the movie store to keep track of customers who are interested in a
 * particular movie.  That way the only communication that occurs is communication that is valuable.
 *
 * For this example we'll use the status of a network call. Let's say it has 3 possible states...
 *
 *      network states:
 *          start
 *          success
 *          error
 *
 * For this example we don't care what we would like to do during these states, that's up to larger
 * application concerns
 *
 */

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

