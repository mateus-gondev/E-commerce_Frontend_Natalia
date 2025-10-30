import { createApp } from 'vue'
import App from './App.vue'
import router from './routers'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css'
import BootstrapVue3 from 'bootstrap-vue-3'

const app = createApp(App)
app.config.devtools = false;
app.use(router)
app.use(BootstrapVue3)
app.mount('#app')
