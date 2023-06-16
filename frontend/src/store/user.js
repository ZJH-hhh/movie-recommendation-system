import $ from 'jquery'
import jwt_decode from 'jwt-decode'

const modulesUser = {
    state: {
        userid: '',
        username: '',
        photo: '',
        access: '',
        refresh: '',
        is_login: false,
        favor_tags: [],
        favor_movies: [],
    },
    getters: {
    },
    mutations: {
        updateUser(state, user) {
            state.userid = user.id;
            state.username = user.username;
            state.photo = user.photo;
            state.access = user.access;
            state.refresh = user.refresh;
            state.is_login = user.is_login;
            state.favor_tags = user.favor_tags;
            state.favor_movies = user.favor_movies;
        },
        updateAccess(state, access) {
            state.access = access;
        },
        logout(state) {
            state.userid = '';
            state.username = '';
            state.photo = '';
            state.access = '';
            state.refresh = '';
            state.is_login = false;
            state.favor_tags = [];
            state.favor_movies = [];
        }
    },
    actions: {
        login(context, data) {
            $.ajax({
                url: 'http://8.130.99.147:8000/api/token/',
                type: 'POST',
                data: {
                    username: data.username,
                    password: data.password,
                },
                success: response => {
                    const { access, refresh } = response;
                    const access_obj = jwt_decode(access);
                    setInterval(() => {
                        $.ajax({
                            url: 'http://8.130.99.147:8000/api/token/refresh/',
                            type: 'POST',
                            data: {
                                refresh,
                            },
                            success: response => {
                                context.commit('updateAccess', response.access);
                            }
                        })
                    }, 4.5 * 60 * 1000);

                    $.ajax({
                        url: 'http://8.130.99.147:8000/api/getinfo/',
                        type: 'GET',
                        data: {
                            user_id: access_obj.user_id,
                        },
                        headers: {
                            "Authorization": "Bearer " + access,
                        },
                        success: response => {
                            console.log(response);
                            context.commit('updateUser', {
                                id: access_obj.user_id,
                                ...response,
                                access: access,
                                refresh: refresh,
                                is_login: true,
                            })
                        }
                    })
                    data.success();
                },
                error() {
                    data.error();
                }
            })
        },

        logout(context) {
            context.commit('logout');
        },

        update(context) {
            console.log(context.state.userid);
            $.ajax({
                url: 'http://8.130.99.147:8000/api/getinfo/',
                type: 'GET',
                data: {
                    user_id: context.state.user_id,
                },
                headers: {
                    "Authorization": "Bearer " + context.state.access,
                },
                success: response => {
                    console.log(response);
                    context.commit('updateUser', {
                        id: context.state.userid,
                        ...response,
                        access: context.state.access,
                        refresh: context.state.refresh,
                        is_login: true,
                    })
                }
            })
        }
    },
    modules: {
    }
}

export default modulesUser;