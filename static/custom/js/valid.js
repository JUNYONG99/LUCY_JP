// 이름 검증 함수
function f_valid_name() {
    if (!re_name.exec($.trim($('#name').val()))) {
        $('#name_small').text('이름을 올바르게 입력해 주세요.(2글자 이상, 4글자 이하)');
        $('#name_small').removeClass('text-primary').addClass('text-danger');
        $('#name').removeClass('is-valid').addClass('is-invalid').val('').focus();
        return false;
    } else {
        $('#name_small').text('2글자 이상, 4글자 이하');
        $('#name_small').removeClass('text-danger').addClass('text-primary');
        $('#name').removeClass('is-invalid').addClass('is-valid');
    }
}

// 아이디 검증 함수
function f_valid_userid() {
    if (!re_userid.exec($.trim($('#userid').val()))) {
        $('#userid_small').text('아이디를 올바르게 입력해 주세요.(6글자 이상, 12글자 이하)');
        $('#userid_small').removeClass('text-primary').addClass('text-danger');
        $('#userid').removeClass('is-valid').addClass('is-invalid').val('').focus();
        return false;
    } else {
        $('#userid_small').text('6글자 이상, 12글자 이하');
        $('#userid_small').removeClass('text-danger').addClass('text-primary');
        $('#userid').removeClass('is-invalid').addClass('is-valid');
    }
}

// 비밀번호 검증 함수
function f_valid_password() {
    if (!re_password_with_specialkey.exec($.trim($('#password').val()))) {
        $('#password_small').text('영문,숫자,특수기호를 조합해 8자리 이상으로 입력해주세요.').removeClass('text-muted').addClass('text-danger');;
        $('#password_small').removeClass('text-primary').addClass('text-danger');
        $('#password').removeClass('is-valid').addClass('is-invalid').val('').focus();
        return false;
    } else {
        $('#password_small').text('').removeClass('text-muted').addClass('text-primary');;
        $('#password_small').removeClass('text-danger').addClass('text-primary');
        $('#password').removeClass('is-invalid').addClass('is-valid');
    }
}

// 비밀번호 확인 검증
function f_valid_password2() {
    if ($.trim($('#password').val()) != $.trim($('#password2').val())) {
        $('#password2_small').text('비밀번호가 일치하지 않습니다. ');
        $('#password2_small').removeClass('text-primary').addClass('text-danger');
        $('#password2').removeClass('is-valid').addClass('is-invalid').val('').focus();
        return false;
    } else {
        $('#password2_small').text('');
        $('#password2_small').removeClass('text-danger').addClass('text-primary');
        $('#password2').removeClass('is-invalid').addClass('is-valid');
    }
}

// 이메일 검증 함수
function f_valid_email() {
    if (!re_email.exec($.trim($('#email').val()))) {
        $('#email_small').text('이메일을 올바르게 입력해 주세요.');
        $('#email_small').removeClass('text-primary').addClass('text-danger');
        $('#email').removeClass('is-valid').addClass('is-invalid').val('').focus();
        return false;
    } else {
        $('#email').removeClass('is-invalid').addClass('is-valid');
    }
}

// 전화번호 검증 함수
function f_valid_tel() {
    if (!re_tel.exec($.trim($('#tel').val()))) {
        $('#tel_small').text('전화번호를 올바르게 입력해 주세요.(-포함, 예시) 010-1234-5678)');
        $('#tel_small').removeClass('text-primary').addClass('text-danger');
        $('#tel').removeClass('is-valid').addClass('is-invalid').val('').focus();
        return false;
    } else {
        $('#tel_small').text('-포함, 예시) 010-1234-5678)');
        $('#tel_small').removeClass('text-danger').addClass('text-primary');
        $('#tel').removeClass('is-invalid').addClass('is-valid');
    }
}