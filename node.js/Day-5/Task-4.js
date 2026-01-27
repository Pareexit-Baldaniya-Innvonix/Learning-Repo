// Task  4:
const fs = require('fs');
const path = require('path');
const { Readable } = require('stream');
const { finished } = require('stream/promises');

const downloadFolder = 'downloaded_images';

// Create folder if it doesn't exist
if (!fs.existsSync(downloadFolder)) {
    fs.mkdirSync(downloadFolder);
}

const downloadImage = async (url) => {
    try {
        const filename = path.join(downloadFolder, url.split('/').pop());
        console.log(`Starting download: ${url}`);

        const response = await fetch(url);

        if (!response.ok) throw new Error(`Status ${response.status}`);

        // Create a write stream for the destination file
        const fileStream = fs.createWriteStream(filename);
        
        // Use the body as a stream and pipe it to the file
        // This is memory efficient for large images
        await finished(Readable.fromWeb(response.body).pipe(fileStream));

        console.log(`Successfully saved to ${filename}`);
    } catch (e) {
        console.error(`Error downloading ${url}: ${e.message}`);
    }
};

const urls = [
    "https://picsum.photos/id/237/200/300.jpg",
    "https://picsum.photos/id/238/200/400.jpg",
    "https://picsum.photos/id/239/200/500.jpg",
    "https://picsum.photos/id/240/200/600.jpg",
    "https://picsum.photos/id/241/200/700.jpg",
];

// Run all downloads in parallel
async function run() {
    await Promise.all(urls.map(url => downloadImage(url)));
    console.log("\nAll downloads completed!");
}

run();