# 100-puppet_ssh_config.pp
# configures a file to connect to a server without typing a password.
file_line {'Turn OFF PasswordAuthentication':
  path    => '/etc/ssh/ssh_config',
  line    => '    PasswordAuthentication no',
  replace => true
}

file_line {'Set Identity':
  path    => '/etc/ssh/ssh_config',
  line    => '    IdentityFile ~/.ssh/school',
  replace => true
}
