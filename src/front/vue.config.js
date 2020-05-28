// vue.config.js for less-loader@6.0.0
module.exports = {
    css: {
      loaderOptions: {
        less: {
          lessOptions: {
            modifyVars: {
              'primary-color': '#517E55',
              'link-color': '#517E55',
              'btn-border-radius-sm': '0px',
            },
            javascriptEnabled: true,
          },
        },
      },
    },
  };