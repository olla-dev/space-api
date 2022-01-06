import Vue from 'vue'
import VueRouter from 'vue-router'

import App from './App.vue'
import router from './router'

Vue.use(VueRouter)

require('@/assets/styles/app.css')

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
