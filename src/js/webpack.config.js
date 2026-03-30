const path = require('path');
const webpack = require('webpack');

module.exports = {
  mode: 'development',
  entry: {
    wrapper: {
      import: './gnoll.js',
    },
  },
  node: {
    global: true,
    __filename: true,
    __dirname: true,
  },
  resolve: {
    fallback: {
      fs: require.resolve('browserify-fs'),
      path: require.resolve('path-browserify'),
      buffer: require.resolve('buffer'),
      stream: require.resolve('stream-browserify'),
      crypto: require.resolve("crypto-browserify"),
      vm: require.resolve("vm-browserify")
    }
  },
  plugins: [
    // Emscripten emits import 'node:fs' / 'node:crypto'; webpack 5 does not resolve node: URIs.
    new webpack.NormalModuleReplacementPlugin(
      /^node:fs$/,
      require.resolve('browserify-fs')
    ),
    new webpack.NormalModuleReplacementPlugin(
      /^node:crypto$/,
      require.resolve('crypto-browserify')
    ),
  ],
  devtool: 'source-map',
  output: {
    filename: 'gnoll.bundle.js',
    path: path.resolve(__dirname, '../../build/jsweb/'),
    library: 'gnoll'
  },
  experiments: {
    asyncWebAssembly: true,
    syncWebAssembly: true
  },
  devServer: {
    static: {
      directory: path.join(__dirname, 'dist'),
    },
    compress: true,
    port: 9000
  },
}
