const path = require('path')
const webpack = require('webpack')

module.exports = {
  mode: 'development',
  entry: './src/index.dev.js',
  output: {
    filename: 'dashboard.js',
    path: path.resolve(__dirname, 'dist'),
  },
  devServer: {
    contentBase: './dist',
    hot: true
  },
  devtool: 'inline-source-map',
  resolve: {
    alias: {
      'react-dom': '@hot-loader/react-dom',
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
      use: ['style-loader', 'css-loader']
    }]
  },
  plugins: [new webpack.DefinePlugin({
    PRODUCTION: false,
  })]
};
