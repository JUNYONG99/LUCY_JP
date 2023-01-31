// 名前検証関数
function f_valid_name() {
    if (!re_name.exec($.trim($('#name').val()))) {
        $('#name_small').text('名前を正しく入力してください。 (2文字以上、4文字以下)');
        $('#name_small').removeClass('text-primary').addClass('text-danger');
        $('#name').removeClass('is-valid').addClass('is-invalid').val('').focus();
        return false;
    } else {
        $('#name_small').text('2文字以上、4文字以下');
        $('#name_small').removeClass('text-danger').addClass('text-primary');
        $('#name').removeClass('is-invalid').addClass('is-valid');
    }
}

// ID検証関数
function f_valid_userid() {
    if (!re_userid.exec($.trim($('#userid').val()))) {
        $('#userid_small').text('IDを正しく入力してください。(6文字以上、12文字以下)');
        $('#userid_small').removeClass('text-primary').addClass('text-danger');
        $('#userid').removeClass('is-valid').addClass('is-invalid').val('').focus();
        return false;
    } else {
        $('#userid_small').text('6文字以上、12文字以下');
        $('#userid_small').removeClass('text-danger').addClass('text-primary');
        $('#userid').removeClass('is-invalid').addClass('is-valid');
    }
}

//　パスワード検証関数
function f_valid_password() {
    if (!re_password_with_specialkey.exec($.trim($('#password').val()))) {
        $('#password_small').text('英文、数字、特殊記号を組み合わせて8桁以上で入力してください。').removeClass('text-muted').addClass('text-danger');;
        $('#password_small').removeClass('text-primary').addClass('text-danger');
        $('#password').removeClass('is-valid').addClass('is-invalid').val('').focus();
        return false;
    } else {
        $('#password_small').text('').removeClass('text-muted').addClass('text-primary');;
        $('#password_small').removeClass('text-danger').addClass('text-primary');
        $('#password').removeClass('is-invalid').addClass('is-valid');
    }
}

// パスワード確認検証関数
function f_valid_password2() {
    if ($.trim($('#password').val()) != $.trim($('#password2').val())) {
        $('#password2_small').text('パスワードが一致しません。');
        $('#password2_small').removeClass('text-primary').addClass('text-danger');
        $('#password2').removeClass('is-valid').addClass('is-invalid').val('').focus();
        return false;
    } else {
        $('#password2_small').text('');
        $('#password2_small').removeClass('text-danger').addClass('text-primary');
        $('#password2').removeClass('is-invalid').addClass('is-valid');
    }
}

// メール検証関数
function f_valid_email() {
    if (!re_email.exec($.trim($('#email').val()))) {
        $('#email_small').text('メールを形式合わせて正しく入力してください。');
        $('#email_small').removeClass('text-primary').addClass('text-danger');
        $('#email').removeClass('is-valid').addClass('is-invalid').val('').focus();
        return false;
    } else {
        $('#email').removeClass('is-invalid').addClass('is-valid');
    }
}

// 電話番号検証関数
function f_valid_tel() {
    if (!re_tel.exec($.trim($('#tel').val()))) {
        $('#tel_small').text('電話番号を正しく入力してください。（-含む、例) 010-1234-5678)');
        $('#tel_small').removeClass('text-primary').addClass('text-danger');
        $('#tel').removeClass('is-valid').addClass('is-invalid').val('').focus();
        return false;
    } else {
        $('#tel_small').text('-含む、例) 010-1234-5678');
        $('#tel_small').removeClass('text-danger').addClass('text-primary');
        $('#tel').removeClass('is-invalid').addClass('is-valid');
    }
}