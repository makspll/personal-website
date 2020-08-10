const path = require('path');

module.exports = {
    entry:  path.resolve('./client/index.js'),
    output: {
        path: path.resolve(__dirname, "static_src"), // string
        filename: "[name].js", // string
        publicPath: "/static_root/", // string 
        chunkFilename: "[id]-[chunkhash].js",
        libraryTarget: 'var',
        library: 'node_modules',
        },
    module: {
        rules: [{
            test: /\.(js|jsx)$/,
            exclude: /node_modules/,
            use: {
                loader: "babel-loader"
                }
            },
            {
                test: /\.css$/i,
                use: ['style-loader','css-loader']
            },
            {
                test: /\.s[ac]ss$/i,
                use: [
                  // Creates `style` nodes from JS strings
                  'style-loader',
                  // Translates CSS into CommonJS
                  'css-loader',
                  // Compiles Sass to CSS
                  'sass-loader',
                  // resolves relative css references to absolutes
                  'resolve-url-loader',
                ],
            },
        ]
    },
    devServer: {
        writeToDisk: true,
    },

}