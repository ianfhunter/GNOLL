const path = require('path');

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
