const path = require('path')
const webpack = require('webpack')
const OptimizeCssAssetsPlugin = require('optimize-css-assets-webpack-plugin')
const MiniCssExtractPlugin = require('mini-css-extract-plugin')

module.exports = {
  mode: 'production',
  entry: './src/index.prod.js',
  output: {
    filename: 'dashboard.js',
    path: path.resolve(__dirname, 'dist'),
  },
  resolve: {
    alias: {
      '@libs': path.resolve(__dirname, 'src', 'libs'),
      '@components': path.resolve(__dirname, 'src', 'components'),
      '@styles': path.resolve(__dirname, 'src', 'styles')
    }
  },
  module: {
    rules: [{
      test: /\.js$/,
      exclude: /node_modules/,
      use: {
        loader: 'babel-loader',
        options: {
          presets: ['@babel/preset-react']
        }
      }
    }, {
      test: /\.css$/i,
      use: [MiniCssExtractPlugin.loader, 'css-loader']
    }]
  },
  plugins: [
    new webpack.DefinePlugin({
      PRODUCTION: true,
    }),
    new OptimizeCssAssetsPlugin(),
    new MiniCssExtractPlugin({
      filename: 'style.css'
    })
  ]
};
