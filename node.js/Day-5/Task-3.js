// Task 3:
const cluster = require('cluster');
const process = require('process');

const checkTask = () => {
    console.log(`Task running in process id: ${process.pid}`);
}

if(cluster.isPrimary) {
    console.log(`Primary process ${process.pid} is starting workers...`);

    const p1 = cluster.fork();
    const p2 = cluster.fork();

    let finished = 0;
    cluster.on('exit', (Worker, code, signal) => {
        finished++;
        if(finished == 2) {
            console.log("All processes done!");
        }
    });
} else {
    checkTask();
    process.exit(0);
}