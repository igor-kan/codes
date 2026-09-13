/**
 * Concurrency-Bounded Asynchronous Map and Batch Pipeline.
 * 
 * Why JavaScript for this module?
 * Node.js and V8 event-loop architectures rely on non-blocking asynchronous I/O.
 * A concurrency limiter prevents socket exhaustion and memory spikes under high loads.
 */

async function pMap(items, mapper, concurrency = 4) {
    const results = new Array(items.length);
    let index = 0;
    
    async function worker() {
        while (index < items.length) {
            const currentIndex = index++;
            results[currentIndex] = await mapper(items[currentIndex], currentIndex);
        }
    }
    
    const workers = Array.from({ length: Math.min(concurrency, items.length) }, () => worker());
    await Promise.all(workers);
    return results;
}

// Test harness
async function main() {
    const items = [10, 20, 30, 40, 50, 60];
    const delays = [50, 20, 10, 30, 40, 10];
    
    const results = await pMap(items, async (item, idx) => {
        await new Promise(r => setTimeout(r, delays[idx]));
        return item * 2;
    }, 2);
    
    console.log("JavaScript Concurrency-Bounded pMap Result:", results);
}

if (typeof require !== "undefined" && require.main === module) {
    main();
}
