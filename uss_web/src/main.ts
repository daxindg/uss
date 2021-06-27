import { createApp } from 'vue'
import App from './App.vue'
import { ElInput, ElContainer, ElAlert, ElButton, ElHeader, ElMain, ElCol, ElRow, ElNotification } from 'element-plus';
//import 'element-plus/lib/theme-chalk/index.css'
import 'element-plus/packages/theme-chalk/src/index.scss'

const app = createApp(App)
const components = [
    ElButton,
    ElHeader,
    ElMain,
    ElRow,
    ElCol,
    ElContainer,
    ElInput,
    ElAlert
];
const plugins = [
    ElNotification
];

components.forEach(c => {
    app.component(c.name, c);
});

plugins.forEach(p => {
    app.use(p);
});

app.mount("#app")
