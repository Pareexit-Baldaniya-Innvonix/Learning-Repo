// Task 2:
const {Worker, isMainThread, parentPort, workerData} = require('worker_threads');

// handles work and delay
const delay = (ms) => new Promise(res => setTimeout(res, ms));

if (isMainThread) {
    // main thread
    const runWorker = (taskName, num) => {
        return new Promise((resolve) => {
            const worker = new Worker(__filename, {
                workerData: {taskName, num}
            });
            worker.on('exit', resolve);
        });
    };

    async function main() {
        const t1 = runWorker('Square', 4);
        const t2 = runWorker('Cube', 4);

        await Promise.all([t1, t2]);
        console.log("Done!");
    }
    main();
} else {
    // worker thread
    const {taskName, num} = workerData;

    async function performTask() {
        if(taskName === 'Square') {
            console.log(`Square of ${num}: `, num*num);
        } else if(taskName === 'Cube') {
            console.log(`Cube of ${num}: `, num*num*num);
        }
        await delay(10000);
        process.exit(0);
    }
    performTask();
}