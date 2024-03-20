const path = require('path');

module.exports = {
  mode: 'development',
  entry: {
    wrapper: {
      import: './src/js/wrapper.js',
    }
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
  output: {
    filename: 'gnoll.js',
    path: path.resolve(__dirname, '../../build/jsweb/')
  },
  experiments: {
    asyncWebAssembly: true,
    syncWebAssembly: true
  },
  module: {
      rules: [
          {
              test: /\.wasm$/,
              // Tells webpack how to interpret wasm files into JavaScript-land
              loader: "wasm-loader"
          }
      ]
  },
  devServer: {
    static: {
      directory: path.join(__dirname, 'dist'),
    },
    compress: true,
    port: 9000
  }
}
