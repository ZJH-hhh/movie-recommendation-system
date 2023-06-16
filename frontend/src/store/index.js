import { createStore } from 'vuex'
import modulesUser from './user';

export default createStore({
    state: { // 存储所有全局数据
    },
    getters: { // 存储state中需要计算获得的内容
    },
    mutations: { // 所有修改state的内容的操作都要放到mutations，不能执行异步操作
    },
    actions: { // 定义对state的各种操作
    },
    modules: { // 将state数据分成若干个modules存储
        user: modulesUser
    }
})