let re_name = /^[가-힣]{2,4}$/g;
let re_userid = /^[a-z0-9]{6,12}$/g;
let re_email = /^([\w\.\_\-])*[a-zA-Z0-9]+([\w\.\_\-])*([a-zA-Z0-9])+([\w\.\_\-])+@([a-zA-Z0-9]+\.)+[a-zA-Z0-9]{2,8}$/i;
let re_password_with_specialkey = /^.*(?=^.{8,20}$)(?=.*\d)(?=.*[a-zA-Z])(?=.*[!@#$%^&+=]).*$/;
let re_password_without_specialkey = /^[A-Za-z0-9]{8,20}$/;;
let re_tel = /^010-\d{3,4}-\d{4}$/;