// Task 5:
const { Worker, isMainThread, parentPort, workerData } = require('worker_threads');
const os = require('os');

if (isMainThread) {
    // main thread
    const datasetSize = 10_000_000;
    const numThreads = os.cpus().length; // Use all available cores
    const chunkSize = Math.ceil(datasetSize / numThreads);
    
    console.log(`Starting parallel computing on ${numThreads} cores...`);
    const startTime = performance.now();

    const createWorker = (start, end) => {
        return new Promise((resolve, reject) => {
            const worker = new Worker(__filename, {
                workerData: { start, end }
            });
            worker.on('message', resolve);
            worker.on('error', reject);
        });
    };

    async function run() {
        const workers = [];
        for (let i = 0; i < numThreads; i++) {
            const start = i * chunkSize;
            const end = Math.min(start + chunkSize, datasetSize);
            workers.push(createWorker(start, end));
        }

        // Wait for all chunks to finish
        const resultsArray = await Promise.all(workers);
        
        // Flatten the chunks
        const results = resultsArray.flat();

        const endTime = performance.now();
        const duration = (endTime - startTime) / 1000;

        console.log(`Parallel processing finished in ${duration.toFixed(4)} seconds.`);
        console.log(`Computed ${results.length} results.`);
    }

    run();

} else {
    // worker thread
    const { start, end } = workerData;
    const chunkResults = [];

    // The actual computation
    for (let i = start; i < end; i++) {
        chunkResults.push(i * i);
    }

    // Send the chunk back to main thread
    parentPort.postMessage(chunkResults);
}