const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
    plugins: [new MiniCssExtractPlugin({
        filename: '[name].css',
        chunkFilename: '[id].css',
    })],
    entry:  path.resolve('./client/index.js'),
    output: {
        path: path.resolve(__dirname, "static_src"), // string
        filename: "[name].js", // string
        publicPath: "/static_root/", // string 
        chunkFilename: "[id]-[chunkhash].js",
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
                    {
                        loader: MiniCssExtractPlugin.loader,
                        options: {
                            hmr: process.env.NODE_ENV ==='development',
                        },   
                    },
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