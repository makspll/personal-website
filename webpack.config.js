const path = require('path');

module.exports = {
    entry:  path.resolve('./client/index.js'),
    output: {
        path: path.resolve(__dirname, "static_root"), // string
        filename: "[name].js", // string
        publicPath: "/static_root/", // string 
        chunkFilename: "[id]-[chunkhash].js",
        libraryTarget: 'var',
        library: 'node_modules',
        },
    module: {
        rules: [
            {
            test: /\.(js|jsx)$/,
            exclude: /node_modules/,
            use: {
                loader: "babel-loader"
            }
            }
        ]
    },
    devServer: {
        writeToDisk: true,
    },

}