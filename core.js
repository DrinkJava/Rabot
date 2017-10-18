const login = require('facebook-chat-api');
const FB_EMAIL = process.env.FB_EMAIL;
const FB_PASSWORD = process.env.FB_PASSWORD;
const axios = require('axios');

login({email: FB_EMAIL, password: FB_PASSWORD}, (err, api) => {
    if(err) return console.error(err);

    api.listen((err, msg) => {
        axios.post('http://127.0.0.1:5000/', msg)
            .then((response) => {
                console.log(msg)
                console.log(response.data)
                api.sendMessage(response.data, msg.threadID);
            });
    });
});
