<template>
  <div class="login-register-card">
    <el-row>
      <el-col :span="12">
        <el-card class="box-card card-left">
        </el-card>
      </el-col>
      <el-col :span="12" v-if="method=='register'">
        <el-card class="box-card card-right">
          <el-form :model="data" style="margin-top: 60px;">
            <el-form-item class="form-item">
              <el-input v-model="data.username" placeholder="用户名" class="input-box" type="text"/>
            </el-form-item>
            <el-form-item class="form-item">
              <el-input v-model="data.password" placeholder="密码" class="input-box" type="password"/>
            </el-form-item>
            <el-form-item class="form-item">
              <el-input v-model="data.password_confirm" placeholder="确认密码" class="input-box" type="password"/>
            </el-form-item>
            <el-form-item class="form-item">
              <div class="error-message" style="color: red">{{ error_message }}</div>
            </el-form-item>
            <el-form-item class="form-item">
              <el-button type="primary" @click="register" style="width: 294.4px; height: 40px;">注册</el-button>
            </el-form-item>
            <el-form-item class="form-item" style="float: right">
              <span @click="change_method" style="color: white; cursor: pointer">登录</span>
            </el-form-item>
          </el-form>
        </el-card>
      </el-col>

      <el-col :span="12" v-if="method=='login'">
        <el-card class="box-card card-right">
          <el-form :model="data" style="margin-top: 60px;">
            <el-form-item class="form-item">
              <el-input v-model="data.username" placeholder="用户名" class="input-box" type="text"/>
            </el-form-item>
            <el-form-item class="form-item">
              <el-input v-model="data.password" placeholder="密码" class="input-box" type="password"/>
            </el-form-item>
            <el-form-item class="form-item">
              <div class="error-message" style="color: red">{{ error_message }}</div>
            </el-form-item>
            <el-form-item class="form-item">
              <el-button type="primary" @click="login" style="width: 294.4px; height: 40px;">登录</el-button>
            </el-form-item>
            <el-form-item class="form-item" style="float: right">
              <span @click="change_method" style="color: white; cursor: pointer">注册</span>
            </el-form-item>
          </el-form>
        </el-card>
      </el-col>
    </el-row>
  </div>

<!--  <el-card class="box-card register-card">-->
<!--    <el-form :model="form" label-width="120px">-->
<!--      <el-form-item label="用户名">-->
<!--        <el-input v-model="form.name" />-->
<!--      </el-form-item>-->
<!--      <el-form-item label="密码">-->
<!--        <el-input v-model="form.password" />-->
<!--      </el-form-item>-->
<!--      <el-form-item label="确认密码">-->
<!--        <el-input v-model="form.confirm_password" />-->
<!--      </el-form-item>-->
<!--      <el-form-item label="感兴趣的类型">-->
<!--        <el-checkbox-group v-model="form.type">-->
<!--          <el-checkbox label="动作" name="type" />-->
<!--          <el-checkbox label="喜剧" name="type" />-->
<!--          <el-checkbox label="剧情" name="type" />-->
<!--          <el-checkbox label="爱情" name="type" />-->
<!--          <el-checkbox label="科幻" name="type" />-->
<!--          <el-checkbox label="动画" name="type" />-->
<!--          <el-checkbox label="悬疑" name="type" />-->
<!--          <el-checkbox label="惊悚" name="type" />-->
<!--          <el-checkbox label="恐怖" name="type" />-->
<!--          <el-checkbox label="纪录片" name="type" />-->
<!--          <el-checkbox label="短片" name="type" />-->
<!--          <el-checkbox label="情色" name="type" />-->
<!--          <el-checkbox label="音乐" name="type" />-->
<!--          <el-checkbox label="歌舞" name="type" />-->
<!--          <el-checkbox label="家庭" name="type" />-->
<!--          <el-checkbox label="儿童" name="type" />-->
<!--          <el-checkbox label="传记" name="type" />-->
<!--          <el-checkbox label="历史" name="type" />-->
<!--          <el-checkbox label="战争" name="type" />-->
<!--          <el-checkbox label="犯罪" name="type" />-->
<!--          <el-checkbox label="西部" name="type" />-->
<!--          <el-checkbox label="奇幻" name="type" />-->
<!--          <el-checkbox label="冒险" name="type" />-->
<!--          <el-checkbox label="灾难" name="type" />-->
<!--          <el-checkbox label="武侠" name="type" />-->
<!--          <el-checkbox label="古装" name="type" />-->
<!--          <el-checkbox label="运动" name="type" />-->
<!--          <el-checkbox label="黑色电影" name="type" />-->
<!--        </el-checkbox-group>-->
<!--      </el-form-item>-->
<!--      <el-form-item>-->
<!--        <el-button type="primary" @click="onSubmit">注册</el-button>-->
<!--        <el-button>取消</el-button>-->
<!--      </el-form-item>-->
<!--    </el-form>-->
<!--  </el-card>-->
</template>

<script setup>
import { reactive, ref } from 'vue';
import { useStore } from 'vuex';
import router from '@/router/index';
import $ from 'jquery';

const data = reactive({
  username: '',
  password: '',
  password_confirm: '',
});

const store = useStore();
let error_message = ref('');
let method = ref('login');

const change_method = () => {
  if (method.value === 'login') method.value = 'register';
  else method.value = 'login';
}

const login = () => {
  error_message.value = '';
  store.dispatch("login", {
      username: data.username,
      password: data.password,
      success() {
          router.push('/');
      },
      error() {
          error_message.value = '用户名或密码错误';
      }
  })
}

const register = () => {
  error_message.value = '';
  $.ajax({
    url: 'http://8.130.99.147:8000/api/register/',
    type: 'POST',
    data: {
      username: data.username,
      password: data.password,
      password_confirm: data.password_confirm,
    },
    success: response => {
      if (response.result === 'success') {
        store.dispatch('login', {
          username: data.username,
          password: data.password,
          success: () => {
            router.push({ path: '/'});
          },
          error: () => {
            error_message.value = '用户名或密码错误';
          }
        });
      } else {
        error_message.value = response.result;
      }
      console.log(response);
    }
  })
}
</script>

<style scoped>
.login-register-card {
  position: relative;
  width: 700px;
  height: 507px;
  /*background-color: lightcoral;*/
  margin: 100px auto auto 400px;
}

.card-left {
  width: 350px;
  height: 507px;
  box-sizing: border-box;
  position: relative;
  border-radius: 12px 0 0 12px;
  z-index: 1;
  background-color: lightcoral;
}

.card-right {
  width: 376px;
  height: 507px;
  box-sizing: border-box;
  position: absolute;
  right: 0px;
  font-family: 'MicrosoftYaHei';
  border-radius: 12px;
  background-color: #1e2126;
  box-shadow: -8px 2px 10px 0 rgba(0, 0, 0, 0.2);
  z-index: 99;
}

.form-item {
  margin-left: 20px;
  margin-right: 20px;
}

.input-box {
  height: 48px;
  font-size: 16px;
}
</style>