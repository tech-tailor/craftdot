$( document ).ready(function() {

  $('#accountState').change(function() {
    var selectedValue = $(this).val();
    var content = '';

    switch (selectedValue) {
      case 'profile':
        content = '<p>Welcome to your Profile</p>';
        history.pushState(null, '', '/account/profile');
        break;
      case 'password':
        content = '<p>Change your Password here</p>';
        history.pushState(null, '', '/account/password');
        break;
      case 'notification':
        content = '<p>Manage your Notifications</p>';
        history.pushState(null, '', '/account/notification');
        break;
      case 'my-task':
        content = '<p>Here are your Tasks</p>';
        history.pushState(null, '', '/account/my-tasks');
        break;
      default:
        content = '<p>Welcome to your Profile</p>';
        history.pushState(null, '', '/account/profile');
        break;
    }

    $('#content').html(content);
  });
});



