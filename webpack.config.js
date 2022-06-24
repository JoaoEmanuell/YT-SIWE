const resolve = require('path').resolve;

module.exports = {
    entry: './siwe/js/app.js',
    output: {
        filename: 'index.js',
        path: resolve(__dirname, 'siwe', 'dist')
    }
};